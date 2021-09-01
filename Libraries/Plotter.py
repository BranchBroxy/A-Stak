
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import QtWidgets


main_ui = object
MainWindow = object


def plotter(ui, MainWindow):
    global main_ui
    main_ui = ui
    sc = MplCanvas(main_ui, width=5, height=4, dpi=100)
    sc.axes.plot([[1, 2, 3, 4], [2, 3, 4, 5]])
    main_ui.plot = QtWidgets.QVBoxLayout(main_ui.plot_frame)
    toolbar = NavigationToolbar(sc, MainWindow)
    main_ui.plot.addWidget(toolbar)
    main_ui.plot.addWidget(sc)


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # self.axes = fig.add_subplot(111).evenplot(Import.spike_list)
        super(MplCanvas, self).__init__(fig)

    def plot_spikes(data):
        #matplotlib.rcParams['font.size'] = 8.0
        colors2 = 'black'
        lineoffsets2 = 1
        linelengths2 = 1
        plt.eventplot(data, colors=colors2, lineoffsets=lineoffsets2, linelengths=linelengths2)