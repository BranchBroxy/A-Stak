from Libraries.Import import get_variables
from Libraries.AStakAlgo import testAlgo
from Libraries.Import import get_data_list, import_dat, import_mat, import_bxr, import_h5

import numpy as np
import os

from Libraries.AStakAlgo.TSPE import TSPE
import matplotlib.pyplot as plt

astak_feauture_list = ["TSPE", "another", "testAlgo"]
main_ui = object
global CMres_TSPE, DMres_TSPE, CM_exh_TSPE, CM_inh_TSPE

global testVektor

def get_astak_variables():
    return CMres_TSPE, DMres_TSPE, CM_exh_TSPE, CM_inh_TSPE

def astak_calc_feature_old(ui):
    global main_ui
    global CMres_TSPE, DMres_TSPE, CM_exh_TSPE, CM_inh_TSPE
    main_ui = ui
    feature = ui.sta_tab_astak_tab_feature_comboBox.currentText()
    spike_list, amp, rec_dur, SaRa = get_variables()
    if feature == "TSPE":
        CMres_TSPE, DMres_TSPE, CM_exh_TSPE, CM_inh_TSPE = TSPE(spike_list, rec_dur)

    if feature == "testAlgo":
        testVektor = testAlgo(spike_list, rec_dur)

def astak_calc_feature(ui):
    global main_ui
    global feature_mean, feature_values, feature_std, feature_pref, feature_label
    main_ui = ui
    feature = ui.sta_tab_astak_tab_feature_comboBox.currentText()

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

        if feature == "TSPE":
            value = TSPE(spike_list, rec_dur)
        elif feature == "another":
            value = 2

    print("Done")




def astak_calc_all_feature(ui):
    pass