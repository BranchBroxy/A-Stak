import numpy as np
import scipy.io
from Libraries.AStakAlgo.TSPE import TSPE
import matplotlib.pyplot as plt

spike_list = np.zeros(0)
amp = np.zeros(0)
rec_dur = 0
SaRa = 0

def import_mat():
    global main_ui
    global filepath



    global spike_list
    global amp
    global rec_dur
    global SaRa

    path = "/home/broxy/Dokumente/Messung31.03.2019_09-27-30_TS.mat"
    mat_data = scipy.io.loadmat(path)
    try:
        spike_list = np.transpose(mat_data["SPIKEZ"]["TS"][0, 0])
        spike_list = np.where(np.invert(np.isnan(spike_list)), spike_list, 0)
        amp = np.zeros([spike_list.shape[1], spike_list.shape[0]])
        rec_dur = float(mat_data["SPIKEZ"][0, 0]["PREF"][0, 0]["rec_dur"][0])
        SaRa = mat_data["SPIKEZ"][0, 0]["PREF"][0, 0]["SaRa"][0][0]
        flag_mat_v1 = True
        print("Mat Datei erfolgreich importiert")

    except:
        try:
            spike_list = np.transpose(mat_data["temp"]["SPIKEZ"][0, 0]["TS"][0, 0])
            amp = mat_data["temp"]["SPIKEZ"][0, 0]["AMP"][0, 0]
            rec_dur = mat_data["temp"]["SPIKEZ"][0, 0]["PREF"][0,0]["rec_dur"][0, 0][0][0]
            SaRa = mat_data["temp"]["SPIKEZ"][0, 0]["PREF"][0, 0]["SaRa"][0, 0][0][0]
            flat_mat_v2 = True
            print("Mat Datei erfolgreich importiert")

        except:
            print("Mat Datei konnte nicht importiert werden")
    print("Erfolgreich")

def import_tspe_example():
    global main_ui
    global filepath

    global spike_list
    global amp
    global rec_dur
    global SaRa

    path = "/home/broxy/Downloads/ExampleSpikeTrain.mat"
    mat_data = scipy.io.loadmat(path)
    spikes = np.transpose(mat_data["data"]["TS_ms"][0][0][0])
    record_d = float(mat_data["data"]["recordingtime_ms"])
    spikes_in_ele = np.zeros(shape=(spikes.shape[0], int(record_d)))
    for i in range(0, spikes.shape[0]):
        for y in range(0, spikes[i].shape[1]):
            spikes_in_ele[i, y] = spikes[i][0][y]
    spike_list = spikes_in_ele / 1000
    rec_dur = record_d / 1000
    print("success")


import_mat()
# import_tspe_example()

# plt.eventplot(spike_list, color = "black")
# longest = spike_list.max()
print("Plotting")
# plt.axis([0, longest + 0.05*longest, 0, spike_list.shape[0]])
# plt.set_title('Spike Train Plot')
# plt.show()
print("Done")

CMres, DMres = TSPE(spike_list, rec_dur)
print("Run")
plt.imshow(CMres, cmap='Blues', interpolation='nearest')
plt.show()
