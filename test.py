import numpy as np
from scipy import stats

RM = np.array([[0, 3, 5, 0, 2], [5, 0, 4, 0, 3], [2, 4, 0, 4, 0], [5, 3, 2, 0, 5], [2, 1, 4, 2, 0]])
RM1 = np.ma.masked_equal(RM, 0)
# RM2 = RM.compressed() # get normal array with masked values removed
# RM3 = RM.mask # get a boolean array of the mask
# RM4 = RM.mean() # it automatically discards masked values
TM = np.zeros(shape=(5, 5))
TM2CM = np.zeros(shape=(5, 5))
FM = np.zeros(shape=(5, 5))
for i in range(0, RM.shape[0]):
    for y in range(0, RM.shape[0]):
        iRow = RM1[i]
        i_Row = RM[i]
        iRow.mask[y] = True
        TM[i, y] = np.mean(iRow) + np.std(iRow, ddof=1)
        if i_Row[y] != 0:
            iRow.mask[y] = False
print(RM)
print(TM)
T2CM = RM > TM

print (T2CM)