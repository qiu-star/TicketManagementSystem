# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RefundUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Refund(object):
    def setupUi(self, Refund):
        Refund.setObjectName("Refund")
        Refund.resize(755, 582)
        self.label = QtWidgets.QLabel(Refund)
        self.label.setGeometry(QtCore.QRect(50, 380, 121, 31))
        self.label.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label.setObjectName("label")
        self.detail = QtWidgets.QTableWidget(Refund)
        self.detail.setGeometry(QtCore.QRect(50, 50, 641, 311))
        self.detail.setObjectName("detail")
        self.detail.setColumnCount(5)
        self.detail.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.detail.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.detail.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.detail.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.detail.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.detail.setHorizontalHeaderItem(4, item)
        self.credit = QtWidgets.QTextEdit(Refund)
        self.credit.setGeometry(QtCore.QRect(50, 420, 271, 41))
        self.credit.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.credit.setObjectName("credit")
        self.search = QtWidgets.QPushButton(Refund)
        self.search.setGeometry(QtCore.QRect(50, 490, 121, 41))
        self.search.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.search.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.search.setObjectName("search")
        self.refundbtn = QtWidgets.QPushButton(Refund)
        self.refundbtn.setGeometry(QtCore.QRect(280, 490, 121, 41))
        self.refundbtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.refundbtn.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.refundbtn.setObjectName("refundbtn")
        self.exitbtn = QtWidgets.QPushButton(Refund)
        self.exitbtn.setGeometry(QtCore.QRect(540, 490, 121, 41))
        self.exitbtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.exitbtn.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.exitbtn.setObjectName("exitbtn")
        self.label_2 = QtWidgets.QLabel(Refund)
        self.label_2.setGeometry(QtCore.QRect(470, 380, 121, 31))
        self.label_2.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_2.setObjectName("label_2")
        self.backmoney = QtWidgets.QTextEdit(Refund)
        self.backmoney.setGeometry(QtCore.QRect(470, 420, 141, 41))
        self.backmoney.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.backmoney.setObjectName("backmoney")
        self.label_3 = QtWidgets.QLabel(Refund)
        self.label_3.setGeometry(QtCore.QRect(620, 420, 121, 31))
        self.label_3.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Refund)
        self.search.clicked.connect(Refund.searchcredit)
        self.refundbtn.clicked.connect(Refund.comfirm)
        self.exitbtn.clicked.connect(Refund.exit)
        QtCore.QMetaObject.connectSlotsByName(Refund)

    def retranslateUi(self, Refund):
        _translate = QtCore.QCoreApplication.translate
        Refund.setWindowTitle(_translate("Refund", "Dialog"))
        self.label.setText(_translate("Refund", "身份证号："))
        item = self.detail.horizontalHeaderItem(0)
        item.setText(_translate("Refund", "发车日期"))
        item = self.detail.horizontalHeaderItem(1)
        item.setText(_translate("Refund", "车次"))
        item = self.detail.horizontalHeaderItem(2)
        item.setText(_translate("Refund", "目的地"))
        item = self.detail.horizontalHeaderItem(3)
        item.setText(_translate("Refund", "票价"))
        item = self.detail.horizontalHeaderItem(4)
        item.setText(_translate("Refund", "座位号"))
        self.credit.setHtml(_translate("Refund", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.search.setText(_translate("Refund", "查询"))
        self.refundbtn.setText(_translate("Refund", "退订"))
        self.exitbtn.setText(_translate("Refund", "退出"))
        self.label_2.setText(_translate("Refund", "返还钱数："))
        self.backmoney.setHtml(_translate("Refund", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("Refund", "元"))
