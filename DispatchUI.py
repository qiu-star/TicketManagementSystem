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
        Dispatch.resize(784, 530)
        Dispatch.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.detail = QtWidgets.QTableWidget(Dispatch)
        self.detail.setGeometry(QtCore.QRect(40, 130, 571, 301))
        self.detail.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.detail.setObjectName("detail")
        self.detail.setColumnCount(0)
        self.detail.setRowCount(0)
        self.line = QtWidgets.QFrame(Dispatch)
        self.line.setGeometry(QtCore.QRect(30, 90, 711, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.title = QtWidgets.QLabel(Dispatch)
        self.title.setGeometry(QtCore.QRect(320, 30, 211, 41))
        font = QtGui.QFont()
        font.setFamily("方正颜宋简体")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setStyleSheet("font: 20pt \"方正颜宋简体\";")
        self.title.setObjectName("title")
        self.acceptbtn = QtWidgets.QPushButton(Dispatch)
        self.acceptbtn.setGeometry(QtCore.QRect(630, 130, 111, 41))
        self.acceptbtn.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.acceptbtn.setObjectName("acceptbtn")
        self.cancelbtn = QtWidgets.QPushButton(Dispatch)
        self.cancelbtn.setGeometry(QtCore.QRect(630, 200, 111, 41))
        self.cancelbtn.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.cancelbtn.setObjectName("cancelbtn")
        self.addbtn = QtWidgets.QPushButton(Dispatch)
        self.addbtn.setGeometry(QtCore.QRect(110, 450, 111, 41))
        self.addbtn.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.addbtn.setObjectName("addbtn")
        self.deletebtn = QtWidgets.QPushButton(Dispatch)
        self.deletebtn.setGeometry(QtCore.QRect(420, 450, 111, 41))
        self.deletebtn.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.deletebtn.setObjectName("deletebtn")

        self.retranslateUi(Dispatch)
        self.acceptbtn.clicked.connect(Dispatch.accept)
        self.cancelbtn.clicked.connect(Dispatch.exit)
        self.addbtn.clicked.connect(Dispatch.tableadd)
        self.deletebtn.clicked.connect(Dispatch.tabledelete)
        QtCore.QMetaObject.connectSlotsByName(Dispatch)

    def retranslateUi(self, Dispatch):
        _translate = QtCore.QCoreApplication.translate
        Dispatch.setWindowTitle(_translate("Dispatch", "Dialog"))
        self.title.setText(_translate("Dispatch", "车辆修改"))
        self.acceptbtn.setText(_translate("Dispatch", "确定"))
        self.cancelbtn.setText(_translate("Dispatch", "取消"))
        self.addbtn.setText(_translate("Dispatch", "增加"))
        self.deletebtn.setText(_translate("Dispatch", "删除"))
