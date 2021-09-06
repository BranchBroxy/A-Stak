import numpy as np
import h5py  # hdf5
import scipy.io
import os
from PyQt5.QtWidgets import QFileDialog
import math
from scipy.sparse import csr_matrix

filepath = ""
name = ""
main_ui = object
extension = ""


spike_list = np.zeros(0)
amp = np.zeros(0)
rec_dur = 0
SaRa = 0


def import_mat():
    global main_ui
    global filepath

    ui = main_ui

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


import_mat()
# print(spike_list)
Recordingdur_ms=60*1000*30 # Recording duration for connectivity estimation
Plotdur_ms=10*1000 # Duration for raster plot
NumEl = 100
pos_wins=np.array([2, 3, 4, 5, 6])
# co_wins=np.array([0,0])
co_wins=0
neg_wins=np.array([3, 4, 5, 6, 7, 8])
d=25
FLAG_NORM=0


print("here")
sdf=spike_list
sdf = sdf * 1000
sdf = sdf.astype(int)

anzahl_elektroden = int(sdf.shape[0]) # 60
anzahl_einträge = int(sdf.shape[1]*1000) # in ms
rec_dur_in_ms = rec_dur * 1000
all = anzahl_elektroden * anzahl_einträge
sdf_new = np.zeros(shape=(anzahl_elektroden,anzahl_einträge))
NrC = anzahl_elektroden
NrS = rec_dur_in_ms # in ms

#################################
# Generation of "sparse" Matrix #
#################################

print("Generation of sparse Matrix")
index = 0
for y in range(0, anzahl_elektroden):
    index = 0
    for i in sdf[y]:
        if i != 0:
            sdf_new[y][index] = i
        else:
            pass
        index = index + 1

spikes1 = []
spikes2 = []
for a in range(0, anzahl_elektroden):
    train = np.trim_zeros(sdf_new[a]).tolist()
    if train != []:
        spikes1.append(train)
        spikes2.append(len(train)*[a]) # Wenn Elektroden wie in Matlab bei 1 Anfangen soll muss hier a+1 -> dann müssen aber noch mehr Änderung am Code durchführt werden
vec1= np.array(spikes1, dtype=object)
vec2= np.array(spikes2, dtype=object)


vec1 = [1,1.1,2,3,4,4.9,0.5,0.6,1,4,4.9,1,2,3,4,4.5]

vec2 = [0,0,0,0,0,0,1,1,1,1,1,2,2,2,2,2]
vec1= np.array(vec1, dtype=object)
vec1 = vec1 * 1000
vec2= np.array(vec2, dtype=object)
NrC = 3
NrS = 5000
anzahl_elektroden = NrC
rec_dur_in_ms = NrS

np.max(sdf) # 59598
mat = np.zeros(shape=(NrS, NrC))
n_spikes = 0
n_spikes_einer_elektrode = np.zeros(shape=(1, anzahl_elektroden))

for i in range(0, vec1.shape[0]):
    if vec1[i] != 0: # vec1[0,i] same as vec2[0][i]
        mat[int(vec1[i])][int(vec2[i])] = 1
mat_new = csr_matrix(mat)


################################################
# Calculation of std deviation and mean values #
################################################

print("Calculation of std deviation and mean values")
l = np.ones(shape=(anzahl_elektroden, NrS))
# n_spikes_einer_elektrode entspricht in matlab l * mat
u_mean = n_spikes_einer_elektrode / NrS
# u_0 = 60 * [u_mean]
u_0 = mat - u_mean
# r=np.std(u_0)
r = np.zeros(shape=(1, anzahl_elektroden))
for i in range(0, anzahl_elektroden):
    r_temp = np.std(u_0[:,i])
    r[0, i] = r_temp


##########################
# Fast Cross-Correlation #
##########################
print("Fast Cross-Correlation")
ran = np.array([range(1 - np.max(neg_wins) - np.max(co_wins), np.max(neg_wins) + d+1)])
CM=np.zeros(shape=(int(ran.shape[1]), NrC, NrC))
CM_matlab = np.zeros(shape=(NrC, int(ran.shape[1]), NrC))
ind = np.max(neg_wins) + np.max(co_wins)
if ind <= -1:
    ind=0
# for python:
ind = ind - 1
for i in range(0, d+np.max(neg_wins)+1):
    CMbuffer = np.divide((np.dot(np.transpose(mat[i:mat.shape[0], :]), mat[0:mat.shape[0] - i, :])), (np.dot(np.transpose(r), r))) / NrS
    CM[i] = CMbuffer
    for counter_1 in range(0, NrC):
        CM_matlab[counter_1, ind, :] = CMbuffer[counter_1]
    ind = ind + 1

# Usage of symmetric construction of cross correlation for faster calculation:
# helping = np.max(neg_wins)+np.max(co_wins)-1
# @TODO potenzieller Bug!!, weil 0 harcodede in helper
helping = np.max(neg_wins)+np.max(co_wins)
helper = np.arange(helping)
helper = helper[helping:0:-1]
helper = np.append(helper, 1)


if(np.max(neg_wins)+np.max(co_wins) > 0):
    bufCM = np.zeros(shape=(NrC, NrC))
    ind = 0
    for j in helper:
        bufCM = CM[np.max(neg_wins) + np.max(co_wins) + j-1, :, :]
        # bufCM = CMbuffer
        CM[ind] = np.transpose(bufCM)
        ind = ind + 1

print("stop")
# Additional scaling for reduction of network burst impacts:
# not finished!!!!!
if FLAG_NORM:
    s = np.zeros(shape=(ran.shape[1], 1))
    for i in range(0, ran.shape[0]):
        zwi = CM[i, np.diag(np.ones(shape=(NrC, 1)))]
        s[i] = np.sum(np.sum(zwi(~ np.isnan(CM[i, ~ np.diag(np.ones((NrC, 1)))]))))


##############################
# Generation of edge filters #
##############################
print("Generation of edge filters")
WB=np.max(neg_wins)+np.max(co_wins)
# sumWin=np.zeros(shape=(d+WB, NrC, NrC))
sumWin=np.zeros(shape=(NrC, d+WB, NrC))
in_=-1
temp_in_=30
# @TODO: win_inner- und beginnigsgröße nicht hardcoden
win_inner = np.zeros(shape=(1, 30))
beginnings = np.zeros(shape=(1, 30))
windows = []
windows = [[] for temp_in_ in range(temp_in_)]

for win_before in neg_wins:
    # for win_p1 in range(0, co_wins):
    win_p1 = co_wins
    for win_in in pos_wins:
        in_=in_+1
        win_p2 = win_p1
        win_after=win_before
        windows[in_].append([-1*np.ones(shape=(win_before, 1)) / win_before])
        if win_p1 != 0: # @TODO: potenzieller Bug
            windows[in_].append([1*np.zeros(shape=(win_p1, 1))])
        windows[in_].append([2/win_in * np.ones(shape=(win_in, 1))])
        if win_p2 != 0: # @TODO: potenzieller Bug
            windows[in_].append([np.zeros(shape=(win_p2, 1))])
        windows[in_].append([-1*np.ones(shape=(win_after, 1)) / win_after])
        # windows[in_]=-1*np.ones(win_before,1) /win_before; np.zeros(win_p1,1);2/win_in* np.ones(win_in,1);np.zeros(win_p2,1);-1*np.ones(win_after,1)/win_after
        beginnings[0, in_]=int(1+WB-win_before-win_p1)
        win_inner[0, in_]=win_in
wnew_windows = [[] for temp_in_ in range(temp_in_)]
var1 = []

for runner in range(0, len(windows)):
    for u in range(len(windows[runner])):
        for t in range(len(windows[runner][u])):
            for r in range(len(windows[runner][u][t])):
                wnew_windows[runner].append(float(windows[runner][u][t][r]))
m = d + np.max(neg_wins) + np.max(co_wins) + np.max(pos_wins)

#########################
# Usage of edge filters #
#########################
print("Usage of edge filters")
# Matlab end -> .shape[0] python
from scipy import signal
# f = signal.fftconvolve(x, y)
# CM(np.isnan(CM))=0
np.nan_to_num(x=CM,copy=False, nan = 0) # if CM contains many NaNs, only NaNs remains after convolution. e.g. for very short spike trains

conv_flag = True
# @TODO buffer.arrays, Größe darf nicht gehard codet sein

# z1buff = np.zeros(shape=(NrC, 29, NrC))
# CM4buff = np.zeros(shape=(NrC, 30, NrC))
for j in range(0, in_+1):
    z1_flag = True
    cm4_flag = True
    for page in range(0, NrC):
        for reihe in range(0, NrC):
            z1 = signal.fftconvolve(CM_matlab[page, int(beginnings[0][j]) - 1: CM_matlab.shape[1], reihe], wnew_windows[j], 'valid')
            if z1_flag:
                z1_flag = False
                z1buff = np.zeros(shape=(NrC, z1.shape[0], NrC))
            # signal.fftconvolve(CM_matlab[0, 5:41, 2], wnew_windows[j], 'valid')
            z1buff[page, :, reihe] = z1
    z1 = z1buff
    z1 = np.around(z1, decimals=4)
    z2 = np.ones(shape=(int(win_inner[0][j]), 1))
    for page in range(0, NrC):
        for reihe in range(0, NrC):
            CM4 = signal.fftconvolve(z1[page, :, reihe] , z2[:,0], 'full')
            if cm4_flag:
                cm4_flag = False
                CM4buff = np.zeros(shape=(NrC, CM4.shape[0], NrC))
            CM4buff[page, :, reihe] = CM4

    CM4 = CM4buff
    m = np.min([m, CM4[1, :, 1].shape[0]])
    # @TODO: für was diese Zeile?: sumWin[0:CM4.shape[1],:,:]=CM4+sumWin[1:CM4.shape[1],:,:]
    sumWin[:, 0:CM4.shape[1], :] = CM4+sumWin[:, 0:CM4.shape[1], :]


sumWin=sumWin[0:m,:,:]
print("sucsess!")
