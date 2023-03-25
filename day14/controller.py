from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap

import cv2

from day14.day14_UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()


    def setup_control(self):
        # TODO
        self.ui.horizontalSlider.valueChanged.connect(self.getslidervalue)
        
        
    # Object Function
    def getslidervalue(self):        
        self.ui.label.setText(f"{self.ui.horizontalSlider.value()}")
        print(self.ui.horizontalSlider.value())
        