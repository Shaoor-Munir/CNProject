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
        PacketInfoWindow.resize(800, 600)
        self.menubar = QtWidgets.QMenuBar(PacketInfoWindow)
        self.menubar.setObjectName("menubar")
        PacketInfoWindow.setMenuBar(self.menubar)
        self.centralwidget = QtWidgets.QWidget(PacketInfoWindow)
        self.centralwidget.setObjectName("centralwidget")
        PacketInfoWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PacketInfoWindow)
        self.statusbar.setObjectName("statusbar")
        PacketInfoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PacketInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(PacketInfoWindow)

    def retranslateUi(self, PacketInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        PacketInfoWindow.setWindowTitle(_translate("PacketInfoWindow", "MainWindow"))

