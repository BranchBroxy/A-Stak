import os
from PyQt5.QtWidgets import QFileDialog
from Libraries.Plotter import plotter_init

main_ui = object
drcell_path = ""
matlab_path = ""
drcell_matlab_flag = False


def initial_start(ui, MainWindow):
    global main_ui
    main_ui = ui
    main_ui.d_tab.setEnabled(True)
    main_ui.sta_tab_matlab_tab.setEnabled(False)
    main_ui.sta_tab_elephant_tab.setEnabled(False)
    main_ui.p_tab.setEnabled(False)
    main_ui.d_tab_plot_button.setEnabled(False)
    plotter_init(main_ui, MainWindow)


def get_drcell_path(ui):
    global drcell_path
    global main_ui
    main_ui = ui
    drcell_path = QFileDialog.getExistingDirectory()
    main_ui.v_tab_DrCellPath_lineEdit.setText(drcell_path)
    main_ui.v_tab_DrCellPath_lineEdit.setEnabled(False)


def get_matlab_path(ui):
    global matlab_path
    global main_ui
    main_ui = ui
    matlab_path = QFileDialog.getExistingDirectory()
    main_ui.v_tab_MatLabPath_lineEdit.setText(matlab_path)
    main_ui.v_tab_MatLabPath_lineEdit.setEnabled(False)

def install_libraries_and_unlock_tabs(ui):
    global drcell_matlab_flag
    global main_ui
    main_ui = ui
    # TODO: requirements.txt und MatLabEngine automatisch installieren
    if drcell_path != "" and matlab_path != "":
        ui.MainTextBrowser.setText("DrCell Pfad und MatLab Pfad wurden festgelegt")
        drcell_matlab_flag = True
        main_ui.sta_tab_matlab_tab.setEnabled(True)
    else:
        ui.MainTextBrowser.setText("DrCell Pfad und MatLab Pfad konnten nicht festgelegt werden!")


def check_drcell_matlab_flag(ui):
    global main_ui
    main_ui = ui
    main_ui.p_tab.setEnabled(True)
    main_ui.d_tab_plot_button.setEnabled(True)
    main_ui.sta_tab_elephant_tab.setEnabled(True)
    global drcell_matlab_flag
    if drcell_matlab_flag == True:
        main_ui.sta_tab_matlab_tab.setEnabled(True)
