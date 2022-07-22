"""
Python 3.7 wird benötigt um die MatLabEngine installieren zu können
und eine aktuelle Version von MatLab muss auf dem Rechner installiert sein.
(https://de.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)
dann im terminal:
cd matlabroot/extern/engines/python
python setup.py install

My Path: /usr/local/MATLAB/R2021a/extern/engines/python
"""


import matlab.engine # funktioniert nur mit matlab 3.7/8
from Libraries.Import import get_data_list, import_dat, import_mat, import_bxr, import_h5
#from Libraries.GUI_handler import get_matlab_drcell_path
import numpy as np
import os
from Libraries.Export import append_data_to_csv

import matplotlib.pyplot as plt


main_ui = object
# drcell_path_var = ""
# matlab_path_var = ""
global feature_mean, feature_values, feature_std, feature_allEl, feature_pref, feature_label



def get_matlab_variables():
    return feature_mean, feature_values, feature_std, feature_pref, feature_label

def matlab_calc_feature(ui, all_flag):
    global main_ui
    global feature_mean, feature_values, feature_std, feature_pref, feature_label
    main_ui = ui
    feature = ui.sta_tab_matlab_tab_feature_comboBox.currentText()

    # spike_list, amp, rec_dur, SaRa = get_variables()

    data = get_data_list()
    for path in data:
        name, extension = os.path.splitext(path)
        if extension == ".bxr":
            spike_list, amp, rec_dur, SaRa = import_bxr()
        elif extension == ".mat":
            spike_list, amp, rec_dur, SaRa = import_mat(path)
        elif extension == ".dat":
            spike_list, amp, rec_dur, SaRa = import_dat()
        elif extension == ".h5":
            spike_list, amp, rec_dur, SaRa = import_h5(path)
        elif extension == ".py":
            print("It's a .py")
        else:
            print("Sorry Datei kann nicht geöffnet werden :(")


        feature_value = matlab_all_feature(TS=spike_list, AMP=amp, rec_dur=rec_dur, SaRa=SaRa,
                                           Selection=feature, time_win=rec_dur, FR_min=0)
        if feature == "Connectivity_TSPE" or feature == "Connectivity_TSPE_withSurrogateThreshold" or feature == "Connectivity_TSPE_70percent":
            feature_mean = feature_value[0][0]
            feature_std = feature_value[1][0]
            feature_values = feature_value[2][0]
            feature_pref = feature_value[3][0]
            feature_label = feature_value[4][0]

        else:
            feature_mean = feature_value[0][0]
            feature_std = feature_value[1][0]
            feature_values = feature_value[2][0]
            feature_pref = feature_value[3][0]
            feature_label = feature_value[4][0]


        ui.MainTextBrowser.append(str(feature) + ": ")
        try:
            ui.MainTextBrowser.append("Mean: " + str(round(feature_mean, 4)) + ", Values: " + str(
                round(feature_values, 4)) + ", Std: " + str(round(feature_std, 4)) + ", allEl: " + str(
                round(feature_label, 4)))

        except:
            ui.MainTextBrowser.append(
                "Mean: " + str(round(feature_mean, 4)) + ", Std: " + str(round(feature_std, 4)))
        if feature == "Connectivity_TSPE":
            feature_mean = feature_value[0][0]
            feature_std = feature_value[1][0]
            feature_values = feature_value[2][0]
            feature_pref = feature_value[3][0]
            feature_label = feature_value[4][0]
            from Plots.TSPE_plot import plot_CM

            TSPE_path = os.path.basename(path)
            TSPE_filename, TSPE_file_extension = os.path.splitext(TSPE_path)

            plot_CM(np.array(feature_values), path="/mnt/HDD/Data/CM/" + "CM_" + TSPE_filename)
    print("Done")



def matlab_calc_all_feature(ui):
    global main_ui
    main_ui = ui
    data = get_data_list()
    for path in data:
        name, extension = os.path.splitext(path)
        if extension == ".bxr":
            spike_list, amp, rec_dur, SaRa = import_bxr()
        elif extension == ".mat":
            spike_list, amp, rec_dur, SaRa = import_mat(path)
        elif extension == ".dat":
            spike_list, amp, rec_dur, SaRa = import_dat()
        elif extension == ".h5":
            spike_list, amp, rec_dur, SaRa = import_h5(path)
        elif extension == ".py":
            print("It's a .py")
        else:
            print("Sorry Datei kann nicht geöffnet werden :(")

        for feature in matlab_feautre_list_french_data:
            try:
                print(f"Calculating {feature}")
                feature_value = matlab_all_feature(TS=spike_list, AMP=amp, rec_dur=rec_dur, SaRa=SaRa,
                                                   Selection=feature, time_win=rec_dur, FR_min=0)
                if feature == "Connectivity_TSPE" or feature == "Connectivity_TSPE_withSurrogateThreshold" or feature == "Connectivity_TSPE_70percent":
                    feature_mean = feature_value[0][0]
                    feature_std = feature_value[1][0]
                    feature_values = feature_value[2][0]
                    feature_pref = feature_value[3][0]
                    feature_label = feature_value[4][0]
                else:
                    feature_mean = feature_value[0][0]
                    feature_std = feature_value[1][0]
                    feature_values = feature_value[2][0]
                    feature_pref = feature_value[3][0]
                    feature_label = feature_value[4][0]


                ui.MainTextBrowser.append(str(feature) + ": ")

                try:
                    ui.MainTextBrowser.append("Mean: " + str(round(feature_mean, 4)) + ", Values: " + str(
                        round(feature_values, 4)) + ", Std: " + str(round(feature_std, 4)) + ", allEl: " + str(
                        round(feature_label, 4)))

                except:
                    ui.MainTextBrowser.append(
                        "Mean: " + str(round(feature_mean, 4)) + ", Std: " + str(round(feature_std, 4)))
            except:
                print(f"Calculating {feature} failed")
                feature_mean = "failed"
                feature_std = "failed"
                feature_values = "failed"
                feature_pref = "failed"
                feature_label = "failed"

            if feature == "Connectivity_TSPE":
                feature_mean = feature_value[0][0]
                feature_std = feature_value[1][0]
                feature_values = feature_value[2][0]
                feature_pref = feature_value[3][0]
                feature_label = feature_value[4][0]
                from Plots.TSPE_plot import plot_CM

                TSPE_path = os.path.basename(path)
                TSPE_filename, TSPE_file_extension = os.path.splitext(TSPE_path)

                plot_CM(np.array(feature_values), path= "/mnt/HDD/Data/CM/" + "CM_" + TSPE_filename)
            append_data_to_csv(feature, feature_mean, feature_std, feature_values, feature_pref, feature_label, path,
                               "/mnt/HDD/Data/Feature.csv")
            print("Done Writing Feature")


        print("Automatische Berechnung der Feature")

def matlab_calc_all_feature_return(spike_list, amp, rec_dur, SaRa):
    #spike_list, amp, rec_dur, SaRa = get_variables()
    feature_mean = []
    feature_std = []
    feature_values = []
    feature_pref = []
    feature_label = []
    for i in matlab_feautre_list:
        feature_value = matlab_all_feature(TS=spike_list, AMP=amp, rec_dur=rec_dur, SaRa=SaRa,
                                           Selection=i, time_win=rec_dur, FR_min=6)
        feature_mean.append(feature_value[0])
        feature_std.append(feature_value[1])
        feature_values.append(feature_value[2])
        feature_pref.append(feature_value[3])
        feature_label.append(feature_value[4])

    return feature_mean, feature_std, feature_values, feature_pref, feature_label

def print_feature(mean, std):
    global main_ui
    ui = main_ui
    ui.MainTextBrowser.append(
        "Mean: " + str(round(mean, 4)) + ", Std: " + str(round(std, 4)))

def matlab_all_feature(TS, AMP, rec_dur, SaRa, Selection, time_win, FR_min, N=0, binSize=0):

    #drcell_path, matlab_path = get_matlab_drcell_path()
    drcell_path, matlab_path = "", ""
    TS = np.transpose(TS)
    TS = matlab.double(TS.tolist())
    # TS = matlab.double(TS)
    AMP = matlab.double(AMP.tolist())
    # AMP = matlab.double(AMP)
    # TODO: path variable von Benutzer eingeben lassen
    """path = os.getcwd()
    path = os.path.dirname(os.path.dirname(path))
    path = path + "/DrCell"""
    drcell_path = "/mnt/HDD/Programmieren/Python/A-Stak/DrCell"
    # rec_dur = matlab.double(rec_dur)
    values = []
    # path_manuell = '/media/broxy/38DA-A148/FauBox/Uni/Master/PyCharm/Astak_V1/DrCell'
    path_manuell_python = drcell_path + '/shared/Engines/Python'
    eng = matlab.engine.start_matlab()  # MatLab Umgebung aufrufen
    eng.cd(path_manuell_python)

    mdic = {"TS": TS,
            "AMP": AMP,
            "rec_dur": rec_dur,
            "SaRa": SaRa,
            "Selection": Selection,
            "time_win": time_win,
            "FR_min": FR_min,
            "binSize": binSize
            }

    mat_file_path = os.path.abspath(os.getcwd()) + "/temp/temp.mat"

    from scipy.io import savemat
    savemat(mat_file_path, mdic)

    # eng.get_path(path_manuell, nargout=0)
    # eng.cd(path)  # nach Spike-Contrast navigieren
    # values = eng.CalcFeatures_call(TS, AMP, float(rec_dur), float(SaRa), Selection, float(time_win), float(FR_min), float(0), float(0))
    rec_dur_mat = float(int(rec_dur) + 1)
    time_win_mat = float(int(time_win) + 1)

    values = eng.adapter_python(drcell_path, mat_file_path)

    eng.quit()
    return values
    # eng.adapter(TS, AMP, rec_dur, SaRa, Selection, time_win, FR_min, N, binSize)

def matlab_first_call():
    # @TODO MatLab first_call nutzen, sobald eng.quit() ausgeführt wird ist auch der Pfad weg -> Lösung finden
    path = os.getcwd()
    path = os.path.dirname(os.path.dirname(path))
    path = path + "/DrCell"
    path_manuell = '/media/broxy/38DA-A148/FauBox/Uni/Master/PyCharm/Astak_V1/DrCell'
    path_manuell_python = path_manuell + '/shared/Engines/Python'

    print(path_manuell)
    print(path_manuell_python)
    eng = matlab.engine.start_matlab()  # MatLab Umgebung aufrufen
    # path_manuell = matlab.char(path_manuell)
    eng.cd(path_manuell_python)  # nach Spike-Contrast navigieren
    eng.get_path(path_manuell, nargout=0)
    eng.quit()


matlab_feautre_list = ['Spikerate',
'Number of spikes',
'Amplitude',
'ActiveElectrodes',
'BR_baker100',
'BD_baker100',
'SIB_baker100',
'IBI_baker100',
'BR_baker200',
'BD_baker200',
'SIB_baker200',
'IBI_baker200',
'BR_selinger',
'BD_selinger',
'SIB_selinger',
'IBI_selinger',
'NBR_chiappalone',
'NBD_chiappalone',
'SINB_chiappalone',
'INBI_chiappalone',
'NBR_jimbo',
'NBD_jimbo',
'SINB_jimbo',
'INBI_jimbo',
'NBR_MC',
'NBD_MC',
'SINB_MC',
'INBI_MC',
'Sync_CC_selinger',
'Sync_STTC',
'Sync_MI1',
'Sync_MI2',
'Sync_PS',
'Sync_PS_M',
'Sync_Contrast',
'Sync_Contrast_fixed',
'Sync_ISIDistance',
'Sync_SpikeDistance',
'Sync_SpikeSynchronization',
'Sync_ASpikeSynchronization',
'Sync_AISIDistance',
'Sync_ASpikeDistance',
'Sync_RISpikeDistance',
'Sync_RIASpikeDistance',
'Sync_EarthMoversDistance',
'Connectivity_TSPE',
'Connectivity_TSPE_70percent',
'Connectivity_TSPE_withSurrogateThreshold',
'Entropy_bin100',
'Entropy_capurro']

matlab_feautre_list_fixed = ['Spikerate',
'Number of spikes',
'Amplitude',
'ActiveElectrodes',
'BR_baker100',
'BD_baker100',
'SIB_baker100',
'IBI_baker100',
'BR_baker200',
'BD_baker200',
'SIB_baker200',
'IBI_baker200',
'BR_selinger',
'BD_selinger',
'SIB_selinger',
'IBI_selinger',
'NBR_chiappalone',
'NBD_chiappalone',
'SINB_chiappalone',
'INBI_chiappalone',
# jimbo missing
'NBR_MC',
'NBD_MC',
'SINB_MC',
'INBI_MC',
#'Sync_CC_selinger',
'Sync_STTC',
# 'Sync_MI1',
# 'Sync_MI2',
'Sync_PS',
'Sync_PS_M',
'Sync_Contrast',
'Sync_Contrast_fixed',
'Sync_ISIDistance',
'Sync_SpikeDistance',
'Sync_SpikeSynchronization',
'Sync_ASpikeSynchronization',
'Sync_AISIDistance',
'Sync_ASpikeDistance',
'Sync_RISpikeDistance',
'Sync_RIASpikeDistance',
'Sync_EarthMoversDistance',
'Connectivity_TSPE',

'Entropy_bin100',
'Entropy_capurro']

small_matlab_feautre_list = [
'Spikerate',
'Number of spikes',
'Amplitude',
'ActiveElectrodes',
'BR_baker100',
'Sync_Contrast',
'Entropy_bin100',
'Entropy_capurro',
'Sync_AISIDistance',
'BD_baker100']

small_matlab_feautre_list_ = [
'Spikerate',
'Sync_Contrast',
'Number of spikes']

matlab_feautre_list_ = ['Spikerate',
'Number of spikes',
'Amplitude',
'ActiveElectrodes',
'Sync_CC_selinger',
'Sync_STTC',
'Sync_MI1',
'Sync_MI2',
'Sync_PS',
'Sync_PS_M',
'Sync_Contrast',
'Sync_ISIDistance',
'Sync_SpikeDistance',
'Sync_SpikeSynchronization',
'Sync_ASpikeSynchronization',
'Sync_AISIDistance',
'Sync_ASpikeDistance',
'Sync_RISpikeDistance',
'Sync_RIASpikeDistance',
'Sync_EarthMoversDistance',
'Connectivity_TSPE']

matlab_feautre_list_french_data = [
'Spikerate',
'Number of spikes',
'Amplitude',
'ActiveElectrodes',
'Sync_CC_selinger',
'Sync_STTC',
'Sync_MI1',
'Sync_MI2',
'Sync_PS',
'Sync_PS_M',
'Sync_Contrast',
'Sync_Contrast_fixed',
'Sync_ISIDistance',
'Sync_SpikeDistance',
'Sync_SpikeSynchronization',
'Sync_ASpikeSynchronization',
'Sync_AISIDistance',
'Sync_ASpikeDistance',
'Sync_RISpikeDistance',
'Sync_RIASpikeDistance',
'Sync_EarthMoversDistance',
'Connectivity_TSPE']