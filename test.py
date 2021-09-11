import numpy as np
import numpy.ma as ma
from scipy import stats
from Libraries.AStakAlgo.TSPE_Treshhold import *

CM = np.array([[0, 3, 5, 7, 2], [5, 0, 4, 6, 3], [2, 4, 0, 4, 7], [5, 3, 2, 0, 5], [2, 1, 4, 2, 0]])
T1CM = TSPE_HT(CM)
FM = TSPE_DDT(T1CM, CM)
print(FM)
