# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

## THIS IS AN EDITED FILE

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.main import Ui_MainWindow
import requests
import sys

class Ui_LoginWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self,LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setKerning(True)
        LoginWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 150, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 220, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 10, 581, 131))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 160, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 230, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 300, 321, 61))
        self.pushButton.clicked.connect(self.login)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.label.setText(_translate("LoginWindow", "Username:"))
        self.label_2.setText(_translate("LoginWindow", "Password:"))
        self.label_3.setText(_translate("LoginWindow", "Messenger"))
        self.pushButton.setText(_translate("LoginWindow", "Login"))

    def login(self):
        login_url = "http://localhost:8080/api/login"
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        data = {"username":username,"password":password}
        response = requests.post(login_url,data=data)
        if "{" in response.text and "}" in response.text:
            print("DSADS")
            self.json = response.json()
            if self.json["bad_credentials"]:
                print("bad_credentials")
            else:
                print("Logged in")
                with open("token","w+") as file:
                    file.write(self.json["token"])
                self.close()
                Ui_MainWindow().login()
        else:
            print("Something unexpected happened")