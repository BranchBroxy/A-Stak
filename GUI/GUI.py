# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiV5.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 759)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../../../../Masterarbeit/th_ab_logo.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setGeometry(QtCore.QRect(10, 0, 681, 191))
        self.tab.setStatusTip("")
        self.tab.setObjectName("tab")
        self.v_tab = QtWidgets.QWidget()
        self.v_tab.setObjectName("v_tab")
        self.v_tab_DrCellPath_frame = QtWidgets.QFrame(self.v_tab)
        self.v_tab_DrCellPath_frame.setGeometry(QtCore.QRect(10, 10, 491, 51))
        self.v_tab_DrCellPath_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.v_tab_DrCellPath_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.v_tab_DrCellPath_frame.setObjectName("v_tab_DrCellPath_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.v_tab_DrCellPath_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.v_tab_DrCellPath_label = QtWidgets.QLabel(self.v_tab_DrCellPath_frame)
        self.v_tab_DrCellPath_label.setObjectName("v_tab_DrCellPath_label")
        self.horizontalLayout_2.addWidget(self.v_tab_DrCellPath_label)
        self.v_tab_DrCellPath_lineEdit = QtWidgets.QLineEdit(self.v_tab_DrCellPath_frame)
        self.v_tab_DrCellPath_lineEdit.setObjectName("v_tab_DrCellPath_lineEdit")
        self.horizontalLayout_2.addWidget(self.v_tab_DrCellPath_lineEdit)
        self.v_tab_DrCellPath_browse_button = QtWidgets.QPushButton(self.v_tab_DrCellPath_frame)
        self.v_tab_DrCellPath_browse_button.setObjectName("v_tab_DrCellPath_browse_button")
        self.horizontalLayout_2.addWidget(self.v_tab_DrCellPath_browse_button)
        self.v_tab_libraries_button = QtWidgets.QPushButton(self.v_tab)
        self.v_tab_libraries_button.setGeometry(QtCore.QRect(520, 10, 131, 51))
        self.v_tab_libraries_button.setObjectName("v_tab_libraries_button")
        self.v_tab_MatLabPath_frame = QtWidgets.QFrame(self.v_tab)
        self.v_tab_MatLabPath_frame.setGeometry(QtCore.QRect(10, 70, 491, 51))
        self.v_tab_MatLabPath_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.v_tab_MatLabPath_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.v_tab_MatLabPath_frame.setObjectName("v_tab_MatLabPath_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.v_tab_MatLabPath_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.v_tab_MatLabPath_label = QtWidgets.QLabel(self.v_tab_MatLabPath_frame)
        self.v_tab_MatLabPath_label.setObjectName("v_tab_MatLabPath_label")
        self.horizontalLayout_3.addWidget(self.v_tab_MatLabPath_label)
        self.v_tab_MatLabPath_lineEdit = QtWidgets.QLineEdit(self.v_tab_MatLabPath_frame)
        self.v_tab_MatLabPath_lineEdit.setObjectName("v_tab_MatLabPath_lineEdit")
        self.horizontalLayout_3.addWidget(self.v_tab_MatLabPath_lineEdit)
        self.v_tab_MatLabPath_browse_button = QtWidgets.QPushButton(self.v_tab_MatLabPath_frame)
        self.v_tab_MatLabPath_browse_button.setObjectName("v_tab_MatLabPath_browse_button")
        self.horizontalLayout_3.addWidget(self.v_tab_MatLabPath_browse_button)
        self.tab.addTab(self.v_tab, "")
        self.d_tab = QtWidgets.QWidget()
        self.d_tab.setObjectName("d_tab")
        self.d_tab_browse_frame = QtWidgets.QFrame(self.d_tab)
        self.d_tab_browse_frame.setGeometry(QtCore.QRect(20, 20, 491, 51))
        self.d_tab_browse_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.d_tab_browse_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.d_tab_browse_frame.setObjectName("d_tab_browse_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.d_tab_browse_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.d_tab_browse_frame_label = QtWidgets.QLabel(self.d_tab_browse_frame)
        self.d_tab_browse_frame_label.setObjectName("d_tab_browse_frame_label")
        self.horizontalLayout.addWidget(self.d_tab_browse_frame_label)
        self.d_tab_browse_frame_lineEdit = QtWidgets.QLineEdit(self.d_tab_browse_frame)
        self.d_tab_browse_frame_lineEdit.setObjectName("d_tab_browse_frame_lineEdit")
        self.horizontalLayout.addWidget(self.d_tab_browse_frame_lineEdit)
        self.d_tab_browse_frame_button = QtWidgets.QPushButton(self.d_tab_browse_frame)
        self.d_tab_browse_frame_button.setObjectName("d_tab_browse_frame_button")
        self.horizontalLayout.addWidget(self.d_tab_browse_frame_button)
        self.d_tab_data_import_button = QtWidgets.QPushButton(self.d_tab)
        self.d_tab_data_import_button.setGeometry(QtCore.QRect(20, 80, 131, 71))
        self.d_tab_data_import_button.setObjectName("d_tab_data_import_button")
        self.d_tab_plot_button = QtWidgets.QPushButton(self.d_tab)
        self.d_tab_plot_button.setGeometry(QtCore.QRect(160, 80, 131, 71))
        self.d_tab_plot_button.setObjectName("d_tab_plot_button")
        self.tab.addTab(self.d_tab, "")
        self.sta_tab = QtWidgets.QWidget()
        self.sta_tab.setObjectName("sta_tab")
        self.sta_tab_tab = QtWidgets.QTabWidget(self.sta_tab)
        self.sta_tab_tab.setGeometry(QtCore.QRect(0, 0, 681, 161))
        self.sta_tab_tab.setObjectName("sta_tab_tab")
        self.sta_tab_matlab_tab = QtWidgets.QWidget()
        self.sta_tab_matlab_tab.setObjectName("sta_tab_matlab_tab")
        self.sta_tab_matlab_tab_feature_comboBox = QtWidgets.QComboBox(self.sta_tab_matlab_tab)
        self.sta_tab_matlab_tab_feature_comboBox.setGeometry(QtCore.QRect(80, 20, 171, 31))
        self.sta_tab_matlab_tab_feature_comboBox.setObjectName("sta_tab_matlab_tab_feature_comboBox")
        self.sta_tab_matlab_tab_feature_label = QtWidgets.QLabel(self.sta_tab_matlab_tab)
        self.sta_tab_matlab_tab_feature_label.setGeometry(QtCore.QRect(20, 20, 91, 21))
        self.sta_tab_matlab_tab_feature_label.setObjectName("sta_tab_matlab_tab_feature_label")
        self.sta_tab_matlab_tab_feature_calc_button = QtWidgets.QPushButton(self.sta_tab_matlab_tab)
        self.sta_tab_matlab_tab_feature_calc_button.setGeometry(QtCore.QRect(80, 60, 121, 41))
        self.sta_tab_matlab_tab_feature_calc_button.setObjectName("sta_tab_matlab_tab_feature_calc_button")
        self.sta_tab_matlab_tab_auto_calc_label = QtWidgets.QLabel(self.sta_tab_matlab_tab)
        self.sta_tab_matlab_tab_auto_calc_label.setGeometry(QtCore.QRect(330, 20, 101, 21))
        self.sta_tab_matlab_tab_auto_calc_label.setObjectName("sta_tab_matlab_tab_auto_calc_label")
        self.sta_tab_matlab_tab_auto_calc_comboBox = QtWidgets.QComboBox(self.sta_tab_matlab_tab)
        self.sta_tab_matlab_tab_auto_calc_comboBox.setGeometry(QtCore.QRect(430, 20, 171, 31))
        self.sta_tab_matlab_tab_auto_calc_comboBox.setObjectName("sta_tab_matlab_tab_auto_calc_comboBox")
        self.sta_tab_matlab_tab_auto_calc_button = QtWidgets.QPushButton(self.sta_tab_matlab_tab)
        self.sta_tab_matlab_tab_auto_calc_button.setGeometry(QtCore.QRect(430, 60, 201, 41))
        self.sta_tab_matlab_tab_auto_calc_button.setObjectName("sta_tab_matlab_tab_auto_calc_button")
        self.sta_tab_tab.addTab(self.sta_tab_matlab_tab, "")
        self.sta_tab_elephant_tab = QtWidgets.QWidget()
        self.sta_tab_elephant_tab.setObjectName("sta_tab_elephant_tab")
        self.sta_tab_elephant_tab_feature_comboBox = QtWidgets.QComboBox(self.sta_tab_elephant_tab)
        self.sta_tab_elephant_tab_feature_comboBox.setGeometry(QtCore.QRect(80, 20, 171, 31))
        self.sta_tab_elephant_tab_feature_comboBox.setObjectName("sta_tab_elephant_tab_feature_comboBox")
        self.sta_tab_elephant_tab_feature_label = QtWidgets.QLabel(self.sta_tab_elephant_tab)
        self.sta_tab_elephant_tab_feature_label.setGeometry(QtCore.QRect(20, 20, 91, 21))
        self.sta_tab_elephant_tab_feature_label.setObjectName("sta_tab_elephant_tab_feature_label")
        self.sta_tab_elephant_tab_auto_calc_button = QtWidgets.QPushButton(self.sta_tab_elephant_tab)
        self.sta_tab_elephant_tab_auto_calc_button.setGeometry(QtCore.QRect(430, 60, 201, 41))
        self.sta_tab_elephant_tab_auto_calc_button.setObjectName("sta_tab_elephant_tab_auto_calc_button")
        self.sta_tab_elephant_tab_feature_calc_button = QtWidgets.QPushButton(self.sta_tab_elephant_tab)
        self.sta_tab_elephant_tab_feature_calc_button.setGeometry(QtCore.QRect(80, 60, 121, 41))
        self.sta_tab_elephant_tab_feature_calc_button.setObjectName("sta_tab_elephant_tab_feature_calc_button")
        self.sta_tab_elephant_tab_auto_calc_comboBox = QtWidgets.QComboBox(self.sta_tab_elephant_tab)
        self.sta_tab_elephant_tab_auto_calc_comboBox.setGeometry(QtCore.QRect(430, 20, 171, 31))
        self.sta_tab_elephant_tab_auto_calc_comboBox.setObjectName("sta_tab_elephant_tab_auto_calc_comboBox")
        self.sta_tab_elephant_tab_auto_calc_label = QtWidgets.QLabel(self.sta_tab_elephant_tab)
        self.sta_tab_elephant_tab_auto_calc_label.setGeometry(QtCore.QRect(330, 20, 101, 21))
        self.sta_tab_elephant_tab_auto_calc_label.setObjectName("sta_tab_elephant_tab_auto_calc_label")
        self.sta_tab_tab.addTab(self.sta_tab_elephant_tab, "")
        self.sta_tab_astak_tab = QtWidgets.QWidget()
        self.sta_tab_astak_tab.setObjectName("sta_tab_astak_tab")
        self.sta_tab_astak_tab_feature_calc_button = QtWidgets.QPushButton(self.sta_tab_astak_tab)
        self.sta_tab_astak_tab_feature_calc_button.setGeometry(QtCore.QRect(80, 60, 121, 41))
        self.sta_tab_astak_tab_feature_calc_button.setObjectName("sta_tab_astak_tab_feature_calc_button")
        self.sta_tab_astak_tab_auto_calc_button = QtWidgets.QPushButton(self.sta_tab_astak_tab)
        self.sta_tab_astak_tab_auto_calc_button.setGeometry(QtCore.QRect(430, 60, 201, 41))
        self.sta_tab_astak_tab_auto_calc_button.setObjectName("sta_tab_astak_tab_auto_calc_button")
        self.sta_tab_astak_tab_auto_calc_label = QtWidgets.QLabel(self.sta_tab_astak_tab)
        self.sta_tab_astak_tab_auto_calc_label.setGeometry(QtCore.QRect(330, 20, 101, 21))
        self.sta_tab_astak_tab_auto_calc_label.setObjectName("sta_tab_astak_tab_auto_calc_label")
        self.sta_tab_astak_tab_feature_comboBox = QtWidgets.QComboBox(self.sta_tab_astak_tab)
        self.sta_tab_astak_tab_feature_comboBox.setGeometry(QtCore.QRect(80, 20, 171, 31))
        self.sta_tab_astak_tab_feature_comboBox.setObjectName("sta_tab_astak_tab_feature_comboBox")
        self.sta_tab_astak_tab_feature_label = QtWidgets.QLabel(self.sta_tab_astak_tab)
        self.sta_tab_astak_tab_feature_label.setGeometry(QtCore.QRect(20, 20, 91, 21))
        self.sta_tab_astak_tab_feature_label.setObjectName("sta_tab_astak_tab_feature_label")
        self.sta_tab_astak_tab_auto_calc_comboBox = QtWidgets.QComboBox(self.sta_tab_astak_tab)
        self.sta_tab_astak_tab_auto_calc_comboBox.setGeometry(QtCore.QRect(430, 20, 171, 31))
        self.sta_tab_astak_tab_auto_calc_comboBox.setObjectName("sta_tab_astak_tab_auto_calc_comboBox")
        self.sta_tab_tab.addTab(self.sta_tab_astak_tab, "")
        self.tab.addTab(self.sta_tab, "")
        self.p_tab = QtWidgets.QWidget()
        self.p_tab.setObjectName("p_tab")
        self.p_tab_plot_ST_button = QtWidgets.QPushButton(self.p_tab)
        self.p_tab_plot_ST_button.setGeometry(QtCore.QRect(20, 20, 131, 71))
        self.p_tab_plot_ST_button.setObjectName("p_tab_plot_ST_button")
        self.p_tab_plot_feature_button = QtWidgets.QPushButton(self.p_tab)
        self.p_tab_plot_feature_button.setGeometry(QtCore.QRect(450, 60, 131, 71))
        self.p_tab_plot_feature_button.setObjectName("p_tab_plot_feature_button")
        self.p_tab_plot_feature_label = QtWidgets.QLabel(self.p_tab)
        self.p_tab_plot_feature_label.setGeometry(QtCore.QRect(390, 20, 91, 21))
        self.p_tab_plot_feature_label.setObjectName("p_tab_plot_feature_label")
        self.p_tab_plot_feature_comboBox = QtWidgets.QComboBox(self.p_tab)
        self.p_tab_plot_feature_comboBox.setGeometry(QtCore.QRect(450, 20, 171, 31))
        self.p_tab_plot_feature_comboBox.setObjectName("p_tab_plot_feature_comboBox")
        self.tab.addTab(self.p_tab, "")
        self.MainTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.MainTextBrowser.setGeometry(QtCore.QRect(700, 30, 411, 161))
        self.MainTextBrowser.setObjectName("MainTextBrowser")
        self.plot_frame = QtWidgets.QFrame(self.centralwidget)
        self.plot_frame.setGeometry(QtCore.QRect(10, 200, 1101, 511))
        self.plot_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plot_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plot_frame.setObjectName("plot_frame")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1116, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(3)
        self.sta_tab_tab.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "A-Stak"))
        self.v_tab_DrCellPath_label.setStatusTip(_translate("MainWindow", "DrCell Pfad"))
        self.v_tab_DrCellPath_label.setText(_translate("MainWindow", "DrCell Path:"))
        self.v_tab_DrCellPath_lineEdit.setStatusTip(_translate("MainWindow", "DrCell Pfad"))
        self.v_tab_DrCellPath_browse_button.setStatusTip(_translate("MainWindow", "Browse Button"))
        self.v_tab_DrCellPath_browse_button.setText(_translate("MainWindow", "Browse"))
        self.v_tab_libraries_button.setStatusTip(_translate("MainWindow", "Installiere Libraries"))
        self.v_tab_libraries_button.setText(_translate("MainWindow", "Installiere Libraries"))
        self.v_tab_MatLabPath_label.setStatusTip(_translate("MainWindow", "MatLab Pfad"))
        self.v_tab_MatLabPath_label.setText(_translate("MainWindow", "MatLab Path:"))
        self.v_tab_MatLabPath_lineEdit.setStatusTip(_translate("MainWindow", "MatLab Pfad"))
        self.v_tab_MatLabPath_browse_button.setStatusTip(_translate("MainWindow", "Browse Button"))
        self.v_tab_MatLabPath_browse_button.setText(_translate("MainWindow", "Browse"))
        self.tab.setTabText(self.tab.indexOf(self.v_tab), _translate("MainWindow", "Vorbereitung"))
        self.d_tab_browse_frame_label.setStatusTip(_translate("MainWindow", "Datei Name"))
        self.d_tab_browse_frame_label.setText(_translate("MainWindow", "Datei Name"))
        self.d_tab_browse_frame_lineEdit.setStatusTip(_translate("MainWindow", "Datei Pfad"))
        self.d_tab_browse_frame_button.setStatusTip(_translate("MainWindow", "Browse Button"))
        self.d_tab_browse_frame_button.setText(_translate("MainWindow", "Browse"))
        self.d_tab_data_import_button.setStatusTip(_translate("MainWindow", "Importiere Datei"))
        self.d_tab_data_import_button.setText(_translate("MainWindow", "Importiere Datei"))
        self.d_tab_plot_button.setStatusTip(_translate("MainWindow", "Plote Spike Trains"))
        self.d_tab_plot_button.setText(_translate("MainWindow", "Plote Spike Trains"))
        self.tab.setTabText(self.tab.indexOf(self.d_tab), _translate("MainWindow", "Datenimport"))
        self.sta_tab_tab.setStatusTip(_translate("MainWindow", "Spike Train Analyse Tab"))
        self.sta_tab_matlab_tab_feature_comboBox.setStatusTip(_translate("MainWindow", "Feature"))
        self.sta_tab_matlab_tab_feature_label.setStatusTip(_translate("MainWindow", "Feature"))
        self.sta_tab_matlab_tab_feature_label.setText(_translate("MainWindow", "Feature:"))
        self.sta_tab_matlab_tab_feature_calc_button.setStatusTip(_translate("MainWindow", "Feature berechnen"))
        self.sta_tab_matlab_tab_feature_calc_button.setText(_translate("MainWindow", "Berechnen"))
        self.sta_tab_matlab_tab_auto_calc_label.setStatusTip(_translate("MainWindow", "Ausgabeformat"))
        self.sta_tab_matlab_tab_auto_calc_label.setText(_translate("MainWindow", "Ausgabeformat:"))
        self.sta_tab_matlab_tab_auto_calc_comboBox.setStatusTip(_translate("MainWindow", "Ausgabeformat"))
        self.sta_tab_matlab_tab_auto_calc_button.setStatusTip(_translate("MainWindow", "Automatisierte Berechnung durchf??hren"))
        self.sta_tab_matlab_tab_auto_calc_button.setText(_translate("MainWindow", "Automatisierte Berechnung"))
        self.sta_tab_tab.setTabText(self.sta_tab_tab.indexOf(self.sta_tab_matlab_tab), _translate("MainWindow", "MatLab"))
        self.sta_tab_elephant_tab_feature_comboBox.setStatusTip(_translate("MainWindow", "Feature"))
        self.sta_tab_elephant_tab_feature_label.setStatusTip(_translate("MainWindow", "Feature"))
        self.sta_tab_elephant_tab_feature_label.setText(_translate("MainWindow", "Feature:"))
        self.sta_tab_elephant_tab_auto_calc_button.setStatusTip(_translate("MainWindow", "Automatisierte Berechnung durchf??hren"))
        self.sta_tab_elephant_tab_auto_calc_button.setText(_translate("MainWindow", "Automatisierte Berechnung"))
        self.sta_tab_elephant_tab_feature_calc_button.setStatusTip(_translate("MainWindow", "Feature berechnen"))
        self.sta_tab_elephant_tab_feature_calc_button.setText(_translate("MainWindow", "Berechnen"))
        self.sta_tab_elephant_tab_auto_calc_comboBox.setStatusTip(_translate("MainWindow", "Ausgabeformat"))
        self.sta_tab_elephant_tab_auto_calc_label.setStatusTip(_translate("MainWindow", "Ausgabeformat"))
        self.sta_tab_elephant_tab_auto_calc_label.setText(_translate("MainWindow", "Ausgabeformat:"))
        self.sta_tab_tab.setTabText(self.sta_tab_tab.indexOf(self.sta_tab_elephant_tab), _translate("MainWindow", "Elephant"))
        self.sta_tab_astak_tab_feature_calc_button.setStatusTip(_translate("MainWindow", "Feature berechnen"))
        self.sta_tab_astak_tab_feature_calc_button.setText(_translate("MainWindow", "Berechnen"))
        self.sta_tab_astak_tab_auto_calc_button.setStatusTip(_translate("MainWindow", "Automatisierte Berechnung durchf??hren"))
        self.sta_tab_astak_tab_auto_calc_button.setText(_translate("MainWindow", "Automatisierte Berechnung"))
        self.sta_tab_astak_tab_auto_calc_label.setStatusTip(_translate("MainWindow", "Ausgabeformat"))
        self.sta_tab_astak_tab_auto_calc_label.setText(_translate("MainWindow", "Ausgabeformat:"))
        self.sta_tab_astak_tab_feature_comboBox.setStatusTip(_translate("MainWindow", "Feature"))
        self.sta_tab_astak_tab_feature_label.setStatusTip(_translate("MainWindow", "Feature"))
        self.sta_tab_astak_tab_feature_label.setText(_translate("MainWindow", "Feature:"))
        self.sta_tab_astak_tab_auto_calc_comboBox.setStatusTip(_translate("MainWindow", "Ausgabeformat"))
        self.sta_tab_tab.setTabText(self.sta_tab_tab.indexOf(self.sta_tab_astak_tab), _translate("MainWindow", "A-Stak"))
        self.tab.setTabText(self.tab.indexOf(self.sta_tab), _translate("MainWindow", "Spike Train Analyse"))
        self.p_tab_plot_ST_button.setStatusTip(_translate("MainWindow", "Spike Trains plotten"))
        self.p_tab_plot_ST_button.setText(_translate("MainWindow", "Plotte Spike Trains"))
        self.p_tab_plot_feature_button.setStatusTip(_translate("MainWindow", "Feature Plotten"))
        self.p_tab_plot_feature_button.setText(_translate("MainWindow", "Plotte Feature"))
        self.p_tab_plot_feature_label.setStatusTip(_translate("MainWindow", "Feature"))
        self.p_tab_plot_feature_label.setText(_translate("MainWindow", "Feature:"))
        self.p_tab_plot_feature_comboBox.setStatusTip(_translate("MainWindow", "Feature w??hlen"))
        self.tab.setTabText(self.tab.indexOf(self.p_tab), _translate("MainWindow", "Plot"))
        self.MainTextBrowser.setStatusTip(_translate("MainWindow", "Ausgabe Feld"))
        self.plot_frame.setStatusTip(_translate("MainWindow", "Plot Feld"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
