import subprocess
from pathlib import Path

import pyshark
from PyQt5 import QtWidgets, QtCore
import json
from ui_mainwindow import Ui_MainWindow
from PacketCaptureDialog import PacketCaptureDialogClass
from PacketInfoWindow import PacketInfoWindowClass


class MainWindowClass(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("background:white")
        self.setFixedSize(self.size())
        my_file = Path("output.pcap")

        if my_file.is_file():
            self.pushButton_results.setEnabled(True)
        else:
            self.pushButton_results.setEnabled(False)
        self.show()
        # connect buttons here
        self.pushButton_start.clicked.connect(self.start_pressed)
        self.pushButton_start.setStyleSheet("background:lightgrey")
        self.pushButton_results.setStyleSheet("background:lightgrey")
        self.pushButton_results.clicked.connect(self.results_pressed)

    def start_pressed(self):

        self.dialog = PacketCaptureDialogClass()
        self.pushButton_results.setEnabled(True)

    def results_pressed(self):

        self.results = PacketInfoWindowClass()