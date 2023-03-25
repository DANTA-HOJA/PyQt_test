from re import L
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSignal

import cv2
import time

from day19.day19_UI import Ui_MainWindow


class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()


    def setup_control(self):
        # TODO
        self.ui.progressBar.setValue(0)
        
        self.ui.pushButton.clicked.connect(self.start_progress)
        
        
    # Object Function
    def start_progress(self):
        self.ui.progressBar.setMaximum(100)
        
        for i in range(100):
            time.sleep(0.01)
            self.ui.progressBar.setValue(i+1)

        