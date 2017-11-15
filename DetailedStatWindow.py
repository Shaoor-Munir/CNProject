import json
import operator
from collections import OrderedDict

import numpy as np
import pyshark
from PyQt5 import QtWidgets, QtCore
from ui_detailedstatwindow import  Ui_DetailedStatWindow
import matplotlib.pyplot as plt

class DetailedStatWindowClass(QtWidgets.QMainWindow, Ui_DetailedStatWindow):

    sorted_results = None
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("background:white")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setFixedSize(self.size())
        self.pushButton_piechart.clicked.connect(self.show_pie_chart)
        self.pushButton_bargraph.clicked.connect(self.show_bar_chart)
        self.pushButton_bargraph.setStyleSheet("background:lightgrey")
        self.pushButton_piechart.setStyleSheet("background:lightgrey")


        results = list()
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

                    if pkt.transport_layer and 'ip' in pkt:
                        dport_number = pkt[pkt.transport_layer].dstport
                        sport_number = pkt[pkt.transport_layer].srcport
                        print("Destination port number is: %s and Source port number is: %s" % (
                            dport_number, sport_number))

                        if dport_number in ports and "Official" in ports[dport_number][0]["status"]:
                            print("Description: %s" % ports[dport_number][0]["description"])
                            results.append(ports[dport_number][0]["description"])
                        elif sport_number in ports and "Official" in ports[sport_number][0]["status"]:
                            print("Description: %s" % ports[sport_number][0]["description"])
                            results.append(ports[sport_number][0]["description"])
                        else:
                            print("The packet cannot be classified")
                            results.append("Unclassified")
                    else:
                        results.append("Unclassified")
        #print(results)
        counts = dict()

        for r in results:
            counts[r] = counts.get(r, 0) + 1

       # print(counts)
        sorted_counts = sorted(counts.items(), key=operator.itemgetter(0), reverse=True)
      #  print (sorted_counts)


        global sorted_results
        sorted_results = OrderedDict()
        for i in sorted_counts:
            sorted_results[i[0]] = int(i[1])

        #print(sorted_results)

        self.stats_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.stats_table.horizontalHeader().setStretchLastSection(True);

        families = sorted_results.values()

        self.label_totalpackets.setText("Total packets captured: %d" %len(results))

        total = sum(families)

        for key, value in sorted_results.items():
            self.stats_table.insertRow(self.stats_table.rowCount())
            self.stats_table.setItem(self.stats_table.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(key))
            self.stats_table.setItem(self.stats_table.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(str(value)))
            message = "{}%".format(round(value/total*100, 2))
            self.stats_table.setItem(self.stats_table.rowCount() - 1, 2, QtWidgets.QTableWidgetItem(message))

        self.stats_table.resizeColumnsToContents()
        self.show()

    def show_pie_chart(self):
        global sorted_results
        # Data to plot
        labels = list(sorted_results.keys() )
        cmap = plt.get_cmap('viridis')
        colors = cmap(np.linspace(0, 1, len(labels)))
        sizes = list(sorted_results.values())
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best",)
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    def show_bar_chart(self):
        global sorted_results
        # Data to plot
        labels = list(sorted_results.keys())
        x_axis = np.arange(len(labels))
        cmap = plt.get_cmap('viridis')
        colors = cmap(np.linspace(0, 1, len(labels)))
        sizes = list(sorted_results.values())
        patches = plt.bar(x_axis, sizes, align='center', alpha=0.5, color = colors)
        plt.legend(patches, labels, loc="best",)
        #plt.xticks(y_axis, labels)
        for a, b in zip(x_axis, sizes):
            plt.text(a, b, str(b))

        plt.tight_layout()
        plt.show()
