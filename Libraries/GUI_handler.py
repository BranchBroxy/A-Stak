import os
from PyQt5.QtWidgets import QFileDialog

main_ui = object
drcell_path = ""
matlab_path = ""


def initial_start(ui):
    global main_ui
    main_ui = ui
    main_ui.d_tab.setEnabled(False)
    main_ui.sta_tab_tab.setEnabled(False)
    main_ui.p_tab.setEnabled(False)


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
    global main_ui
    main_ui = ui
    # TODO: requirements.txt und MatLabEngine automatisch installieren
    if drcell_path != "" and matlab_path != "":
        ui.MainTextBrowser.setText("DrCell Pfad und MatLab Pfad wurden festgelegt")
        main_ui.d_tab.setEnabled(True)
        main_ui.sta_tab_tab.setEnabled(True)
    else:
        ui.MainTextBrowser.setText("DrCell Pfad und MatLab Pfad konnten nicht festgelegt werden!")
