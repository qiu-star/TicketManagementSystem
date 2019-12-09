# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DispatchUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dispatch(object):
    def setupUi(self, Dispatch):
        Dispatch.setObjectName("Dispatch")
        Dispatch.resize(778, 441)
        self.detail = QtWidgets.QTableWidget(Dispatch)
        self.detail.setGeometry(QtCore.QRect(40, 100, 571, 301))
        self.detail.setObjectName("detail")
        self.detail.setColumnCount(0)
        self.detail.setRowCount(0)
        self.line = QtWidgets.QFrame(Dispatch)
        self.line.setGeometry(QtCore.QRect(30, 60, 711, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.title = QtWidgets.QLabel(Dispatch)
        self.title.setGeometry(QtCore.QRect(340, 20, 72, 15))
        self.title.setText("")
        self.title.setObjectName("title")
        self.acceptbtn = QtWidgets.QPushButton(Dispatch)
        self.acceptbtn.setGeometry(QtCore.QRect(630, 260, 111, 41))
        self.acceptbtn.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.acceptbtn.setObjectName("acceptbtn")
        self.cancelbtn = QtWidgets.QPushButton(Dispatch)
        self.cancelbtn.setGeometry(QtCore.QRect(630, 330, 111, 41))
        self.cancelbtn.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.cancelbtn.setObjectName("cancelbtn")

        self.retranslateUi(Dispatch)
        QtCore.QMetaObject.connectSlotsByName(Dispatch)

    def retranslateUi(self, Dispatch):
        _translate = QtCore.QCoreApplication.translate
        Dispatch.setWindowTitle(_translate("Dispatch", "Dialog"))
        self.acceptbtn.setText(_translate("Dispatch", "确定"))
        self.cancelbtn.setText(_translate("Dispatch", "取消"))
