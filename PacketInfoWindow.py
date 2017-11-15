import json

import pyshark
from PyQt5 import QtWidgets, QtCore, QtGui

from ui_packetinfowindow import Ui_PacketInfoWindow

from DetailedStatWindow import  DetailedStatWindowClass


class PacketInfoWindowClass(QtWidgets.QMainWindow, Ui_PacketInfoWindow):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background:white")
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setFixedSize(self.size())
        self.packetTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.packetTable.horizontalHeader().setStretchLastSection(True);

        self.pushButton_stats.clicked.connect(self.stat_clicked)
        self.pushButton_stats.setStyleSheet("background:lightgrey")

        # self.packetTable.resizeColumnsToContents()

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

                    if 'ip' in pkt and pkt.transport_layer:
                        self.packetTable.insertRow(self.packetTable.rowCount())
                        dport_number = pkt[pkt.transport_layer].dstport
                        sport_number = pkt[pkt.transport_layer].srcport

                        self.packetTable.setItem(self.packetTable.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(
                            "%s:%s" % (pkt.ip.src, pkt[pkt.transport_layer].srcport)))
                        self.packetTable.setItem(self.packetTable.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(
                            "%s:%s" % (pkt.ip.dst, pkt[pkt.transport_layer].dstport)))

                        print("Destination port number is: %s and Source port number is: %s" % (
                            dport_number, sport_number))

                        if dport_number in ports and "Official" in ports[dport_number][0]["status"]:
                            self.packetTable.setItem(self.packetTable.rowCount() - 1, 2,
                                                     QtWidgets.QTableWidgetItem(ports[dport_number][0]["description"]))
                            self.packetTable.item(self.packetTable.rowCount() - 1, 1).setBackground(
                                QtGui.QColor("lightgreen"))
                        elif sport_number in ports and "Official" in ports[sport_number][0]["status"]:
                            print("Description: %s" % ports[sport_number][0]["description"])
                            self.packetTable.setItem(self.packetTable.rowCount() - 1, 2,
                                                     QtWidgets.QTableWidgetItem(ports[sport_number][0]["description"]))
                            self.packetTable.item(self.packetTable.rowCount() - 1, 0).setBackground(
                                QtGui.QColor("lightgreen"))
                        else:
                            print("The packet cannot be classified")
                            self.packetTable.setItem(self.packetTable.rowCount() - 1, 2,
                                                     QtWidgets.QTableWidgetItem("Unclassified"))
                            self.packetTable.item(self.packetTable.rowCount() - 1, 2).setBackground(QtGui.QColor("red"))

        self.packetTable.resizeColumnsToContents()
        self.show()


    def stat_clicked(self):
        self.detailedstatwindow = DetailedStatWindowClass()