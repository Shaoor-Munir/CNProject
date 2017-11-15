# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'packetinfowindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PacketInfoWindow(object):
    def setupUi(self, PacketInfoWindow):
        PacketInfoWindow.setObjectName("PacketInfoWindow")
        PacketInfoWindow.resize(1091, 712)
        self.centralwidget = QtWidgets.QWidget(PacketInfoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.packetTable = QtWidgets.QTableWidget(self.centralwidget)
        self.packetTable.setGeometry(QtCore.QRect(30, 60, 1021, 531))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.packetTable.setFont(font)
        self.packetTable.setObjectName("packetTable")
        self.packetTable.setColumnCount(3)
        self.packetTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.packetTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.packetTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.packetTable.setHorizontalHeaderItem(2, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 20, 591, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_stats = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stats.setGeometry(QtCore.QRect(460, 610, 171, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_stats.setFont(font)
        self.pushButton_stats.setObjectName("pushButton_stats")
        PacketInfoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PacketInfoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1091, 28))
        self.menubar.setObjectName("menubar")
        PacketInfoWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PacketInfoWindow)
        self.statusbar.setObjectName("statusbar")
        PacketInfoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PacketInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(PacketInfoWindow)

    def retranslateUi(self, PacketInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        PacketInfoWindow.setWindowTitle(_translate("PacketInfoWindow", "Packet Info"))
        item = self.packetTable.horizontalHeaderItem(0)
        item.setText(_translate("PacketInfoWindow", "Source IP"))
        item = self.packetTable.horizontalHeaderItem(1)
        item.setText(_translate("PacketInfoWindow", "Destination IP"))
        item = self.packetTable.horizontalHeaderItem(2)
        item.setText(_translate("PacketInfoWindow", "Classification"))
        self.label.setText(_translate("PacketInfoWindow", "All the packets captured and their classification"))
        self.pushButton_stats.setText(_translate("PacketInfoWindow", "View Stats"))

