from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap

import cv2

from day12.day12_UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()


    def setup_control(self):
        # TODO
        self.ui.img_Button.clicked.connect(self.buttonClicked_loadImg)
        self.ui.zoomInButton.clicked.connect(self.buttonClicked_zoom_in)
        self.ui.zoomInButton.setEnabled(False)
        self.ui.zoomOutButton.clicked.connect(self.buttonClicked_zoom_out)
        self.ui.zoomOutButton.setEnabled(False)
        
            
    # Object Function
    def buttonClicked_loadImg(self):
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
            self.qpixmap = QPixmap.fromImage(self.qimg)
            self.qpixmap_height = self.qpixmap.height()
            self.ui.label_img.setPixmap(QPixmap.fromImage(self.qimg))

            self.ui.zoomInButton.setEnabled(True)
            self.ui.zoomOutButton.setEnabled(True)
            
        except Exception as e:
            print(e)
    
    def buttonClicked_zoom_out(self):
        self.qpixmap_height -= 100 # 調小 pixmap 高度 => scaledToHeight() = 拉小照片，放回固定大小的 window 看起來就是 縮小
        self.resize_image()

    def buttonClicked_zoom_in(self):
        self.qpixmap_height += 100 # 調大 pixmap 高度 => scaledToHeight() = 拉大照片，放回固定大小的 window 看起來就是 放大
        self.resize_image()

    def resize_image(self):
        scaled_pixmap = self.qpixmap.scaledToHeight(self.qpixmap_height)
        self.ui.label_img.setPixmap(scaled_pixmap)
        