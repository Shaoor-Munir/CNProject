import subprocess
import sys
import pyshark
from PyQt5 import QtWidgets, QtCore
import json

from ui_packetcapturedialog import Ui_PacketCaptureDialog


class PacketCaptureDialogClass(QtWidgets.QMainWindow, Ui_PacketCaptureDialog):
    sp = None
    time_elapsed = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setStyleSheet("background:white")
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_event)
        self.setFixedSize(self.size())
        self.timer.start(1000)

        global time_elapsed
        time_elapsed = 0
        global sp

        sp = subprocess.Popen(['tcpdump', '-w', 'output.pcap'], shell=False)

        self.pushButton_stop.clicked.connect(self.exit_pressed)
        self.pushButton_stop.setStyleSheet("background:lightgrey")
        self.show()

    def update_event(self):

        global time_elapsed

        time_elapsed += 1

        if time_elapsed is 1:
            self.timer_label.setText("Time elapsed: %d second" % time_elapsed)
        else:
            self.timer_label.setText("Time elapsed: %d seconds" % time_elapsed)

    def exit_pressed(self):

        global sp

        sp.terminate()
        self.timer.stop()

        self.close()

        print("exit pressed")
