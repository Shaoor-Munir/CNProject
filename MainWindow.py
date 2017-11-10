import subprocess
import dpkt
import os

import pyshark
import time
from PyQt5 import QtWidgets, QtCore
from threading import Thread

from ui_mainwindow import Ui_MainWindow


class MainWindowClass(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        #connect buttons here

        self.pushButton_start.clicked.connect(self.start_pressed)
        self.pushButton_stop.clicked.connect(self.exit_pressed)

    sp = None

    def start_pressed(self):
        global sp

        sp = subprocess.Popen(['tcpdump', '-w', 'output.pcap'], shell = False )

    def exit_pressed(self):
        global  sp

        sp.terminate()

        f = open("output.pcap", "rb")

        if f.closed:
            print('There has been some error in opening the output file.')
        else:
            print("The output file was openend successfuly")
            #pcap = savefile.load_savefile(f, verbose=True)
            pcap = pyshark.FileCapture('output.pcap')

            for pkt in pcap:
                print(pkt[pkt.transport_layer].dstport)
            #for ts, buf in pcap:
             #   eth = dpkt.ethernet.Ethernet(buf)
              #  ip = eth.data
               # tcp = ip.data
                #print("The tcp port is")
                #print(tcp.sport)
        print("exit pressed")
