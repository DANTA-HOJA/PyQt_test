from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap

import cv2

from ui.MainWindow import Ui_MainWindow

# Sub Widget/Window
from subui_ctrl.slider_ctrl import slider_Form


class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Zebra Fish")
        self.sub_widget = slider_Form()
        self.sub_widget2 = slider_Form()
        self.setup_control()


    def setup_control(self):
        # TODO
        self.ui.gridLayout_4.addWidget(self.sub_widget)
        self.ui.label.setText("Tab1_label")
        
        self.ui.pushButton.clicked.connect(self.buttonClicked)
        
        self.ui.pushButton_4.setText("Switch Tab")
        self.ui.pushButton_4.clicked.connect(self.switch_tab)
        
        self.ui.pushButton_2.setText("Show\n\nsubwidget2")
        self.sub_widget2_show_status = False
        self.ui.pushButton_2.clicked.connect(self.show_subwidget2)
        
        self.ui.tabWidget.setCurrentIndex(0)
        
        
    # Object Function
    def buttonClicked(self):        
        self.ui.textEdit.setText("Hello World!")
        # print(self.ui.tabWidget.currentIndex())
        self.ui.tabWidget.setCurrentIndex(1)
        print('Switch to "Tab 2"')


    def switch_tab(self):
        
        self.tab_display_info = {0: 'Switch to "Tab 1"', 1: 'Switch to "Tab 2"'}
        
        print(self.tab_display_info[(self.ui.tabWidget.currentIndex()+1)%2])
        self.ui.tabWidget.setCurrentIndex((self.ui.tabWidget.currentIndex()+1)%2)

    
    def show_subwidget2(self):
        if self.sub_widget2_show_status: 
            self.sub_widget2.hide()
            self.sub_widget2_show_status = False
            self.ui.pushButton_2.setText("Show\n\nsubwidget2")
        else: 
            self.sub_widget2.show()
            self.sub_widget2_show_status = True
            self.ui.pushButton_2.setText("Hide\n\nsubwidget2")