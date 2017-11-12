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

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_event)
        self.timer.start(10)

        global time_elapsed
        time_elapsed = 0
        global sp

        sp = subprocess.Popen(['tcpdump', '-w', 'output.pcap'], shell=False)

        self.pushButton_stop.clicked.connect(self.exit_pressed)
        self.show()

    def update_event(self):

        global time_elapsed

        time_elapsed += 1

        self.timer_label.setText("Time elapsed: %d millsecond" % time_elapsed)

    def exit_pressed(self):

        global sp

        sp.terminate()
        self.timer.stop()

        f = open("output.pcap", "rb")

        if f.closed:
            print('There has been some error in opening the output file.')
        else:
            print("The output file was openend successfuly")
            pcap = pyshark.FileCapture('output.pcap')

            json_file = open("ports.lists.json")
            if json_file.closed:
                print("Error in opening the JSON file.")
            else:
                ports = json.load(json_file)
                for pkt in pcap:

                    if pkt.transport_layer:
                        dport_number = pkt[pkt.transport_layer].dstport
                        sport_number = pkt[pkt.transport_layer].srcport
                        print("Destination port number is: %s and Source port number is: %s" % (
                        dport_number, sport_number))

                        if dport_number in ports and ports[dport_number][0]["status"] == "Official":
                            print("Description: %s" % ports[dport_number][0]["description"])
                        elif sport_number in ports and ports[sport_number][0]["status"] == "Official":
                            print("Description: %s" % ports[sport_number][0]["description"])
                        else:
                            print("The packet cannot be classified")

        print("exit pressed")
