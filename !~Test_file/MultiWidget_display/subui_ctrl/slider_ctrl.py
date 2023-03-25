from PyQt5 import QtWidgets, QtGui, QtCore
import PyQt5
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap

import cv2

from ui.slider_Form import Ui_Form # QtWidgets.QWidget
# from MultiWidget_test.slider_test import Ui_Dialog # QtWidgets.QDialog


class slider_Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # TODO
        self.ui.horizontalSlider.valueChanged.connect(self.getslidervalue)
        
        
    # Object Function
    def getslidervalue(self):        
        self.ui.label.setText(f"{self.ui.horizontalSlider.value()}")
        print(self.ui.horizontalSlider.value())
        