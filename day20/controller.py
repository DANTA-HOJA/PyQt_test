from enum import Flag
from re import L
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSignal

import cv2
import time

from day20.day20_UI import Ui_MainWindow


class ThreadTask(QThread):
    task_processing = pyqtSignal(int)
    task_complete = pyqtSignal()
    statusBar_display = pyqtSignal(str, str)
    
    def __init__(self, name:str):
        super().__init__()
        self.name = name
    
    def run(self):
        max_value = 100
        
        # process
        self.statusBar_display.emit(self.name, "running")
        
        for i in range(max_value):
            time.sleep(0.01)
            self.task_processing.emit(i+1)
        
        self.statusBar_display.emit(self.name, "complete")
        self.task_complete.emit()
        

class statusBar_cleaner(QThread):
    
    msg_cleaner = pyqtSignal()
    
    def __init__(self, clean_time=1):
        super().__init__()
        self.clean_time = clean_time
        
    def run(self):
        time.sleep(self.clean_time)
        self.msg_cleaner.emit()
        print("statusBar cleaned")
            


class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.qthread = ThreadTask("progressBar")
        self.statusBar_cleaner = statusBar_cleaner(clean_time=2)
        
        self.setup_control()


    def setup_control(self):
        # TODO
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setMaximum(100)
        
        self.ui.pushButton.clicked.connect(self.ButtonClick)
        
        self.qthread.task_processing.connect(self.progress_changed)
        self.qthread.task_complete.connect(self.progress_completed)
        self.qthread.statusBar_display.connect(lambda name, status:self.ui.statusbar.showMessage(f"{name} is {status}."))
        
    
    # Object Function
    def ButtonClick(self):
        self.ui.pushButton.setEnabled(False)
        self.qthread.start()
    
    
    # progressBar
    def progress_changed(self, value):
        self.ui.progressBar.setValue(value)
        
    def progress_completed(self):
        self.ui.pushButton.setEnabled(True)
        
        self.statusBar_cleaner = statusBar_cleaner(clean_time=2)
        self.statusBar_cleaner.msg_cleaner.connect(lambda: self.ui.statusbar.clearMessage())
        self.statusBar_cleaner.start()
        