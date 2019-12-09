# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SellUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sell(object):
    def setupUi(self, Sell):
        Sell.setObjectName("Sell")
        Sell.resize(543, 328)
        self.label = QtWidgets.QLabel(Sell)
        self.label.setGeometry(QtCore.QRect(50, 60, 81, 31))
        self.label.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label.setObjectName("label")
        self.ticketnum = QtWidgets.QSpinBox(Sell)
        self.ticketnum.setGeometry(QtCore.QRect(170, 110, 51, 31))
        self.ticketnum.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.ticketnum.setMinimum(1)
        self.ticketnum.setObjectName("ticketnum")
        self.label_2 = QtWidgets.QLabel(Sell)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 81, 31))
        self.label_2.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_2.setObjectName("label_2")
        self.credit = QtWidgets.QTextEdit(Sell)
        self.credit.setGeometry(QtCore.QRect(170, 60, 261, 41))
        self.credit.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.credit.setObjectName("credit")
        self.label_3 = QtWidgets.QLabel(Sell)
        self.label_3.setGeometry(QtCore.QRect(50, 160, 111, 31))
        self.label_3.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_3.setObjectName("label_3")
        self.sum = QtWidgets.QTextEdit(Sell)
        self.sum.setGeometry(QtCore.QRect(170, 160, 141, 41))
        self.sum.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.sum.setObjectName("sum")
        self.label_4 = QtWidgets.QLabel(Sell)
        self.label_4.setGeometry(QtCore.QRect(320, 170, 51, 31))
        self.label_4.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_4.setObjectName("label_4")
        self.print = QtWidgets.QPushButton(Sell)
        self.print.setGeometry(QtCore.QRect(380, 210, 121, 31))
        self.print.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.print.setObjectName("print")
        self.execbtn = QtWidgets.QPushButton(Sell)
        self.execbtn.setGeometry(QtCore.QRect(380, 250, 121, 31))
        self.execbtn.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.execbtn.setObjectName("execbtn")

        self.retranslateUi(Sell)
        self.print.clicked.connect(Sell.printticket)
        self.execbtn.clicked.connect(Sell.exec1)
        QtCore.QMetaObject.connectSlotsByName(Sell)

    def retranslateUi(self, Sell):
        _translate = QtCore.QCoreApplication.translate
        Sell.setWindowTitle(_translate("Sell", "Dialog"))
        self.label.setText(_translate("Sell", "身份证："))
        self.label_2.setText(_translate("Sell", "购票数："))
        self.credit.setHtml(_translate("Sell", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("Sell", "应付钱数："))
        self.sum.setHtml(_translate("Sell", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">100.0</p></body></html>"))
        self.label_4.setText(_translate("Sell", "元"))
        self.print.setText(_translate("Sell", "打印车票"))
        self.execbtn.setText(_translate("Sell", "退出"))
