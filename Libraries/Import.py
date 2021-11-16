import numpy as np
import h5py  # hdf5
import scipy.io
import os
from PyQt5.QtWidgets import QFileDialog
import math

filepath = ""
name = ""
main_ui = object
extension = ""


spike_list = np.zeros(0)
amp = np.zeros(0)
rec_dur = 0
SaRa = 0


def get_variables():
    global spike_list
    global amp
    global rec_dur
    global SaRa
    return spike_list, amp, rec_dur, SaRa


def get_filepath(ui):
    global name
    global filepath
    global extension
    global main_ui
    main_ui = ui
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


def import_mat():
    global main_ui
    global filepath

    ui = main_ui

    global spike_list
    global amp
    global rec_dur
    global SaRa

    path = filepath
    mat_data = scipy.io.loadmat(path)
    try:
        spike_list = np.transpose(mat_data["SPIKEZ"]["TS"][0, 0])
        spike_list = np.where(np.invert(np.isnan(spike_list)), spike_list, 0)
        amp = np.zeros([spike_list.shape[1], spike_list.shape[0]])
        rec_dur = float(mat_data["SPIKEZ"][0, 0]["PREF"][0, 0]["rec_dur"][0])
        SaRa = mat_data["SPIKEZ"][0, 0]["PREF"][0, 0]["SaRa"][0][0]
        flag_mat_v1 = True
        print("Mat Datei erfolgreich importiert")
        ui.MainTextBrowser.setText("Mat Datei erfolgreich importiert")
    except:
        try:
            spike_list = np.transpose(mat_data["temp"]["SPIKEZ"][0, 0]["TS"][0, 0])
            amp = mat_data["temp"]["SPIKEZ"][0, 0]["AMP"][0, 0]
            rec_dur = mat_data["temp"]["SPIKEZ"][0, 0]["PREF"][0,0]["rec_dur"][0, 0][0][0]
            SaRa = mat_data["temp"]["SPIKEZ"][0, 0]["PREF"][0, 0]["SaRa"][0, 0][0][0]
            flat_mat_v2 = True
            print("Mat Datei erfolgreich importiert")
            ui.MainTextBrowser.setText("Mat Datei erfolgreich importiert")
        except:
            print("Mat Datei konnte nicht importiert werden")
            ui.MainTextBrowser.setText("Mat Datei konnte nicht erfolgreich importiert werden")

    #print(Import.amp)



def import_data():
    global extension
    if extension == ".bxr":
        import_bxr()
    elif extension == ".mat":
        import_mat()
    elif extension == ".py":
        print("It's a .py")
    else:
        print("Sorry Datei kann nicht geöffnet werden :(")



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