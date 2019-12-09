# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConductorUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(921, 458)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(740, 110, 101, 31))
        self.label.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label.setObjectName("label")
        self.aimstation = QtWidgets.QComboBox(Dialog)
        self.aimstation.setGeometry(QtCore.QRect(740, 150, 161, 31))
        self.aimstation.setStyleSheet("font: 14pt \"Academy Engraved LET\";")
        self.aimstation.setObjectName("aimstation")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(740, 210, 101, 31))
        self.label_2.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 300, 121, 31))
        self.label_3.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_3.setObjectName("label_3")
        self.price = QtWidgets.QTextBrowser(Dialog)
        self.price.setGeometry(QtCore.QRect(160, 300, 161, 41))
        self.price.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.price.setObjectName("price")
        self.detail = QtWidgets.QTableWidget(Dialog)
        self.detail.setGeometry(QtCore.QRect(50, 30, 641, 251))
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
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(440, 300, 81, 31))
        self.label_4.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_4.setObjectName("label_4")
        self.seatnum = QtWidgets.QTextBrowser(Dialog)
        self.seatnum.setGeometry(QtCore.QRect(530, 300, 161, 41))
        self.seatnum.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.seatnum.setObjectName("seatnum")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 360, 121, 31))
        self.label_5.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_5.setObjectName("label_5")
        self.rest = QtWidgets.QTextBrowser(Dialog)
        self.rest.setGeometry(QtCore.QRect(160, 360, 161, 41))
        self.rest.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.rest.setObjectName("rest")
        self.find = QtWidgets.QPushButton(Dialog)
        self.find.setGeometry(QtCore.QRect(790, 300, 111, 31))
        self.find.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.find.setObjectName("find")
        self.sell = QtWidgets.QPushButton(Dialog)
        self.sell.setGeometry(QtCore.QRect(790, 350, 111, 31))
        self.sell.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.sell.setObjectName("sell")
        self.print = QtWidgets.QPushButton(Dialog)
        self.print.setGeometry(QtCore.QRect(790, 400, 111, 31))
        self.print.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.print.setObjectName("print")
        self.aimstation_2 = QtWidgets.QComboBox(Dialog)
        self.aimstation_2.setGeometry(QtCore.QRect(740, 70, 161, 31))
        self.aimstation_2.setStyleSheet("font: 14pt \"Academy Engraved LET\";")
        self.aimstation_2.setObjectName("aimstation_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(740, 30, 101, 31))
        self.label_6.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_6.setObjectName("label_6")
        self.month = QtWidgets.QSpinBox(Dialog)
        self.month.setGeometry(QtCore.QRect(790, 210, 61, 31))
        self.month.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.month.setMinimum(1)
        self.month.setMaximum(12)
        self.month.setObjectName("month")
        self.date = QtWidgets.QSpinBox(Dialog)
        self.date.setGeometry(QtCore.QRect(790, 250, 61, 31))
        self.date.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.date.setMinimum(1)
        self.date.setMaximum(31)
        self.date.setObjectName("date")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(740, 250, 101, 31))
        self.label_7.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "目标站："))
        self.label_2.setText(_translate("Dialog", "月："))
        self.label_3.setText(_translate("Dialog", "票    价："))
        self.price.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Academy Engraved LET\';\"><br /></p></body></html>"))
        item = self.detail.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "车次"))
        item = self.detail.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "终点站"))
        item = self.detail.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "车型"))
        item = self.detail.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "发车时间"))
        item = self.detail.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "检票口"))
        self.label_4.setText(_translate("Dialog", "座位号："))
        self.seatnum.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Academy Engraved LET\';\"><br /></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "剩余车票："))
        self.rest.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Academy Engraved LET\';\"><br /></p></body></html>"))
        self.find.setText(_translate("Dialog", "查找"))
        self.sell.setText(_translate("Dialog", "销售"))
        self.print.setText(_translate("Dialog", "打印"))
        self.label_6.setText(_translate("Dialog", "上车站："))
        self.label_7.setText(_translate("Dialog", "日："))
