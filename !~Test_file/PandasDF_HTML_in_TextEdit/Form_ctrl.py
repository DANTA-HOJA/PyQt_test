from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QProcess, pyqtSignal

import os
import sys

import re
import glob
import json

import pandas as pd

import cv2

from showDf_HTML import Ui_MainWindow # QtWidgets.QWidget


class Df_in_HTML_Form(QMainWindow):
    
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # TODO
        pass
        # sub widget connection
        
        
        # variable
        self.file_path = None
        
        
        # signal/slot
        self.ui.openFileButton.clicked.connect(self.openFile)
        self.ui.showButton.clicked.connect(self.showInHTML)
        
        
        # view
        
        
        
    # Object Function
    def openFile(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Open file", directory="./show_log")
        print(self.file_path)
        self.ui.fileLineEdit.setText(self.file_path)
    
    
    def showInHTML(self):
        with open(self.file_path, "r") as f:
            info = json.load(f)
        df = pd.DataFrame(info)
        # print(df)
        
        df_HTML = df.to_html()
        print(df_HTML)
        
        self.ui.textEdit.append(df_HTML)
        