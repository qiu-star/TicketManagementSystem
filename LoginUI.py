# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(610, 406)
        self.ifmanager = QtWidgets.QRadioButton(Form)
        self.ifmanager.setGeometry(QtCore.QRect(140, 130, 131, 31))
        self.ifmanager.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.ifmanager.setObjectName("ifmanager")
        self.ifconductor = QtWidgets.QRadioButton(Form)
        self.ifconductor.setGeometry(QtCore.QRect(330, 130, 131, 31))
        self.ifconductor.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.ifconductor.setObjectName("ifconductor")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 20, 351, 61))
        self.label.setStyleSheet("font: 20pt \"方正颜宋简体\";")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(40, 90, 531, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.nametext = QtWidgets.QTextEdit(Form)
        self.nametext.setGeometry(QtCore.QRect(240, 210, 191, 31))
        self.nametext.setObjectName("nametext")
        self.passwordtext = QtWidgets.QTextEdit(Form)
        self.passwordtext.setGeometry(QtCore.QRect(240, 260, 191, 31))
        self.passwordtext.setObjectName("passwordtext")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 210, 91, 31))
        self.label_2.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 260, 91, 31))
        self.label_3.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_3.setObjectName("label_3")
        self.ok = QtWidgets.QPushButton(Form)
        self.ok.setGeometry(QtCore.QRect(480, 290, 91, 31))
        self.ok.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.ok.setObjectName("ok")
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(480, 340, 91, 31))
        self.cancel.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.cancel.setObjectName("cancel")

        self.retranslateUi(Form)
        self.ok.clicked.connect(Form.accept)
        self.cancel.clicked.connect(Form.exec)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ifmanager.setText(_translate("Form", "管理员"))
        self.ifconductor.setText(_translate("Form", "售票员"))
        self.label.setText(_translate("Form", "车站售票管理系统"))
        self.label_2.setText(_translate("Form", "用户名："))
        self.label_3.setText(_translate("Form", "密  码："))
        self.ok.setText(_translate("Form", "确定"))
        self.cancel.setText(_translate("Form", "退出"))
