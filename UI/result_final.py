# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result_final.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from processing_image import processing

class Ui_Demo_Result(object):
    def setupUi(self, Demo_Result, model, nameimage):
    # def setupUi(self, Demo_Result, nameimage):
        self.fname = nameimage
        w = 801
        h = 561
        self.scene = QGraphicsScene()


        top5acr = processing( model, nameimage)


        Demo_Result.setObjectName("Demo_Result")
        Demo_Result.resize(797, 600)

        self.centralwidget = QtWidgets.QWidget(Demo_Result)
        self.centralwidget.setObjectName("centralwidget")

        self.Result = QtWidgets.QGraphicsView(self.centralwidget)
        self.Result.setGeometry(QtCore.QRect(0, 0, 801, 561))
        self.Result.setObjectName("Result")

        nameimage = QPixmap(self.fname).scaled(w, h)
        self.scene.addPixmap(nameimage)
        self.Result.setScene(self.scene)

        self.Accuracy = QtWidgets.QTextBrowser(self.centralwidget)
        self.Accuracy.setGeometry(QtCore.QRect(0, 0, 231, 111))
        self.Accuracy.setObjectName("Accuracy")
        Demo_Result.setCentralWidget(self.centralwidget)

        self.Accuracy.append(top5acr)

        self.menubar = QtWidgets.QMenuBar(Demo_Result)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 25))
        self.menubar.setObjectName("menubar")
        Demo_Result.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(Demo_Result)
        self.statusbar.setObjectName("statusbar")
        Demo_Result.setStatusBar(self.statusbar)

        self.retranslateUi(Demo_Result)
        QtCore.QMetaObject.connectSlotsByName(Demo_Result)

    def retranslateUi(self, Demo_Result):
        _translate = QtCore.QCoreApplication.translate
        Demo_Result.setWindowTitle(_translate("Demo_Result", "Result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Demo_Result = QtWidgets.QMainWindow()
    ui = Ui_Demo_Result()
    ui.setupUi(Demo_Result)
    Demo_Result.show()
    sys.exit(app.exec_())

