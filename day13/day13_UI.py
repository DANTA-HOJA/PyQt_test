# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'day13_UI.ui'
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 741, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img_Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.img_Button.setObjectName("img_Button")
        self.horizontalLayout.addWidget(self.img_Button)
        self.img_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.img_lineEdit.setObjectName("img_lineEdit")
        self.horizontalLayout.addWidget(self.img_lineEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(150, 460, 551, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.zoomInButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.zoomInButton.setObjectName("zoomInButton")
        self.horizontalLayout_2.addWidget(self.zoomInButton)
        self.widget = QtWidgets.QWidget(self.horizontalLayoutWidget_2)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2.addWidget(self.widget)
        self.zoomOutButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.zoomOutButton.setObjectName("zoomOutButton")
        self.horizontalLayout_2.addWidget(self.zoomOutButton)
        self.widget_2 = QtWidgets.QWidget(self.horizontalLayoutWidget_2)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.label_resolution = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_resolution.setMinimumSize(QtCore.QSize(200, 0))
        self.label_resolution.setObjectName("label_resolution")
        self.horizontalLayout_2.addWidget(self.label_resolution)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(30, 100, 741, 331))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 739, 329))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_img = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_img.setGeometry(QtCore.QRect(0, 0, 741, 331))
        self.label_img.setObjectName("label_img")
        self.scrollArea.setWidget(self.label_img)
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
        self.img_Button.setText(_translate("MainWindow", "Open Image"))
        self.zoomInButton.setText(_translate("MainWindow", "Zoom In"))
        self.zoomOutButton.setText(_translate("MainWindow", "Zoon Out"))
        self.label_resolution.setText(_translate("MainWindow", "TextLabel"))
        self.label_img.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
