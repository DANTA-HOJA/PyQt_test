from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap

import cv2

from day11.day11_UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()


    def setup_control(self):
        # TODO
        self.ui.img_Button.clicked.connect(self.buttonClicked_img)
            
    # Object Function
    def buttonClicked_img(self):
        img_path, search_type = QFileDialog.getOpenFileName(self, "Select Image", "C:/Users/User/Desktop")
        
        try:
            print(img_path, search_type)
            self.ui.img_lineEdit.setText(img_path)
            
            self.img = cv2.imread(img_path)
            height, width, channel = self.img.shape
            print(f"Image Size = {width} x {height}")
            Size = (int(width/3), int(height/3))
            self.img = cv2.resize(self.img, dsize=Size)

            bytesPerline = 3 * Size[0]
            self.qimg = QImage(self.img, Size[0], Size[1], bytesPerline, QImage.Format_RGB888).rgbSwapped()
            self.ui.label_img.setPixmap(QPixmap.fromImage(self.qimg))
            self.ui.label_img.adjustSize()

        except Exception as e:
            print(e)
        
        