import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
"""
Berechnet eine verbesserte CM Matrix entsprechend:
Thresholding Functional Connectivity Matrices to Recover the Topological Properties of Large-Scale Neuronal Networks.
Alessio Boschi, Martina Brofiga and Paolo Massobrio
https://doi.org/10.3389/fnins.2021.705103
Original implementation by: Philipp Steigerwald [s160857@th-ab.de]
"""

def TSPE_HT(CM):
    # CM = np.array([[0, 3, 5, 7, 2], [5, 0, 4, 6, 3], [2, 4, 0, 4, 7], [5, 3, 2, 0, 5], [2, 1, 4, 2, 0]])
    CM1 = np.ma.masked_equal(CM, 0)
    std = np.std(CM1, ddof=1)
    mean = np.mean(CM1)
    HT = std + mean
    T1CM = np.where(CM > HT, CM, 0)
    return T1CM

def TSPE_DDT(T1CM, CM):
    # T1CM = np.array([[0, 0, 0, 7, 0], [0, 0, 0, 6, 0], [0, 0, 0, 0, 7], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    El_anzahl = T1CM.shape[0]
    # RM = np.array([[0, 3, 5, 0, 2], [5, 0, 4, 0, 3], [2, 4, 0, 4, 0], [5, 3, 2, 0, 5], [2, 1, 4, 2, 0]])
    RM = CM - T1CM
    RM1 = np.ma.masked_equal(RM, 0)
    TM = np.zeros(shape=(El_anzahl, El_anzahl))
    for i in range(0, RM.shape[0]):
        iRow = RM1[i]
        i_Row = RM[i]
        if np.count_nonzero(i_Row) == 0:
            # @TODO: pass oder TM[i] = np.mean(iRow) oder TM[i] = 0
            TM[i] = 0
        elif np.count_nonzero(i_Row) == 1:
            TM[i] = 0
        elif np.count_nonzero(i_Row) == 2:
            TM[i] = np.mean(iRow) + np.std(iRow, ddof=1)
        else:
            for y in range(0, RM.shape[0]):
                iRow.mask[y] = True
                TM[i, y] = np.mean(iRow) + np.std(iRow, ddof=1)
                if i_Row[y] != 0:
                    iRow.mask[y] = False
    T2CM = RM > TM
    T2CM = ma.masked_where(~T2CM, RM, copy=True)
    T2CM = T2CM.filled(0)
    FM = T1CM + T2CM




    """fig, axs = plt.subplots(1, 6)
    fig.suptitle('TSPE')
    axs[0].set_title("CM")
    axs[1].set_title("T1CM")
    axs[2].set_title("RM")
    axs[3].set_title("TM")
    axs[4].set_title("T2CM")
    axs[5].set_title("FM")

    CM_inh_TSPE = np.array([[0, 3, 5, 7, 2], [5, 0, 4, 6, 3], [2, 4, 0, 4, 7], [5, 3, 2, 0, 5], [2, 1, 4, 2, 0]])

    # interpolation argument: https://matplotlib.org/stable/gallery/images_contours_and_fields/interpolation_methods.html
    axs[0].imshow(CM_inh_TSPE, cmap="viridis", interpolation='nearest')
    axs[1].imshow(T1CM, interpolation='nearest')
    axs[2].imshow(RM, interpolation='nearest')
    axs[3].imshow(TM, interpolation='nearest')
    axs[4].imshow(T2CM, interpolation='nearest')
    axs[5].imshow(FM, interpolation='nearest')
    fig.show()"""









    return FM