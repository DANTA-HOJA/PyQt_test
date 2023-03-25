from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog

from day10.day10_UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()


    def setup_control(self):
        # TODO
        self.ui.file_Button.clicked.connect(self.buttonClicked_file)
        self.ui.folder_Button.clicked.connect(self.buttonClicked_folder)
    
    # Object Function
    def buttonClicked_file(self):
        file_path, file_type = QFileDialog.getOpenFileName(self, "Open file", "./")
        print(file_path, file_type)
        self.ui.file_lineEdit.setText(file_path)
        
    def buttonClicked_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Open folder", "./")
        print(folder_path)
        self.ui.folder_lineEdit.setText(folder_path)