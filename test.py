import numpy as np
import pandas as pd

from Plots.TSPE_plot import plot_CM_test, plot_CM
from numpy import load
# load array
CM = load('CM.npy')
#print(CM)
#CM = np.zeros(shape=(60, 60))
#CM[1,8] = 1
#CM[0,0] = 30
#CM = np.zeros((64, 64), dtype=np.int)


#CM = np.zeros((64, 64), dtype=np.int)
#CM[30,40] = 10

#CM[50,59] = 100



# from Plots.TSPE_plot import plot_CM
plot_CM(CM, "")
