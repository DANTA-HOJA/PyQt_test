import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class Stream(QObject):
    newText = pyqtSignal(str) # 自定義訊號類型

    def write(self, text): # print() 會使用 class 底下稱為 write 的 function 傳遞輸出字串
        self.newText.emit(str(text))


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initGui()

        
    def initGui(self):
        self.layout = QVBoxLayout()

        self.btn1 = QPushButton('输出”Hello World! “')
        self.btn1.clicked.connect(self.printHello)

        self.consoleBox = QTextEdit(self, readOnly=True)

        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.consoleBox)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        
        self.stream = Stream()
        self.stream.newText.connect(self.onUpdateText2)
        sys.stdout = self.stream
        
        self.show()
        
    def onUpdateText(self, text): # 要和連接的 signal 具有相同類型的引數 
        """Write console output to text widget."""
        cursor = self.consoleBox.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.consoleBox.setTextCursor(cursor)
        self.consoleBox.ensureCursorVisible()
        # self.consoleBox.append(text)
    
    
    def onUpdateText2(self, text):
        self.consoleBox.append(text)
        # self.consoleBox.insertPlainText(text)
    
    
    def closeEvent(self, event):
        """Shuts down application on close."""
        # Return stdout to defaults.
        sys.stdout = sys.__stdout__
        super().closeEvent(event)
    
    
    def printHello(self):
        print('Hello, World! ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())