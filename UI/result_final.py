# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result_final.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
sys.path.insert(0, '/home/nvidia/hanh_demo/UIpython/recognition/')
# sys.path.insert(0, '/home/buiduchanh/WorkSpace/demo_jestson/recognition/')
import cv2
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from processing import get_model

class Ui_Demo_Result(object):

    def convert_img(self,img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        # r, g, b, a = qImg.split()
        # qImg = Image.merge("RGBA", (b, g, r, a))
        return qImg


    def setupUi(self, Demo_Result, nameimage):
    # def setupUi(self, Demo_Result, nameimage):
        self.fname = nameimage
        # w = 801
        # h = 561
        self.scene = QGraphicsScene()
        print(type(nameimage))

        results = get_model(nameimage)

        Demo_Result.setObjectName("Demo_Result")
        Demo_Result.resize(797, 600)

        self.centralwidget = QtWidgets.QWidget(Demo_Result)
        self.centralwidget.setObjectName("centralwidget")

        self.Result = QtWidgets.QGraphicsView(self.centralwidget)
        self.Result.setGeometry(QtCore.QRect(0, 0, 801, 561))
        self.Result.setObjectName("Result")

        img = self.convert_img(nameimage)
        _image = QtGui.QPixmap.fromImage(img).scaled(801, 561)
        self.scene.addPixmap(_image)
        self.Result.setScene(self.scene)


        self.Accuracy = QtWidgets.QTextBrowser(self.centralwidget)
        self.Accuracy.setGeometry(QtCore.QRect(0, 0, 235, 95))
        # self.Accuracy.setGeometry(QtCore.QRect(0, 0, 271, 31))
        self.Accuracy.setObjectName("Accuracy")
        Demo_Result.setCentralWidget(self.centralwidget)
        self.Accuracy.append("{}\n{}\n{}".format(''.join(results[0]),''.join(results[1]),''.join(results[2])))

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

