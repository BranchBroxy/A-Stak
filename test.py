import numpy as np
import h5py  # hdf5
import scipy.io

path = "/media/broxy/38DA-A148/FauBox/Uni/Master/PyCharm/WrappedUp/Data/Mat/1_TS.mat"
mat_data = scipy.io.loadmat(path)

spike_list = np.transpose(mat_data["SPIKEZ"]["TS"][0, 0])
spike_list = np.where(np.invert(np.isnan(spike_list)), spike_list, 0)
amp = np.zeros([spike_list.shape[1], spike_list.shape[0]])
rec_dur = float(mat_data["SPIKEZ"][0, 0]["PREF"][0, 0]["rec_dur"][0])
SaRa = mat_data["SPIKEZ"][0, 0]["PREF"][0, 0]["SaRa"][0][0]
flag_mat_v1 = True
print("Mat Datei erfolgreich importiert")
