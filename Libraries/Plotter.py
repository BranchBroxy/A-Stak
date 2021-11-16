
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import QtWidgets
import numpy as np
from Libraries.Import import get_variables

from Libraries.AStakEngine import get_astak_variables

from Libraries.AStakAlgo.TSPE_Treshhold import *
from Libraries.MatLabEngine import get_matlab_variables
import matplotlib.colors as colors

main_ui = object
MainWindow = object

spike_list = np.zeros(0)
amp = np.zeros(0)
rec_dur = 0
SaRa = 0

def plotter(ui, MainWindow):
    global main_ui
    main_ui = ui
    sc = MplCanvas(main_ui, width=5, height=4, dpi=100)
    main_ui.plot = QtWidgets.QVBoxLayout(main_ui.plot_frame)
    toolbar = NavigationToolbar(sc, MainWindow)
    # main_ui.plot.removeWidget(toolbar)
    # main_ui.plot.removeWidget(sc)
    main_ui.plot.addWidget(toolbar)
    main_ui.plot.addWidget(sc)



class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # @TODO Plot Klasse aufräumen
        # @TODO Plots updatbar machen, um neue Plots generieren zu können
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        np.random.seed(789680)
        data1 = np.random.random([6, 50])
        global spike_list
        global amp
        global rec_dur
        global SaRa
        spike_list, amp, rec_dur, SaRa = get_variables()
        datas = spike_list
        longest = datas.max()
        # datas = np.where(np.invert(0 == datas), datas, float("nan"))
        datas = np.where(np.invert(0 == datas), datas, np.nan)
        colors1 = ['C{}'.format(i) for i in range(6)]
        lineoffsets1 = np.array([-9, -13, 1,
                                 15, 6, 10])

        # linelengths1 = [5, 2, 9, 11, 3, 5]

        fig, axs = plt.subplots()

        # axs.eventplot(data1, colors=colors1, lineoffsets=lineoffsets1, linelengths=linelengths1)
        # @TODO Achsen anpassbar machen
        axs.eventplot(datas, color = "black")
        axs.axis([0, longest + 0.05*longest, -1, datas.shape[0]])
        axs.set_title('Spike Train Plot')
        super(MplCanvas, self).__init__(fig)

    def plot_spikes(data):
        #matplotlib.rcParams['font.size'] = 8.0
        colors2 = 'black'
        lineoffsets2 = 1
        linelengths2 = 1
        plt.eventplot(data, colors=colors2, lineoffsets=lineoffsets2, linelengths=linelengths2)

def plotter_init(ui, MainWindow):
    global main_ui
    main_ui = ui
    sc = MplCanvas_init(main_ui, width=5, height=4, dpi=100)
    main_ui.plot = QtWidgets.QVBoxLayout(main_ui.plot_frame)
    toolbar = NavigationToolbar(sc, MainWindow)
    main_ui.plot.addWidget(toolbar)
    main_ui.plot.addWidget(sc)



class MplCanvas_init(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # @TODO Plot Klasse aufräumen
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        fig, axs = plt.subplots()
        axs.eventplot([[0,0]])
        axs.axis([0, 60, 0, 60])
        axs.set_title('Plot')
        super(MplCanvas_init, self).__init__(fig)

def plot_tab_plotter():
    from Libraries.AStakAlgo.TSPE_Treshhold import TSPE_DDT, TSPE_HT
    # CMres_TSPE, DMres_TSPE, CM_exh_TSPE, CM_inh_TSPE = get_astak_variables()
    """CM_inh_TSPE = np.array([[0, 3, 5, 7, 2], [5, 0, 4, 6, 3], [2, 4, 0, 4, 7], [5, 3, 2, 0, 5], [2, 1, 4, 2, 0]])
    T1CM = TSPE_HT(CM_inh_TSPE)
    FM = TSPE_DDT(T1CM, CM_inh_TSPE)

    fig, axs = plt.subplots(1, 3)
    fig.suptitle('TSPE')
    axs[0].set_title("CMres_TSPE")
    axs[1].set_title("T1CM")
    axs[2].set_title("FM")

    # interpolation argument: https://matplotlib.org/stable/gallery/images_contours_and_fields/interpolation_methods.html
    axs[0].imshow(CM_inh_TSPE, cmap="viridis",  interpolation='nearest')
    axs[1].imshow(T1CM, interpolation='nearest')
    axs[2].imshow(FM, interpolation='nearest')
    fig.show()"""

    CMres_TSPE, DMres_TSPE, CM_exh_TSPE, CM_inh_TSPE = get_astak_variables()
    feature_mean, feature_values, feature_std, feature_allEl = get_matlab_variables()
    feature_values =  np.array(feature_values)
    CM_inh_feature_values = np.where(feature_values > 0, feature_values, 0)

    cmap = plt.get_cmap('viridis')
    new_cmap = truncate_colormap(cmap, 0, 0.5)

    """fig, axs = plt.subplots(1, 3)
    fig.suptitle('TSPE')
    axs[0].imshow(CMres_TSPE, interpolation='nearest')
    axs[1].imshow(feature_values,  interpolation='nearest')
    difference = CMres_TSPE - feature_values

    axs[2].imshow(difference, cmap=new_cmap, interpolation='nearest')
    axs[0].set_title("CMres TSPE Python")
    axs[1].set_title("CMres TSPE MatLab")
    axs[2].set_title("Error")
    fig.show()"""

    fig, axs = plt.subplots(1, 3)
    fig.suptitle('TSPE')
    axs[0].imshow(CM_inh_TSPE, interpolation='nearest')
    axs[1].imshow(CM_inh_feature_values, interpolation='nearest')
    difference = CM_inh_TSPE - CM_inh_feature_values

    axs[2].imshow(difference, cmap=new_cmap, interpolation='nearest')
    axs[0].set_title("CMres_inh TSPE Python")
    axs[1].set_title("CMres_inh TSPE MatLab")
    axs[2].set_title("Error")
    fig.show()

    """CM_python = TSPE_HT(CM_inh_TSPE)
    CM_matalb = TSPE_HT(CM_inh_feature_values)
    ddt_python = TSPE_DDT(CM_python, CMres_TSPE)
    ddt_matlab = TSPE_DDT(CM_matalb, feature_values)

    fig, axs = plt.subplots(1, 3)
    fig.suptitle('TSPE')
    axs[0].imshow(ddt_python, interpolation='nearest')
    axs[1].imshow(ddt_matlab,  interpolation='nearest')
    difference = ddt_python - ddt_matlab
    axs[2].imshow(difference, interpolation='nearest')
    axs[0].set_title("CMres/DDT TSPE Python")
    axs[1].set_title("CMres/DDT TSPE MatLab")
    axs[2].set_title("Error")
    fig.show()"""


def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap