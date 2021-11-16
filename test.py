import numpy as np
import numpy.ma as ma
from scipy import stats
from Libraries.AStakAlgo.TSPE_Treshhold import *
import scipy.io
from scipy import fft, signal
import matplotlib.pyplot as plt

spike_list = np.zeros(0)
amp = np.zeros(0)
rec_dur = 0
SaRa = 0
filepath = "/media/broxy/38DA-A148/FauBox/Uni/Master/Semester_3/5elec.mat"

filepath1 = "/media/broxy/38DA-A148/FauBox/Uni/Master/MatLab/something_1.mat"

def import_mat():
    global main_ui
    global filepath
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
    # print(spike_list)

def autocorr(x):
    x = np.trim_zeros(x, 'b')
    x = x * 1000
    n = x.size
    norm = (x - np.mean(x))
    result = np.correlate(norm, norm, mode='same')
    acorr = result[n//2 + 1:] / (x.var() * np.arange(n-1, n//2, -1))
    lag = np.abs(acorr).argmax() + 1
    r = acorr[lag-1]
    if np.abs(r) > 0.5:
      print('Appears to be autocorrelated with r = {}, lag = {}'. format(r, lag))
    else:
      print('Appears to be not autocorrelated')
    return r, lag

import_mat()
spikes = spike_list[1]
spikes = np.trim_zeros(spikes)
result = np.correlate(spikes, spikes, mode='full')
r, lag  = autocorr(spikes)
print(r, lag)
print(spikes)

from scipy.fft import fft, fftfreq, fftshift
import matplotlib.pyplot as plt
t = spikes
sp = fftshift(fft(spikes))
freq = fftshift(fftfreq(t.shape[-1]))
plt.plot(freq, sp.real, freq, sp.imag)
plt.show()

