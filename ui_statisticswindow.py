# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statisticswindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StatisticsWindow(object):
    def setupUi(self, StatisticsWindow):
        StatisticsWindow.setObjectName("StatisticsWindow")
        StatisticsWindow.resize(1068, 658)
        self.centralwidget = QtWidgets.QWidget(StatisticsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 90, 601, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_piechar = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_piechar.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_piechar.setObjectName("gridLayout_piechar")
        StatisticsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StatisticsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 28))
        self.menubar.setObjectName("menubar")
        StatisticsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StatisticsWindow)
        self.statusbar.setObjectName("statusbar")
        StatisticsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StatisticsWindow)
        QtCore.QMetaObject.connectSlotsByName(StatisticsWindow)

    def retranslateUi(self, StatisticsWindow):
        _translate = QtCore.QCoreApplication.translate
        StatisticsWindow.setWindowTitle(_translate("StatisticsWindow", "MainWindow"))

