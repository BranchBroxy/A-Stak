import numpy as np
import h5py  # hdf5
import scipy.io
import os
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
import os
import glob
import math

filepath = ""
name = ""
main_ui = object
extension = ""

data = []
spike_list = np.zeros(0)
amp = np.zeros(0)
rec_dur = 0
SaRa = 0
files = []

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            name, extension = os.path.splitext(fullPath)
            if extension == ".mat" or extension == ".bxr" or extension == ".dat" or extension == ".h5":
                allFiles.append(fullPath)

    return allFiles


def get_variables():
    global spike_list
    global amp
    global rec_dur
    global SaRa
    return spike_list, amp, rec_dur, SaRa

def get_file_and_extension():
    global filepath
    global extension
    return filepath, extension

def retun_files():
    global files
    return files

def get_data_list():
    print("here")
    return data


def get_filepath(ui):
    global name
    global filepath
    global extension
    global main_ui
    main_ui = ui
    if ui.d_tab_checkbox.isChecked():
        filename = QFileDialog.getExistingDirectory()
        filepath = filename
    else:
        filename = QFileDialog.getOpenFileName()
        filepath = filename[0]
        main_ui.d_tab_browse_frame_lineEdit.setText(filepath)
        main_ui.d_tab_browse_frame_lineEdit.setEnabled(False)
        name, extension = os.path.splitext(filepath)


def import_bxr():
    global main_ui
    global filepath
    ui = main_ui

    global spike_list
    global amp
    global rec_dur
    global SaRa
    path = filepath
    bxr_data = ReadBxr(path)
    spike_list = convert_to_elephant_array_bxr(bxr_data)
    # ch, ts = get_spiketimes(bxr_data)
    amp = np.zeros([spike_list.shape[1], spike_list.shape[0]])
    SaRa = bxr_data.sf
    rec_dur = bxr_data.recLenght
    print("Bxr Datei erfolgreich importiert")
    ui.MainTextBrowser.setText("Bxr Datei erfolgreich importiert")

    return spike_list, amp, rec_dur, SaRa


def import_dat():
    global main_ui
    global filepath

    ui = main_ui
    path = filepath

    global spike_list
    global amp
    global rec_dur
    global SaRa

    i = pd.read_csv(path, sep="\s+", encoding="cp1252", nrows=0)
    meta = list(i.columns.values)
    data = pd.read_csv(path, sep="\s+", encoding="cp1252", skiprows=3)
    rec_dur = data.iloc[:, 0].max() # Recording Duration
    SaRa = meta[2] # Sample Rate
    spike_list = data.iloc[:, 1:].to_numpy()
    amp = np.zeros([spike_list.shape[1], spike_list.shape[0]])

    print("Dat Datei erfolgreich importiert")
    ui.MainTextBrowser.setText("Dat Datei erfolgreich importiert")

def import_mat(path):
    global main_ui
    global filepath

    ui = main_ui




    mat_data = scipy.io.loadmat(path)
    try:
        spike_list = np.transpose(mat_data["SPIKEZ"]["TS"][0, 0])
        # if spike_list.shape ==
        spike_list = np.where(np.invert(np.isnan(spike_list)), spike_list, 0)
        amp = np.zeros([spike_list.shape[1], spike_list.shape[0]])
        rec_dur = float(mat_data["SPIKEZ"][0, 0]["PREF"][0, 0]["rec_dur"][0])
        SaRa = mat_data["SPIKEZ"][0, 0]["PREF"][0, 0]["SaRa"][0][0]
        flag_mat_v1 = True
        if np.transpose(mat_data["temp"]["SPIKEZ"][0, 0]["TS"][0, 0]).shape[1] == 0:
            print("Mat Datei leer")
            ui.MainTextBrowser.setText("Mat Datei leer")
            spike_list = np.array([1, 1])
            amp = np.array([0, 0])
            rec_dur = 1
            SaRa = 1000
        else:
            print("Mat Datei erfolgreich importiert")
            ui.MainTextBrowser.setText("Mat Datei erfolgreich importiert")
    except:
        try:
            spike_list = np.transpose(mat_data["temp"]["SPIKEZ"][0, 0]["TS"][0, 0])
            amp = mat_data["temp"]["SPIKEZ"][0, 0]["AMP"][0, 0]
            rec_dur = mat_data["temp"]["SPIKEZ"][0, 0]["PREF"][0,0]["rec_dur"][0, 0][0][0]
            SaRa = mat_data["temp"]["SPIKEZ"][0, 0]["PREF"][0, 0]["SaRa"][0, 0][0][0]
            flat_mat_v2 = True
            if np.transpose(mat_data["temp"]["SPIKEZ"][0, 0]["TS"][0, 0]).shape[1] == 0:
                print("Mat Datei leer")
                ui.MainTextBrowser.setText("Mat Datei leer")
                spike_list = np.array([1, 1])
                amp = np.array([0, 0])
                rec_dur = 1
                SaRa = 1000
            else:
                print("Mat Datei erfolgreich importiert")
                ui.MainTextBrowser.setText("Mat Datei erfolgreich importiert")
        except:
            print("Mat Datei konnte nicht importiert werden")
            ui.MainTextBrowser.setText("Mat Datei konnte nicht erfolgreich importiert werden")

    print("here")
    return spike_list, amp, rec_dur, SaRa

def import_h5_old(path):
    global main_ui
    global filepath
    ui = main_ui

    spikes = []
    max_length_array = 0
    rec_dur = 0
    SaRa = 10000

    h5 = h5py.File(path, 'r')
    h5_data = h5["Data/Recording_0/TimeStampStream/Stream_0"]
    for i in h5_data:
        if i != "InfoTimeStamp":
            if np.array(h5_data[i]).max()/1000000 > rec_dur:
                rec_dur = np.array(h5_data[i]).max()/1000000

            if np.array(h5_data[i]).size > max_length_array:
                max_length_array = np.array(h5_data[i]).size

    spikes = np.zeros(shape=(60, max_length_array))
    x = 0
    y = 0

    for counter, a in enumerate(h5_data):
        if a != "InfoTimeStamp":
            electrode = np.array(h5_data[a])/1000000
            spikes[x+counter:x+counter+electrode.shape[0], y:y+electrode.shape[1]] = electrode
    spike_list = spikes
    #spike_list = np.transpose(spikes)
    amp = np.zeros([spike_list.shape[1], spike_list.shape[0]])
    return spike_list, amp, rec_dur, SaRa

def import_h5(path):
    import re
    global main_ui
    global filepath
    ui = main_ui

    TSE_ID_to_Label = {
                21:  0, 31:  1, 41:  2, 51:  3, 61:  4, 71:  5,
        12:  6, 22:  7, 32:  8, 42:  9, 52: 10, 62: 11, 72: 12, 82: 13,
        13: 14, 23: 15, 33: 16, 43: 17, 53: 18, 63: 19, 73: 20, 83: 21,
        14: 22, 24: 23, 34: 24, 44: 25, 54: 26, 64: 27, 74: 28, 84: 29,
        15: 30, 25: 31, 35: 32, 45: 33, 55: 34, 65: 35, 75: 36, 85: 37,
        16: 38, 26: 39, 36: 40, 46: 41, 56: 42, 66: 43, 76: 44, 86: 45,
        17: 46, 27: 47, 37: 48, 47: 49, 57: 50, 67: 51, 77: 52, 87: 53,
                28: 54, 38: 55, 48: 56, 58: 57, 68: 58, 78: 59,
    }

    spikes = []
    max_length_array = 0
    rec_dur = 0
    SaRa = 10000

    h5 = h5py.File(path, 'r')
    h5_data = h5["Data/Recording_0/TimeStampStream/Stream_0"]

    # SoureChannel
    for i in h5_data:
        if i != "InfoTimeStamp":
            if np.array(h5_data[i]).max()/1000000 > rec_dur:
                rec_dur = np.array(h5_data[i]).max()/1000000

            if np.array(h5_data[i]).size > max_length_array:
                max_length_array = np.array(h5_data[i]).size

    spikes = np.zeros(shape=(60, max_length_array))
    x = 0
    y = 0

    for counter, a in enumerate(h5_data):
        if a != "InfoTimeStamp":
            electrode = np.array(h5_data[a])/1000000

            time_stamp_entity_id = int(re.search(r'\d+', a).group())
            TimeStampEntityID = h5_data["InfoTimeStamp"]["TimeStampEntityID"]
            index = int(np.where(TimeStampEntityID == time_stamp_entity_id)[0])
            label = int(h5_data["InfoTimeStamp"]["Label"][index])

            electrode_row = TSE_ID_to_Label[label]

            spikes[electrode_row:electrode_row+electrode.shape[0], y:y+electrode.shape[1]] = electrode
    spike_list = spikes
    #spike_list = np.transpose(spikes)
    amp = np.zeros([spike_list.shape[1], spike_list.shape[0]])

    np.array(h5["Data/Recording_0/TimeStampStream/Stream_0/InfoTimeStamp"])["Label"]
    np.array(h5["Data/Recording_0/TimeStampStream/Stream_0/InfoTimeStamp"])["Label"]
    return spike_list, amp, rec_dur, SaRa

def import_data(ui):
    from os import listdir
    from os.path import isfile, join
    from os import walk
    global filepath
    global main_ui
    main_ui = ui
    global data
    if ui.d_tab_checkbox.isChecked():
        listOfFiles = getListOfFiles(filepath)
        data = listOfFiles
        ui.MainTextBrowser.setText("Alle Dateien:")
        for i in listOfFiles:
            ui.MainTextBrowser.append(i)

    else:
        data.append(filepath)
    print(filepath)
    ui.d_tab_checkbox.setEnabled(False)
    ui.MainTextBrowser.setText(filepath)

def import_data_old(ui):
    global extension
    global filepath
    global files
    if ui.d_tab_checkbox.isChecked():
        all_directories = [x[0] for x in os.walk(filepath)]
        for i in all_directories:
            mat_file = glob.glob(os.path.join(i, "*.mat"))
            if mat_file != []:
                files.append(mat_file)
        ui.MainTextBrowser.setText("Folgende Datein wurden erkannt:")
        ui.MainTextBrowser.setText("hello")
        ui.MainTextBrowser.append("hello")

    else:
        if extension == ".bxr":
            import_bxr()
        elif extension == ".mat":
            import_mat()
        elif extension == ".dat":
            import_dat()
        elif extension == ".py":
            print("It's a .py")
        else:
            print("Sorry Datei kann nicht geöffnet werden :(")
    print(filepath)
    ui.d_tab_checkbox.setEnabled(False)
    ui.MainTextBrowser.setText(filepath)


class ReadBxr:
    def __init__(self, path):
        self.data = h5py.File(path, 'r')

        self.sf = self.data['3BRecInfo/3BRecVars/SamplingRate'][()][0]
        self.recLenght = self.data['3BRecInfo/3BRecVars/NRecFrames'][0] / self.sf


def get_spiketimes(file, typeTs='s'):
    spkTime = np.array(file.data['3BResults/3BChEvents/SpikeTimes'])
    spkCh = np.array(file.data['3BResults/3BChEvents/SpikeChIDs'])

    if typeTs == 's':
        return spkCh, spkTime / file.sf
    elif typeTs == 'frame':
        return spkCh, spkTime


def convert_to_elephant_array_bxr(file):
    ch, ts = get_spiketimes(file)
    # array = np.zeros([ch.max() + 1, round(ts.shape[0]/ch.max())])  # 14036
    array = np.zeros([ch.max() + 1, ch.shape[0]])
    y = 0
    k = 0
    for i in ch:
        while float(array[i, k]) != 0:
            k += 1
        array[i, k] = ts[y]
        y = y + 1
        k = 0
    return array



