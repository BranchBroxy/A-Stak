"""
Python 3.7 wird benötigt um die MatLabEngine installieren zu können
und eine aktuelle Version von MatLab muss auf dem Rechner installiert sein.
(https://de.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)
dann im terminal:
cd matlabroot/extern/engines/python
python setup.py install

My Path: /usr/local/MATLAB/R2021a/extern/engines/python
"""


import matlab.engine # funktioniert nur mit matlab 3.7
from Libraries.Import import get_variables
import numpy as np
import os

import matplotlib.pyplot as plt

main_ui = object


def matlab_calc_feature(ui):
    global main_ui
    main_ui = ui
    feature = ui.sta_tab_matlab_tab_feature_comboBox.currentText()
    spike_list, amp, rec_dur, SaRa = get_variables()
    feature_value = matlab_all_feature(TS=spike_list, AMP=amp, rec_dur=rec_dur, SaRa=SaRa,
                                       Selection=feature, time_win=rec_dur, FR_min=0)
    feature_mean = feature_value[0]
    feature_values = feature_value[1]
    feature_std = feature_value[2]
    feature_allEl = feature_value[3]
    ui.MainTextBrowser.append(str(feature) + ": ")
    try:
        ui.MainTextBrowser.append("Mean: " + str(round(feature_mean, 4)) + ", Values: " + str(
            round(feature_values, 4)) + ", Std: " + str(round(feature_std, 4)) + ", allEl: " + str(
            round(feature_allEl, 4)))

    except:
        ui.MainTextBrowser.append(
            "Mean: " + str(round(feature_mean, 4)) + ", Std: " + str(round(feature_std, 4)))

    plt.imshow(feature_values, cmap='Blues', interpolation='nearest')
    plt.show()

def matlab_calc_all_feature(ui):
    global main_ui
    main_ui = ui
    spike_list, amp, rec_dur, SaRa = get_variables()
    for i in matlab_feautre_list:
        feature_value = matlab_all_feature(TS=spike_list, AMP=amp, rec_dur=rec_dur, SaRa=SaRa,
                                           Selection=i, time_win=rec_dur, FR_min=0)
        feature_mean = feature_value[0]
        feature_values = feature_value[1]
        feature_std = feature_value[2]
        feature_allEl = feature_value[3]
        print_feature(feature_mean, feature_std)

def print_feature(mean, std):
    global main_ui
    ui = main_ui
    ui.MainTextBrowser.append(
        "Mean: " + str(round(mean, 4)) + ", Std: " + str(round(std, 4)))

def matlab_all_feature(TS, AMP, rec_dur, SaRa, Selection, time_win, FR_min, N=0, binSize=0):
    TS = np.transpose(TS)
    TS = matlab.double(TS.tolist())
    AMP = matlab.double(AMP.tolist())
    # TODO: path variable von Benutzer eingeben lassen
    """path = os.getcwd()
    path = os.path.dirname(os.path.dirname(path))
    path = path + "/DrCell"""
    path = "/media/broxy/38DA-A148/FauBox/Uni/Master/PyCharm/Astak_V1/DrCell"
    # rec_dur = matlab.double(rec_dur)
    values = []
    path_manuell = '/media/broxy/38DA-A148/FauBox/Uni/Master/PyCharm/Astak_V1/DrCell'
    path_manuell_python = path_manuell + '/shared/Engines/Python'
    eng = matlab.engine.start_matlab()  # MatLab Umgebung aufrufen
    eng.cd(path_manuell_python)  # nach Spike-Contrast navigieren
    eng.get_path(path_manuell, nargout=0)
    eng.cd(path)  # nach Spike-Contrast navigieren
    values = eng.CalcFeatures_call(TS, AMP, float(rec_dur), float(SaRa), Selection, float(time_win), float(FR_min), float(0), float(0))
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
'NBD_jimbo'
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