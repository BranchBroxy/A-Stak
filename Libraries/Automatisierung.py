import numpy as np
import h5py  # hdf5
import scipy.io
import matplotlib.pyplot as plt
from Libraries.MatLabEngine import matlab_calc_all_feature_return
import os
import glob
from os import listdir
import csv
from numpy import save

filepath = "/run/user/1000/gvfs/smb-share:server=192.168.2.119,share=home/Uni/Masterarbeit/Daten/LSD Experimente SWTEO Th 5/0221/TS_SWTEO/2 DMSO/Messung21.02.2022_16-34-28_TS.mat"

def import_mat(path):


    path = path
    mat_data = scipy.io.loadmat(path)
    try:
        spike_list = np.transpose(mat_data["SPIKEZ"]["TS"][0, 0])
        # if spike_list.shape ==
        spike_list = np.where(np.invert(np.isnan(spike_list)), spike_list, 0)
        amp = np.zeros([spike_list.shape[1], spike_list.shape[0]])
        rec_dur = float(mat_data["SPIKEZ"][0, 0]["PREF"][0, 0]["rec_dur"][0])
        SaRa = mat_data["SPIKEZ"][0, 0]["PREF"][0, 0]["SaRa"][0][0]
        flag_mat_v1 = True
        if np.transpose(mat_data["temp"]["SPIKEZ"][0, 0]["TS"][0, 0]).shape[1] == 0:
            print("Mat Datei leer")
            spike_list = np.array([1, 1])
            amp = np.array([0, 0])
            rec_dur = 1
            SaRa = 1000
        else:
            print("Mat Datei erfolgreich importiert")
    except:
        try:
            spike_list = np.transpose(mat_data["temp"]["SPIKEZ"][0, 0]["TS"][0, 0])
            amp = mat_data["temp"]["SPIKEZ"][0, 0]["AMP"][0, 0]
            rec_dur = mat_data["temp"]["SPIKEZ"][0, 0]["PREF"][0,0]["rec_dur"][0, 0][0][0]
            SaRa = mat_data["temp"]["SPIKEZ"][0, 0]["PREF"][0, 0]["SaRa"][0, 0][0][0]
            flat_mat_v2 = True
            if np.transpose(mat_data["temp"]["SPIKEZ"][0, 0]["TS"][0, 0]).shape[1] == 0:
                print("Mat Datei leer")
                spike_list = np.array([1, 1])
                amp = np.array([0, 0])
                rec_dur = 1
                SaRa = 1000
            else:
                print("Mat Datei erfolgreich importiert")
        except:
            print("Mat Datei konnte nicht importiert werden")
    return spike_list, amp, rec_dur, SaRa

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text  # or whatever

# import_mat()
# datas = spike_list
"""longest = datas.max()
datas = np.where(np.invert(0 == datas), datas, np.nan)
plt.eventplot(datas, color="black")
plt.axis([0, longest + 0.05 * longest, 0, datas.shape[0]])
plt.title('Spike Train Plot')
plt.show()"""
mypath = "/run/user/1000/gvfs/smb-share:server=192.168.2.119,share=home/Uni/Masterarbeit/Daten/LSD Experimente SWTEO Th 4.5 sotieren cut/0222"
csv_name = '/run/user/1000/gvfs/smb-share:server=192.168.2.119,share=home/Uni/Masterarbeit/Daten/LSD Experimente SWTEO Th 4.5 sotieren cut/0222.csv'
# mypath = "/mnt/HDD/FauBox"
files = []
all_directories = [x[0] for x in os.walk(mypath)]
for i in all_directories:
    mat_file = glob.glob(os.path.join(i, "*.mat"))
    if mat_file != []:
        files.append(mat_file)
for y in files:
    print(y)
print(len(files))
test = files[0:5]
# print(test)
# files = test
csv_export = []
mean = []
std = []
label = []
n_files = len(files)
n_feature = 10
to_csv = np.zeros(shape=(n_files*4, n_feature+1), dtype=object)

for counter, y in enumerate(files):
    print(f'Datei {counter + 1}. aus {n_files}')
    spike_list, amp, rec_dur, SaRa = import_mat(y[0])
    #file_name = y[0] - mypath
    file_name = remove_prefix(y[0], mypath)
    feature_mean, feature_std, feature_values, feature_pref, feature_label = matlab_calc_all_feature_return(spike_list, amp, rec_dur, SaRa)
    #save = np.asarray([feature_mean, feature_std, feature_values, feature_pref, feature_label])
    # saver = np.asarray([feature_mean, feature_std, feature_label])
    #shape = save.shape

    #to_csv[counter][0] = str(feature_mean[counter][0])
    #to_csv[counter][1] = feature_std[counter][0]
    #to_csv[counter][2] = feature_label[counter][0]
    to_csv[0 + 4 * counter][1] = file_name
    for b in range(0, n_feature):
        to_csv[0 + 4 * counter][0] = "File"
        to_csv[1 + 4 * counter][0] = "Label"
        to_csv[2 + 4 * counter][0] = "Mean"
        to_csv[3 + 4 * counter][0] = "Std"

        to_csv[1+4*counter][b+1] = feature_label[b][0]
        to_csv[2+4*counter][b+1] = feature_mean[b][0]
        to_csv[3+4*counter][b+1] = feature_std[b][0]

        #mean.append(feature_mean[b][0])
        #std.append(feature_std[b][0])
        #label.append(feature_label[b][0])

        #csv_export.append(label)
        #csv_export.append(mean)
        #csv_export.append(std)
        # csv_export.append(y[0])
spike_rate_means_DMSO = []
spike_rate_means_LSD = []
Number_of_spikes_means_DMSO = []
Number_of_spikes_means_LSD = []
Amplitude_means_DMSO = []
Amplitude_means_LSD = []
ActiveElectrodes_means_DMSO = []
ActiveElectrodes_means_LSD = []
BR_baker100_means_DMSO = []
BR_baker100_means_LSD = []
BD_baker100_means_DMSO = []
BD_baker100_means_LSD = []
Sync_Contrast_means_DMSO = []
Sync_Contrast_means_LSD = []
Entropy_bin100_means_DMSO = []
Entropy_bin100_means_LSD = []
Entropy_capurro_means_DMSO = []
Entropy_capurro_means_LSD = []
Sync_CC_selinger_means_DMSO = []
Sync_CC_selinger_means_LSD = []

for a in range(n_files):
    if "DMSO" in to_csv[a*4,1]:
        spike_rate_means_DMSO.append(to_csv[a*4+2, 1])
        Number_of_spikes_means_DMSO.append(to_csv[a*4+2, 2])
        Amplitude_means_DMSO.append(to_csv[a*4+2, 3])
        ActiveElectrodes_means_DMSO.append(to_csv[a*4+2, 4])
        BR_baker100_means_DMSO.append(to_csv[a*4+2, 5])
        Sync_Contrast_means_DMSO.append(to_csv[a*4+2, 6])
        Entropy_bin100_means_DMSO.append(to_csv[a*4+2, 7])
        Entropy_capurro_means_DMSO.append(to_csv[a*4+2, 8])
        Sync_CC_selinger_means_DMSO.append(to_csv[a*4+2, 9])
        BD_baker100_means_DMSO.append(to_csv[a * 4 + 2, 10])
    else:
        spike_rate_means_LSD.append(to_csv[a*4+2, 1])
        Number_of_spikes_means_LSD.append(to_csv[a*4+2, 2])
        Amplitude_means_LSD.append(to_csv[a*4+2, 3])
        ActiveElectrodes_means_LSD.append(to_csv[a*4+2, 4])
        BR_baker100_means_LSD.append(to_csv[a*4+2, 5])
        Sync_Contrast_means_LSD.append(to_csv[a*4+2, 6])
        Entropy_bin100_means_LSD.append(to_csv[a*4+2, 7])
        Entropy_capurro_means_LSD.append(to_csv[a * 4 + 2, 8])
        Sync_CC_selinger_means_LSD.append(to_csv[a * 4 + 2, 9])
        BD_baker100_means_LSD.append(to_csv[a * 4 + 2, 10])
#mean_data =
spike_rate_mean_DMSO = np.array(spike_rate_means_DMSO).mean()
spike_rate_mean_LSD = np.array(spike_rate_means_LSD).mean()
Number_of_spikes_mean_DMSO = np.array(Number_of_spikes_means_DMSO).mean()
Number_of_spikes_mean_LSD = np.array(Number_of_spikes_means_LSD).mean()
Amplitude_mean_DMSO = np.array(Amplitude_means_DMSO).mean()
Amplitude_mean_LSD = np.array(Amplitude_means_LSD).mean()
ActiveElectrodes_mean_DMSO = np.array(ActiveElectrodes_means_DMSO).mean()
ActiveElectrodes_mean_LSD = np.array(ActiveElectrodes_means_LSD).mean()
BR_baker100_mean_DMSO = np.array(BR_baker100_means_DMSO).mean()
BR_baker100_mean_LSD = np.array(BR_baker100_means_LSD).mean()
BD_baker100_mean_DMSO = np.array(BD_baker100_means_DMSO).mean()
BD_baker100_mean_LSD = np.array(BD_baker100_means_LSD).mean()
Sync_Contrast_mean_DMSO = np.array(Sync_Contrast_means_DMSO).mean()
Sync_Contrast_mean_LSD = np.array(Sync_Contrast_means_LSD).mean()
Entropy_bin100_mean_DMSO = np.array(Entropy_bin100_means_DMSO).mean()
Entropy_bin100_mean_LSD = np.array(Entropy_bin100_means_LSD).mean()
Entropy_capurro_mean_DMSO = np.array(Entropy_capurro_means_DMSO).mean()
Entropy_capurro_mean_LSD = np.array(Entropy_capurro_means_LSD).mean()
Sync_CC_selinger_mean_DMSO = np.array(Sync_CC_selinger_means_DMSO).mean()
Sync_CC_selinger_mean_LSD  = np.array(Sync_CC_selinger_means_LSD).mean()

spike_rate_std_DMSO = np.array(spike_rate_means_DMSO).std()
spike_rate_std_LSD = np.array(spike_rate_means_LSD).std()
Number_of_spikes_std_DMSO = np.array(Number_of_spikes_means_DMSO).std()
Number_of_spikes_std_LSD = np.array(Number_of_spikes_means_LSD).std()
Amplitude_std_DMSO = np.array(Amplitude_means_DMSO).std()
Amplitude_std_LSD = np.array(Amplitude_means_LSD).std()
ActiveElectrodes_std_DMSO = np.array(ActiveElectrodes_means_DMSO).std()
ActiveElectrodes_std_LSD = np.array(ActiveElectrodes_means_LSD).std()
BR_baker100_std_DMSO = np.array(BR_baker100_means_DMSO).std()
BR_baker100_std_LSD = np.array(BR_baker100_means_LSD).std()
BD_baker100_std_DMSO = np.array(BD_baker100_means_DMSO).std()
BD_baker100_std_LSD = np.array(BD_baker100_means_LSD).std()
Sync_Contrast_std_DMSO = np.array(Sync_Contrast_means_DMSO).std()
Sync_Contrast_std_LSD = np.array(Sync_Contrast_means_LSD).std()
Entropy_bin100_std_DMSO = np.array(Entropy_bin100_means_DMSO).std()
Entropy_bin100_std_LSD = np.array(Entropy_bin100_means_LSD).std()
Entropy_capurro_std_DMSO = np.array(Entropy_capurro_means_DMSO).std()
Entropy_capurro_std_LSD = np.array(Entropy_capurro_means_LSD).std()
Sync_CC_selinger_std_DMSO = np.array(Sync_CC_selinger_means_DMSO).std()
Sync_CC_selinger_std_LSD  = np.array(Sync_CC_selinger_means_LSD).std()

csv_export_feature = np.zeros(shape=(5, n_feature + 1), dtype=object)
csv_export_feature[0, 1] = "Spike Rate"
csv_export_feature[0, 2] = "Number of Spikes"
csv_export_feature[0, 3] = "Amplitude"
csv_export_feature[0, 4] = "Active Electrodes"
csv_export_feature[0, 5] = "Burst Rate Baker"
csv_export_feature[0, 6] = "Spike Contrast"
csv_export_feature[0, 7] = "Entropy_bin100"
csv_export_feature[0, 8] = "Entropy_capurro"
csv_export_feature[0, 9] = "Sync_CC_selinger"
csv_export_feature[0, 10] = "Burst Duration Baker"

csv_export_feature[1, 0] = "LSD Mean"
csv_export_feature[2, 0] = "DMSO Mean"
csv_export_feature[3, 0] = "LSD Std"
csv_export_feature[4, 0] = "DMSO Std"

csv_export_feature[1, 1] = spike_rate_mean_LSD
csv_export_feature[1, 2] = Number_of_spikes_mean_LSD
csv_export_feature[1, 3] = Amplitude_mean_LSD
csv_export_feature[1, 4] = ActiveElectrodes_mean_LSD
csv_export_feature[1, 5] = BR_baker100_mean_LSD
csv_export_feature[1, 6] = Sync_Contrast_mean_LSD
csv_export_feature[1, 7] = Entropy_bin100_mean_LSD
csv_export_feature[1, 8] = Entropy_capurro_mean_LSD
csv_export_feature[1, 9] = Sync_CC_selinger_mean_LSD
csv_export_feature[1, 10] = BD_baker100_mean_LSD

csv_export_feature[2, 1] = spike_rate_mean_DMSO
csv_export_feature[2, 2] = Number_of_spikes_mean_DMSO
csv_export_feature[2, 3] = Amplitude_mean_DMSO
csv_export_feature[2, 4] = ActiveElectrodes_mean_DMSO
csv_export_feature[2, 5] = BR_baker100_mean_DMSO
csv_export_feature[2, 6] = Sync_Contrast_mean_DMSO
csv_export_feature[2, 7] = Entropy_bin100_mean_DMSO
csv_export_feature[2, 8] = Entropy_capurro_mean_DMSO
csv_export_feature[2, 9] = Sync_CC_selinger_mean_DMSO
csv_export_feature[2, 10] = BD_baker100_mean_DMSO

csv_export_feature[3, 1] = spike_rate_std_LSD
csv_export_feature[3, 2] = Number_of_spikes_std_LSD
csv_export_feature[3, 3] = Amplitude_std_LSD
csv_export_feature[3, 4] = ActiveElectrodes_std_LSD
csv_export_feature[3, 5] = BR_baker100_std_LSD
csv_export_feature[3, 6] = Sync_Contrast_std_LSD
csv_export_feature[3, 7] = Entropy_bin100_std_LSD
csv_export_feature[3, 8] = Entropy_capurro_std_LSD
csv_export_feature[3, 9] = Sync_CC_selinger_std_LSD
csv_export_feature[3, 10] = BD_baker100_std_LSD

csv_export_feature[4, 1] = spike_rate_std_DMSO
csv_export_feature[4, 2] = Number_of_spikes_std_DMSO
csv_export_feature[4, 3] = Amplitude_std_DMSO
csv_export_feature[4, 4] = ActiveElectrodes_std_DMSO
csv_export_feature[4, 5] = BR_baker100_std_DMSO
csv_export_feature[4, 6] = Sync_Contrast_std_DMSO
csv_export_feature[4, 7] = Entropy_bin100_std_DMSO
csv_export_feature[4, 8] = Entropy_capurro_std_DMSO
csv_export_feature[4, 9] = Sync_CC_selinger_std_DMSO
csv_export_feature[4, 10] = BD_baker100_std_DMSO




# big = []
# big.append(csv_export)
with open(csv_name, 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    for counter_csv, a in enumerate(to_csv):
        if counter_csv % 4 == 0 and counter_csv != 0:
            writer.writerow([])
        writer.writerow(a)
    writer.writerow([])
    for y in csv_export_feature:
        writer.writerow(y)

#save("/run/user/1000/gvfs/smb-share:server=192.168.2.119,share=home/Uni/Masterarbeit/Daten/LSD Experimente SWTEO Th 4.5 sotieren/0214_feature.npy", csv_export_feature)
#save("/run/user/1000/gvfs/smb-share:server=192.168.2.119,share=home/Uni/Masterarbeit/Daten/LSD Experimente SWTEO Th 4.5 sotieren/0214.npy", csv_export)




