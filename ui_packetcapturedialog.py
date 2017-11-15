# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'packetcapturedialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PacketCaptureDialog(object):
    def setupUi(self, PacketCaptureDialog):
        PacketCaptureDialog.setObjectName("PacketCaptureDialog")
        PacketCaptureDialog.resize(475, 227)
        self.verticalLayoutWidget = QtWidgets.QWidget(PacketCaptureDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 40, 371, 137))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.timer_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.timer_label.setFont(font)
        self.timer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.timer_label.setObjectName("timer_label")
        self.verticalLayout.addWidget(self.timer_label)
        self.pushButton_stop = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.verticalLayout.addWidget(self.pushButton_stop)

        self.retranslateUi(PacketCaptureDialog)
        QtCore.QMetaObject.connectSlotsByName(PacketCaptureDialog)

    def retranslateUi(self, PacketCaptureDialog):
        _translate = QtCore.QCoreApplication.translate
        PacketCaptureDialog.setWindowTitle(_translate("PacketCaptureDialog", "Capturing Packets"))
        self.label.setText(_translate("PacketCaptureDialog", "Capturing incoming and outgoing packets"))
        self.timer_label.setText(_translate("PacketCaptureDialog", "Time elapsed: 0 millsecond"))
        self.pushButton_stop.setText(_translate("PacketCaptureDialog", "Stop Capture"))

