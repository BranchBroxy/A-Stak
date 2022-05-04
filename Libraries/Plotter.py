
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import QtWidgets
import numpy as np
from Libraries.Import import get_variables, get_file_and_extension

from Libraries.AStakEngine import get_astak_variables

from Libraries.AStakAlgo.TSPE_Treshhold import *
from Libraries.MatLabEngine import get_matlab_variables

import matplotlib.colors as colors

from PyQt5 import sip

main_ui = object
MainWindow = object

spike_list = np.zeros(0)
amp = np.zeros(0)
rec_dur = 0
SaRa = 0
flag_wid = False




def plotter(ui, MainWindow):
    global main_ui, flag_wid
    main_ui = ui
    main_ui.plot = QtWidgets.QVBoxLayout(main_ui.plot_frame)
    sc = MplCanvas(main_ui, width=5, height=4, dpi=100)
    toolbar = NavigationToolbar(sc, MainWindow)
    main_ui.plot.addWidget(toolbar)
    main_ui.plot.addWidget(sc)
    main_ui.plot.deleteLater()

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):

        print("sc")
        # @TODO Plot Klasse aufräumen
        # @TODO Plots updatbar machen, um neue Plots generieren zu können
        # fig = Figure(figsize=(width, height), dpi=dpi)
        # self.axes = fig.add_subplot(111)
        # np.random.seed(789680)
    # def draw(self):
        data1 = np.random.random([6, 50])
        global spike_list
        global amp
        global rec_dur
        global SaRa
        spike_list, amp, rec_dur, SaRa = get_variables()
        filepath, extension = get_file_and_extension()
        datas = spike_list
        longest = datas.max()
        # datas = np.where(np.invert(0 == datas), datas, float("nan"))
        datas = np.where(np.invert(0 == datas), datas, np.nan)
        colors1 = ['C{}'.format(i) for i in range(6)]
        lineoffsets1 = np.array([-9, -13, 1,
                                 15, 6, 10])

        # linelengths1 = [5, 2, 9, 11, 3, 5]

        self.fig, self.axs = plt.subplots()

        # axs.eventplot(data1, colors=colors1, lineoffsets=lineoffsets1, linelengths=linelengths1)
        # @TODO Achsen anpassbar machen
        if extension == "dat":
            print("dat")
            self.axs.plt(spike_list[:, 35])
            self.axs.set_title('Analog Signal Plot')
            super(MplCanvas, self).__init__(self.fig)
        else:
            self.axs.eventplot(datas, color="black")
            self.axs.axis([0, longest + 0.05 * longest, 0, datas.shape[0]])
            self.axs.set_title('Spike Train Plot')
            super(MplCanvas, self).__init__(self.fig)
            # global flag_wid
            # flag_wid = True

    def update(self):
        global spike_list
        global amp
        global rec_dur
        global SaRa
        datas = spike_list
        longest = datas.max()
        datas = np.where(np.invert(0 == datas), datas, np.nan)
        self.fig.clear(True)
        # self.fig.canvas.draw_idle()"""



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


    """CMres_TSPE, DMres_TSPE, CM_exh_TSPE, CM_inh_TSPE = get_astak_variables()
    feature_mean, feature_values, feature_std, feature_pref, feature_label = get_matlab_variables()
    feature_values = np.array(feature_values)
    CM_inh_feature_values = np.where(feature_values > 0, feature_values, 0)

    cmap = plt.get_cmap('viridis')
    new_cmap = truncate_colormap(cmap, 0, 0.5)

    fig, axs = plt.subplots(1, 4)
    fig.suptitle('TSPE')
    axs[0].imshow(CMres_TSPE, cmap=new_cmap, interpolation='nearest')
    axs[1].imshow(feature_values, interpolation='nearest')
    difference = CMres_TSPE - feature_values
    axs[2].imshow(difference, cmap=new_cmap, interpolation='nearest')
    divison = CMres_TSPE / feature_values
    axs[3].imshow(divison, cmap=new_cmap, interpolation='nearest')
    axs[0].set_title("CMres TSPE Python")
    axs[1].set_title("CMres TSPE MatLab")
    axs[2].set_title("Error")
    axs[3].set_title("Div")
    fig.show()"""
    spike_list, amp, rec_dur, SaRa = get_variables()
    datas = spike_list
    longest = datas.max()
    # datas = np.where(np.invert(0 == datas), datas, float("nan"))
    datas = np.where(np.invert(0 == datas), datas, np.nan)
    plt.eventplot(datas[55, :], color="black")
    # plt.plot(peaks, x[peaks], "x")
    plt.show()


def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap