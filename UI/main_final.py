# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_final.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from camera_final import Ui_Camera
from result_final import Ui_Demo_Result

from custom_layers.scale_layer import Scale
from keras.optimizers import Nadam
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from time import sleep
# model = None

# model = load_model('/home/buiduchanh/WorkSpace/demo_jestson/model/weights.21-0.88502994.hdf5',
#                        custom_objects={"Scale": Scale})
# nadam = Nadam(lr=1e-06, beta_1=0.9, beta_2=0.999, epsilon=1e-08, schedule_decay=0.004)
# model.compile(optimizer=nadam, loss='categorical_crossentropy', metrics=['accuracy'])
class Ui_Demo_ACR(object):
    def __init__(self):
        self.ui = None
        self.model = load_model('/home/buiduchanh/WorkSpace/demo_jestson/model/weights.21-0.88502994.hdf5',
                               custom_objects={"Scale": Scale})
        self.nadam = Nadam(lr=1e-06, beta_1=0.9, beta_2=0.999, epsilon=1e-08, schedule_decay=0.004)
        self.model.compile(optimizer=self.nadam, loss='categorical_crossentropy', metrics=['accuracy'])


    def openCamera(self):
        self.window = QtWidgets.QMainWindow()
        # if self.ui is not None:
        #     print("have")
        #     self.ui.close()
        #     sleep(1)
        #     sys.exit(app.exec_())
        # else:
        self.ui = Ui_Camera(self.model)

        # self.ui = Ui_Camera()
        self.ui.setupUi(self.window )
        self.window.show()
        self.ui.startcamera()

    def openImage(self):
        w = 751
        h = 331
        self.fname, _ = QFileDialog.getOpenFileName(None, "Open file",
                                                    # "", "Image files (*.mov)")
                                                    "", "All files (*.jpg *.gif *.mov)")

        self.window = QtWidgets.QMainWindow()
        self.uiim = Ui_Demo_Result()
        self.uiim.setupUi(self.window, self.model, self.fname)
        self.window.show()

    def setupUi(self, Demo_ACR):



        Demo_ACR.setObjectName("Demo_ACR")
        Demo_ACR.resize(300, 179)

        self.centralwidget = QtWidgets.QWidget(Demo_ACR)
        self.centralwidget.setObjectName("centralwidget")

        self.Image = QtWidgets.QPushButton(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(30, 50, 99, 61))
        self.Image.setObjectName("Image")

        self.Image.clicked.connect(self.openImage)

        self.Camera = QtWidgets.QPushButton(self.centralwidget)
        self.Camera.setGeometry(QtCore.QRect(170, 50, 99, 61))
        self.Camera.setObjectName("Camera")

        self.Camera.clicked.connect(self.openCamera)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 91, 17))
        self.label.setObjectName("label")
        Demo_ACR.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(Demo_ACR)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 25))
        self.menubar.setObjectName("menubar")
        Demo_ACR.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(Demo_ACR)
        self.statusbar.setObjectName("statusbar")
        Demo_ACR.setStatusBar(self.statusbar)

        self.retranslateUi(Demo_ACR)
        QtCore.QMetaObject.connectSlotsByName(Demo_ACR)

    def retranslateUi(self, Demo_ACR):
        _translate = QtCore.QCoreApplication.translate
        Demo_ACR.setWindowTitle(_translate("Demo_ACR", "ACR-DEMO"))
        self.Image.setText(_translate("Demo_ACR", "Image"))
        self.Camera.setText(_translate("Demo_ACR", "Camera"))
        self.label.setText(_translate("Demo_ACR", "ACR-DEMO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Demo_ACR = QtWidgets.QMainWindow()
    ui = Ui_Demo_ACR()
    ui.setupUi(Demo_ACR)
    Demo_ACR.show()
    sys.exit(app.exec_())

