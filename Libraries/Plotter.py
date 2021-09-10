
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import QtWidgets
import numpy as np
from Libraries.Import import get_variables

from Libraries.AStakEngine import get_astak_variables
from Libraries.MatLabEngine import get_matlab_variables

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
    toolbar = NavigationToolbar(sc,MainWindow)
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
        axs.axis([0, longest + 0.05*longest, 0, datas.shape[0]])
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
    CMres_TSPE, DMres_TSPE, CM_exh_TSPE, CM_inh_TSPE = get_astak_variables()
    feature_mean, feature_values, feature_std, feature_allEl = get_matlab_variables()
    fig, axs = plt.subplots(1, 3)
    fig.suptitle('TSPE')
    axs[0].imshow(CMres_TSPE, cmap='Blues', interpolation='nearest')
    axs[1].imshow(feature_values, cmap='Blues', interpolation='nearest')
    difference = CMres_TSPE - feature_values
    axs[2].imshow(difference, cmap='Blues', interpolation='nearest')
    fig.show()
    """tspe_plt = plt
    tspe_plt.
    tspe_plt.show()
    mtl_plt = plt
    mtl_plt.
    mtl_plt.show()"""