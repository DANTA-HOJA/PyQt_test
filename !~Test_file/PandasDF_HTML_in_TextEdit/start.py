from PyQt5 import QtWidgets
from Form_ctrl import Df_in_HTML_Form 

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Df_in_HTML_Form()    
    window.show()
    sys.exit(app.exec_()) # 全部的視窗都關閉才會結束