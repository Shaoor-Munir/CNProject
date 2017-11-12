import json
import random

import pyshark
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsEllipseItem, QGraphicsView

from ui_statisticswindow import Ui_StatisticsWindow

class StatisticsWindowClass(QtWidgets.QMainWindow, Ui_StatisticsWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)


        scene = QGraphicsScene()

        families = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        total = 0
        set_angle = 0
        count1 = 0
        colours = []
        total = sum(families)

        for count in range(len(families)):
            number = []
            for count in range(3):
                number.append(random.randrange(0, 255))
            colours.append(QColor(number[0], number[1], number[2]))

        for family in families:
            # Max span is 5760, so we have to calculate corresponding span angle
            angle = round(float(family * 5760) / total)
            ellipse = QGraphicsEllipseItem(0, 0, 400, 400)
            ellipse.setPos(0, 0)
            ellipse.setStartAngle(set_angle)
            ellipse.setSpanAngle(angle)
            ellipse.setBrush(colours[count1])
            set_angle += angle
            count1 += 1
            scene.addItem(ellipse)

        self.view = QGraphicsView(scene)
        self.view.setStyleSheet("background:transparent")
        self.gridLayout_piechar.addWidget(self.view)
        self.show()