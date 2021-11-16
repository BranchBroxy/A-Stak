from Libraries.Import import get_variables
from Libraries.AStakAlgo import testAlgo

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

def astak_calc_feature(ui):
    global main_ui
    global CMres_TSPE, DMres_TSPE, CM_exh_TSPE, CM_inh_TSPE
    main_ui = ui
    feature = ui.sta_tab_astak_tab_feature_comboBox.currentText()
    spike_list, amp, rec_dur, SaRa = get_variables()
    if feature == "TSPE":
        CMres_TSPE, DMres_TSPE, CM_exh_TSPE, CM_inh_TSPE = TSPE(spike_list, rec_dur)

    if feature == "testAlgo":
        testVektor = testAlgo(spike_list, rec_dur)



def astak_calc_all_feature(ui):
    pass