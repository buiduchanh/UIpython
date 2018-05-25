# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera_final.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, Qt

import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from multiprocessing import Queue
from threading import Thread
from result_final import Ui_Demo_Result

class Ui_Camera(object):
    # def __init__(self):
    def __init__(self):
        self.flag = True

    def openResultCamera(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Demo_Result()
        self.ui.setupUi(self.window, self.imageprocesing)
        # self.ui.setupUi(self.window, self.image)
        self.window.show()

    def convert(self,img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        return qImg

    def close_application(self):

        self.capturing = False
        self.timer.stop()
        print("stop")
        QCloseEvent()



    def openCamera(self):
        print("extract image")
        image ={}
        self.capturing = True
        self.cap = cv2.VideoCapture("nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)1280, height=(int)720,format=(string)I420, framerate=(fraction)30/1 ! nvvidconv flip-method=2 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink")
        # self.cap = cv2.VideoCapture(0)
        while self.capturing:
            # print("camera")
            _, frame = self.cap.read()
            image["img"] = frame
            if self.ImageQueue.qsize() < 10:
                self.ImageQueue.put(image)

    def updateimage(self):
        print("update_image")
        print("qsize",self.ImageQueue.qsize())
        if self.ImageQueue.qsize() > 0:
            frame = self.ImageQueue.get()
            # if self.flag == True:
            #
            if frame:

                img = frame["img"]
                self.imageprocesing = img
                data = self.convert(img)
                _image = QtGui.QPixmap.fromImage(data).scaled(811, 501)

                self.setImage(_image)

    def setImage(self, _image):
        self.image = _image
        self.display(self.image)

    def display(self,frame):
        if frame is not None:
            print("display")
            self.scene.addPixmap(frame)
            self.graphicsView.setScene(self.scene)

    def startcamera(self):
        print("Thread get image start")

        self.ThreadGetImage = Thread(target=self.openCamera)
        self.ThreadGetImage.start()

    def setupUi(self, Camera):
        self.imageprocesing = None
        self.image = None
        self.ImageQueue = Queue()

        # if self.timer is None:
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateimage)
        self.timer.start(30)

        self.scene = QGraphicsScene()

        Camera.setObjectName("Camera")
        Camera.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(Camera)
        self.centralwidget.setObjectName("centralwidget")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(-5, 1, 811, 501))
        self.graphicsView.setObjectName("graphicsView")

        self.Capture = QtWidgets.QPushButton(self.centralwidget)
        self.Capture.setGeometry(QtCore.QRect(330, 520, 99, 27))
        self.Capture.setObjectName("Capture")
        Camera.setCentralWidget(self.centralwidget)

        self.Capture.clicked.connect(self.openResultCamera)
        # self.Capture.clicked.connect(self.close_application)

        self.menubar = QtWidgets.QMenuBar(Camera)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        Camera.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(Camera)
        self.statusbar.setObjectName("statusbar")
        Camera.setStatusBar(self.statusbar)

        self.retranslateUi(Camera)
        QtCore.QMetaObject.connectSlotsByName(Camera)

    def retranslateUi(self, Camera):
        _translate = QtCore.QCoreApplication.translate
        Camera.setWindowTitle(_translate("Camera", "Camera"))
        self.Capture.setText(_translate("Camera", "Capture"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Camera = QtWidgets.QMainWindow()

    ui = Ui_Camera()
    ui.setupUi(Camera)
    Camera.show()
    sys.exit(app.exec_())

