# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 651)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("* {background-color: qlineargradient(spread:pad, x1:0.523045, y1:0, x2:0.522, y2:0.994318, stop:0 rgba(6, 136, 165, 255), stop:1 rgba(5, 100, 189, 155))}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 9, 2884, 2052))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setMouseTracking(True)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 2880, 2048))
        self.scrollAreaWidgetContents.setStyleSheet("QScrollArea { color: blue }")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setGeometry(QtCore.QRect(505, 210, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("* {position: absolute;\n"
"width: 169.27px;\n"
"height: 50.9px;\n"
"left: 360.6px;\n"
"top: 436.84px;\n"
"\n"
"font-family: Montserrat;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"line-height: 44px;\n"
"\n"
"color: #FFFFFF;}")
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setGeometry(QtCore.QRect(455, 450, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAutoFillBackground(False)
        self.lineEdit_4.setStyleSheet("* {position: absolute;\n"
"width: 169.27px;\n"
"height: 50.9px;\n"
"left: 360.6px;\n"
"top: 436.84px;\n"
"\n"
"font-family: Montserrat;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"line-height: 44px;\n"
"\n"
"color: #FFFFFF;}")
        self.lineEdit_4.setFrame(False)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_5.setGeometry(QtCore.QRect(225, 210, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet("* {position: absolute;\n"
"width: 169.27px;\n"
"height: 50.9px;\n"
"left: 360.6px;\n"
"top: 436.84px;\n"
"\n"
"font-family: Montserrat;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"line-height: 44px;\n"
"\n"
"color: #FFFFFF;}")
        self.lineEdit_5.setFrame(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setGeometry(QtCore.QRect(225, 450, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setStyleSheet("* {position: absolute;\n"
"width: 169.27px;\n"
"height: 50.9px;\n"
"left: 360.6px;\n"
"top: 436.84px;\n"
"\n"
"font-family: Montserrat;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"line-height: 44px;\n"
"\n"
"color: #FFFFFF;}")
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(198, 100, 121, 111))
        self.pushButton.setStyleSheet("*{position: absolute;\n"
"width: 230.6px;\n"
"height: 230.6px;\n"
"left: 329.93px;\n"
"top: 623.01px;\n"
"\n"
"background: rgba(255, 255, 255, 0.3);\n"
"border-radius: 15px;}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Image/project-management.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(479, 100, 121, 111))
        self.pushButton_2.setStyleSheet("*{position: absolute;\n"
"width: 230.6px;\n"
"height: 230.6px;\n"
"left: 329.93px;\n"
"top: 623.01px;\n"
"\n"
"background: rgba(255, 255, 255, 0.3);\n"
"border-radius: 15px;}")
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setGeometry(QtCore.QRect(481, 340, 121, 111))
        self.pushButton_3.setStyleSheet("*{position: absolute;\n"
"width: 230.6px;\n"
"height: 230.6px;\n"
"left: 329.93px;\n"
"top: 623.01px;\n"
"\n"
"background: rgba(255, 255, 255, 0.3);\n"
"border-radius: 15px;}")
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 340, 121, 111))
        self.pushButton_4.setStyleSheet("*{position: absolute;\n"
"width: 230.6px;\n"
"height: 230.6px;\n"
"left: 329.93px;\n"
"top: 623.01px;\n"
"\n"
"background: rgba(255, 255, 255, 0.3);\n"
"border-radius: 15px;}")
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 21))
        self.menubar.setStyleSheet("* { background-color: rgb(19, 173, 207) }")
        self.menubar.setObjectName("menubar")
        self.menuFiles = QtWidgets.QMenu(self.menubar)
        self.menuFiles.setStyleSheet("a{qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(6, 136, 165, 255), stop:1 rgba(129, 129, 129, 255))}")
        self.menuFiles.setObjectName("menuFiles")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_a_Project = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Image/plus 1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionAdd_a_Project.setIcon(icon1)
        self.actionAdd_a_Project.setObjectName("actionAdd_a_Project")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Image/exit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionExit_2.setIcon(icon2)
        self.actionExit_2.setObjectName("actionExit_2")
        self.menuFiles.addAction(self.actionAdd_a_Project)
        self.menuFiles.addAction(self.actionExit_2)
        self.menubar.addAction(self.menuFiles.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(self.pushButton_3.animateClick)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_2.setText(_translate("MainWindow", "Project 2"))
        self.lineEdit_4.setText(_translate("MainWindow", "Create New Project"))
        self.lineEdit_5.setText(_translate("MainWindow", "Project 1"))
        self.lineEdit_3.setText(_translate("MainWindow", "Project 3"))
        self.menuFiles.setTitle(_translate("MainWindow", "Files"))
        self.actionAdd_a_Project.setText(_translate("MainWindow", "Add a Project"))
        self.actionAdd_a_Project.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionExit_2.setShortcut(_translate("MainWindow", "Esc"))
import Resource_rc
