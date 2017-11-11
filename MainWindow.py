import subprocess

import pyshark
from PyQt5 import QtWidgets, QtCore
import json
from ui_mainwindow import Ui_MainWindow
from PacketCaptureDialog import PacketCaptureDialogClass


class MainWindowClass(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # connect buttons here

        self.pushButton_start.clicked.connect(self.start_pressed)

    def start_pressed(self):

        self.dialog = PacketCaptureDialogClass()




