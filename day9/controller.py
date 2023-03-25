from PyQt5 import QtWidgets, QtGui, QtCore
from day9.day9_UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()


    def setup_control(self):
        # TODO
        self.ui.line_botton.clicked.connect(self.buttonClicked_line)
        self.ui.text_botton.clicked.connect(self.buttonClicked_text)
        self.ui.plainText_botton.clicked.connect(self.buttonClicked_plainText)
        
    def buttonClicked_line(self):
        msg = self.ui.lineEdit.text()
        self.ui.line_label.setText(msg)
        self.ui.line_label.adjustSize()
        
    def buttonClicked_text(self):
        msg = self.ui.textEdit.toPlainText()
        self.ui.text_label.setText(msg)
        self.ui.text_label.adjustSize()
        
    def buttonClicked_plainText(self):
        msg = self.ui.plainTextEdit.toPlainText()
        self.ui.plainText_label.setText(msg)
        self.ui.plainText_label.adjustSize()