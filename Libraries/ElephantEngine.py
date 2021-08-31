from elephant.spike_train_synchrony import spike_contrast as elephant_spike_contrast
from neo.core import SpikeTrain
import numpy as np
import quantities as pq
from Libraries.Import import get_variables

elephant_feauture_list = ["Spike-Contrast", "another"]
main_ui = object


def elephant_calc_feature(ui):
    global main_ui
    main_ui = ui
    feature = ui.sta_tab_elephant_tab_feature_comboBox.currentText()
    ui.MainTextBrowser.append(str(feature) + ": ")
    feature_value = elephant_all_features(feature)
    ui.MainTextBrowser.append(
        "Mean: " + str(round(feature_value, 4)))


def elephant_calc_all_feature(ui):
    global main_ui
    main_ui = ui
    feature = ui.sta_tab_elephant_tab_feature_comboBox.currentText()
    for i in elephant_feauture_list:
        ui.MainTextBrowser.append(str(i) + ": ")
        feature_value = elephant_all_features(i)
        ui.MainTextBrowser.append("Mean: " + str(round(feature_value, 4)))



def elephant_all_features(feature):
    spike_list, amp, rec_dur, SaRa = get_variables()
    spike_list = convert_to_spiketrain(spike_list)
    if feature == "Spike-Contrast":
        value = elephant_spike_contrast(spike_list)
    elif feature == "another":
        value = 2
    return value


def convert_to_spiketrain(data):
    spikes = []
    for i in range(0, data.shape[0]):
        train = data[i]
        train = np.trim_zeros(train)
        train = SpikeTrain(train*pq.s, t_stop=np.amax(data[i]))
        spikes.append(train)
    return spikes
