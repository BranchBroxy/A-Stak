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

# sdf_new_trimzeros = sdf_new

spikes1 = []
spikes2 = []
for a in range(0, anzahl_elektroden):
    train = np.trim_zeros(sdf_new[a]).tolist()
    if train != []:
        spikes1.append(train)
        spikes2.append(len(train)*[a]) # Wenn Elektroden wie in Matlab bei 1 Anfangen soll muss hier a+1 -> dann müssen aber noch mehr Änderung am Code durchführt werden
vec1= np.array(spikes1, dtype=object)
vec2= np.array(spikes2, dtype=object)


"""vec1 = np.zeros(shape=(1,all))
# vec2 = np.zeros(shape=(1,sdf.shape[0]*sdf.shape[1]))
# vec2 = np.array()
# temp = np.ones((5,), dtype=int)
# @TODO Nullen raus?
vec1 = np.reshape(sdf_new, newshape=(1, all))
temp0 = np.zeros((anzahl_einträge,), dtype=int)
temp = np.ones((anzahl_einträge,), dtype=int)
for app in range(0, anzahl_elektroden):
    if app == 0:
        vec2 = temp0
    elif app == 1:
        vec2 = np.append(vec2, temp)
    else:
        temp = temp + 1
        vec2 = np.append(vec2, temp)
vec2 = np.reshape(vec2, newshape=(1, all))
vec1[np.abs(vec1)< .1]= 0 # some zeros
vec1 = np.ma.masked_equal(vec1,0)"""
np.max(sdf) # 59598
mat = np.zeros(shape=(rec_dur_in_ms, anzahl_elektroden))
n_spikes = 0
n_spikes_einer_elektrode = np.zeros(shape=(1, anzahl_elektroden))
for x in range(0, len(vec1)):
    # zahler = zahler + 1
    for y in range(0, len(vec1[x])):
        n_spikes_einer_elektrode[0][vec2[x][0]] = len(vec1[x])
        n_spikes = n_spikes + 1


for x in range(0, len(vec1)):
    for y in range(0, len(vec1[x])):
        mat[int(vec1[x][y])][int(vec2[x][y])] = 1

"""for i in range(0, vec1.shape[1]):
    if vec1[0,i] != 0: # vec1[0,i] same as vec2[0][i]
        mat[int(vec2[0,i])][int(vec1[0,i])] = 1"""
mat_new = csr_matrix(mat)
mat_zero = mat[0]

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
CM=np.zeros(shape=(NrC, int(ran.shape[1]), NrC))
ind = np.max(neg_wins) + np.max(co_wins)
if ind <= -1:
    ind=0
# for python:
ind = ind - 1
counter = 0
for i in range(0, d+np.max(neg_wins)+1):

    # CM[ind, :, :] =(np.transpose(mat[1+i:mat.shape[0], :]) * mat[1:mat.shape[0]-i, :]) / ((np.transpose(r)*r)/NrS)
    # CM[ind, :, :] = (np.dot(np.transpose(mat[1 + i:mat.shape[0], :]), mat[1:mat.shape[0] - i, :])) / ((np.dot(np.transpose(r), r)) / NrS)
    # CM[ind, :, :] = (np.dot(np.transpose(mat[i:mat.shape[0], :]), mat[0:mat.shape[0] - i, :])) / (np.dot(np.transpose(r), r)) / NrS
    CMbuffer = np.divide((np.dot(np.transpose(mat[i:mat.shape[0], :]), mat[0:mat.shape[0] - i, :])),(np.dot(np.transpose(r), r))) / NrS
    for counter_1 in range(0, NrC):
        CM[counter_1, ind, :] = CMbuffer[counter_1]
    #counter = counter + 1
    # np.divide((np.dot(np.transpose(mat[0:mat.shape[0], :]), mat[0:mat.shape[0] - 0, :])), (np.dot(np.transpose(r), r)) )/ NrS
    # CM(ind,:,:)=(u_0(1+i:end,:)'*u_0(1:end-i,:))./(r'*r)/NrS;
    # takes longer, no performance impact
    ind = ind + 1

# Usage of symmetric construction of cross correlation for faster calculation:
# helping = np.max(neg_wins)+np.max(co_wins)-1
# @TODO potenzieller Bug!!, weil 0 harcodede in helper
helping = np.max(neg_wins)+np.max(co_wins)
helper = np.arange(helping)
helper = helper[helping:0:-1]
helper = np.append(helper, 0)
# @TODO hier STOP!
# @TODO hier STOP!
if(np.max(neg_wins)+np.max(co_wins) > 0):
    bufCM = np.zeros(shape=(NrC,NrC))
    ind = -1
    for j in helper:
        bufCM = CM[:, np.max(neg_wins) + np.max(co_wins) + j-1, :]
        # bufCM = CMbuffer
        ind = ind + 1
        for counter_1 in range(0, NrC):
            # CM[counter_1, ind, :] = CMbuffer[counter_1]
            CM[counter_1, ind, :] = np.transpose(bufCM[counter_1])

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
sumWin=np.zeros(shape=(d+WB,NrC,NrC))
in_=-1
temp_in_=30
win_inner = np.zeros(shape=(1, 30))
beginnings = np.zeros(shape=(1, 30))
windows = []
windows = [[] for temp_in_ in range(temp_in_)]
"""for win_before in neg_wins:
    # for win_p1 in range(0, co_wins):
    win_p1 = co_wins
    for win_in in pos_wins:
        in_=in_+1
        win_p2 = win_p1
        win_after=win_before
        first_append = np.array([-1*np.ones(shape=(win_before, 1)) / win_before])
        windows[in_].append(first_append.tolist)
        # windows[in_].append([-1*np.ones(shape=(win_before, 1)) / win_before])
        if win_p1 != 0: # @TODO: potenzieller B
            windows[in_].append([1*np.zeros(shape=(win_p1, 1))])
        windows[in_].append([2/win_in * np.ones(shape=(win_in, 1))])
        if win_p2 != 0: # @TODO: potenzieller Bug
            windows[in_].append([np.zeros(shape=(win_p2, 1))])
        windows[in_].append([-1*np.ones(shape=(win_after, 1)) / win_after])
        # windows[in_]=-1*np.ones(win_before,1) /win_before; np.zeros(win_p1,1);2/win_in* np.ones(win_in,1);np.zeros(win_p2,1);-1*np.ones(win_after,1)/win_after
        beginnings[0, in_]=int(1+WB-win_before-win_p1)
        win_inner[0, in_]=win_in"""

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
    indi = 0
    for runner_1 in range(0, len(windows[runner])):

        var = windows[runner][runner_1][0].tolist()
        wnew_windows[runner].append(var)
        # wnew_windows[runner].append(windows[runner][runner_1+1][0].tolist())

    indi = indi + 1
        # wnew_windows[runner].append(windows[runner][runner_1][0].tolist())
    # wnew_windows[runner] = np.append(wnew_windows, windows[runner][1]).tolist()
    # wnew_windows[runner] = np.append(wnew_windows, windows[runner][2])

#########################
# Usage of edge filters #
#########################
# Matlab end -> .shape[0] python
from scipy import signal
# f = signal.fftconvolve(x, y)
# CM(np.isnan(CM))=0
np.nan_to_num(x=CM,copy=False, nan = 0) # if CM contains many NaNs, only NaNs remains after convolution. e.g. for very short spike trains
for j in range(0, in_):
    CM3 = signal.fftconvolve(CM[beginnings[0][j]:CM.shape[0], :, :], windows[j], 'valid')
print("sucsess!")
