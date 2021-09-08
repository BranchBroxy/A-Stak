from Libraries.Import import get_variables
from Libraries.AStakAlgo.TSPE import TSPE
import numpy as np
import os

from Libraries.AStakAlgo.TSPE import TSPE
import matplotlib.pyplot as plt

astak_feauture_list = ["TSPE", "another"]
main_ui = object



def astak_calc_feature(ui):
    global main_ui
    main_ui = ui
    feature = ui.sta_tab_astak_tab_feature_comboBox.currentText()
    spike_list, amp, rec_dur, SaRa = get_variables()
    if feature == "TSPE":
        CMres, DMres, CM_exh, CM_inh = TSPE(spike_list, rec_dur)
        plt.imshow(CMres, cmap='Blues', interpolation='nearest')
        plt.show()


def astak_calc_all_feature(ui):
    pass