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
        

        self.lineEdit = QLineEdit("hello")
        
        
        self.layout_addText = QHBoxLayout()
        self.btnInsertPlainText = QPushButton('Insert')
        self.btnInsertPlainText.clicked.connect(self.InsertPlainText)
        self.btnInsertHTML = QPushButton('Insert HTML')
        self.btnInsertHTML.clicked.connect(self.InsertHTML)
        self.btnAppendText = QPushButton('Append')
        self.btnAppendText.clicked.connect(self.AppendText)
        self.layout_addText.addWidget(self.btnInsertPlainText)
        self.layout_addText.addWidget(self.btnInsertHTML)
        self.layout_addText.addWidget(self.btnAppendText)
        
        

        self.TextEdit = QTextEdit(self, readOnly=True)
        
        self.btnConvert = QPushButton('convert to HTML')
        self.btnConvert.clicked.connect(self.convertToHTML)
        
        self.TextEditHTML = QTextEdit(self, readOnly=True)

        
        self.layout.addWidget(self.lineEdit)
        self.layout.addLayout(self.layout_addText)
        self.layout.addWidget(self.TextEdit)
        self.layout.addWidget(self.btnConvert)
        self.layout.addWidget(self.TextEditHTML)


        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        
        self.stream = Stream()
        self.stream.newText.connect(self.onUpdateText)
        sys.stdout = self.stream


        self.show()



    def closeEvent(self, event):
        """Shuts down application on close."""
        # Return stdout to defaults.
        sys.stdout = sys.__stdout__
        super().closeEvent(event)

    
    def onUpdateText(self, text): # 要和連接的 signal 具有相同類型的引數 
        """Write console output to text widget."""
        cursor = self.TextEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.TextEdit.setTextCursor(cursor)
        self.TextEdit.ensureCursorVisible()
        # self.consoleBox.append(text)
    
    
    def InsertPlainText(self):
        self.stream.newText.disconnect() # 因一個 signal 可以 connect 多個 function，需先斷開才 connect 新的方法，
                                         # 否則會單一個 print 所有已 connect 過的 function，出現 emit 一次 print 三次的情況。
        self.stream.newText.connect(lambda text: self.TextEdit.insertPlainText(text))
        print(self.lineEdit.text())
    
    
    def InsertHTML(self):
        self.stream.newText.disconnect()
        self.stream.newText.connect(lambda text: self.TextEdit.insertHtml(text))
        print(self.lineEdit.text())
    
    
    def AppendText(self):
        self.stream.newText.disconnect()
        self.stream.newText.connect(lambda text: self.TextEdit.append(text))
        print(self.lineEdit.text())
    
    
    def convertToHTML(self):
        self.TextEditHTML.setPlainText(self.TextEdit.toHtml())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())