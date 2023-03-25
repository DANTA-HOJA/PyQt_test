from PyQt5 import QtWidgets
from controller import MainWindow_controller


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_()) # 全部的視窗都關閉才會結束