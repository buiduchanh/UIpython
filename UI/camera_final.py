# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera_final.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from multiprocessing import Queue
from multiprocessing.dummy import Pool as ThreadPool

from threading import Thread
# from image_result import Ui_ImageCar
from UI.result_final import Ui_Demo_Result
from PIL import Image
from PIL.ImageQt import ImageQt
class Ui_Camera(object):
    def openResultCamera(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Demo_Result()
        self.ui.setupUi(self.window, self.image)
        self.window.show()

    def convert(self,img):

        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        # r, g, b, a = qImg.split()
        # qImg = Image.merge("RGBA", (b, g, r, a))
        return qImg

    def openCamera(self):
        # Videopath = '/media/buiduchanh/Work/SUBARU_1.mov'
        image ={}
        self.capturing = True
        self.cap = cv2.VideoCapture(0)
        # QApplication.processEvents()
        while self.capturing:
            _, frame = self.cap.read()
            image["img"] = frame
            if self.ImageQueue.qsize() < 10:
                self.ImageQueue.put(image)
            else:
                print(self.ImageQueue.qsize())

    def updateimage(self):
        if not self.ImageQueue.empty():
            frame = self.ImageQueue.get()
            img = frame["img"]
            data = self.convert(img)
            # _image = QPixmap(data).scaled(601, 341)
            _image = QtGui.QPixmap.fromImage(data).scaled(811, 501)

            self.setImage(_image)

    def setImage(self, _image):
        self.image = _image
        self.display(self.image)

    def display(self,frame):

        self.scene.addPixmap(frame)
        self.graphicsView.setScene(self.scene)

            # _,frame = self.cap.read()
            # self.graphicsView.update():


    def startcamera(self):

        self.ThreadGetImage = Thread(target=self.openCamera)
        self.ThreadGetImage.start()

    def setupUi(self, Camera):
        self.image = None
        self.ImageQueue = Queue()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateimage)
        self.timer.start(1)

        self.scene = QGraphicsScene()

        Camera.setObjectName("Camera")
        Camera.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(Camera)
        self.centralwidget.setObjectName("centralwidget")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(-5, 1, 811, 501))
        self.graphicsView.setObjectName("graphicsView")


        # self.Livecamera = QtWidgets.QPushButton(self.centralwidget)
        # self.Livecamera.setGeometry(QtCore.QRect(180, 520, 99, 27))
        # self.Livecamera.setObjectName("Livecamera")

        self.Capture = QtWidgets.QPushButton(self.centralwidget)
        self.Capture.setGeometry(QtCore.QRect(330, 520, 99, 27))
        self.Capture.setObjectName("Capture")
        Camera.setCentralWidget(self.centralwidget)

        self.Capture.clicked.connect(self.openResultCamera)

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
        # self.Livecamera.setText(_translate("Camera", "Live Camera"))
        self.Capture.setText(_translate("Camera", "Capture"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Camera = QtWidgets.QMainWindow()
    ui = Ui_Camera()
    ui.setupUi(Camera)
    Camera.show()
    sys.exit(app.exec_())

