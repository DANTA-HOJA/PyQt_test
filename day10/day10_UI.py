# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\day10.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 110, 171, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.file_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.file_Button.setEnabled(True)
        self.file_Button.setMinimumSize(QtCore.QSize(0, 50))
        self.file_Button.setObjectName("file_Button")
        self.verticalLayout.addWidget(self.file_Button)
        self.folder_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.folder_Button.setMinimumSize(QtCore.QSize(0, 50))
        self.folder_Button.setObjectName("folder_Button")
        self.verticalLayout.addWidget(self.folder_Button)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(310, 110, 331, 191))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.file_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.file_lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.file_lineEdit.setObjectName("file_lineEdit")
        self.verticalLayout_2.addWidget(self.file_lineEdit)
        self.folder_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.folder_lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.folder_lineEdit.setObjectName("folder_lineEdit")
        self.verticalLayout_2.addWidget(self.folder_lineEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.file_Button.setText(_translate("MainWindow", "Open File"))
        self.folder_Button.setText(_translate("MainWindow", "Open Folder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
