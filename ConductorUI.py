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
        Dialog.resize(921, 454)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(730, 60, 101, 31))
        self.label.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label.setObjectName("label")
        self.aimstation = QtWidgets.QComboBox(Dialog)
        self.aimstation.setGeometry(QtCore.QRect(730, 100, 161, 31))
        self.aimstation.setStyleSheet("font: 14pt \"Academy Engraved LET\";")
        self.aimstation.setObjectName("aimstation")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(730, 160, 101, 31))
        self.label_2.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 310, 121, 31))
        self.label_3.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_3.setObjectName("label_3")
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
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(420, 310, 121, 31))
        self.label_5.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_5.setObjectName("label_5")
        self.find = QtWidgets.QPushButton(Dialog)
        self.find.setGeometry(QtCore.QRect(790, 300, 111, 31))
        self.find.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.find.setObjectName("find")
        self.sell = QtWidgets.QPushButton(Dialog)
        self.sell.setGeometry(QtCore.QRect(790, 350, 111, 31))
        self.sell.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.sell.setObjectName("sell")
        self.refund = QtWidgets.QPushButton(Dialog)
        self.refund.setGeometry(QtCore.QRect(790, 400, 111, 31))
        self.refund.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.refund.setObjectName("refund")
        self.month = QtWidgets.QSpinBox(Dialog)
        self.month.setGeometry(QtCore.QRect(780, 160, 61, 31))
        self.month.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.month.setMinimum(1)
        self.month.setMaximum(12)
        self.month.setObjectName("month")
        self.date = QtWidgets.QSpinBox(Dialog)
        self.date.setGeometry(QtCore.QRect(780, 220, 61, 31))
        self.date.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.date.setMinimum(1)
        self.date.setMaximum(31)
        self.date.setObjectName("date")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(730, 220, 101, 31))
        self.label_7.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_7.setObjectName("label_7")
        self.price = QtWidgets.QTextEdit(Dialog)
        self.price.setGeometry(QtCore.QRect(160, 310, 161, 41))
        self.price.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.price.setObjectName("price")
        self.rest = QtWidgets.QTextEdit(Dialog)
        self.rest.setGeometry(QtCore.QRect(530, 310, 161, 41))
        self.rest.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.rest.setObjectName("rest")

        self.retranslateUi(Dialog)
        self.find.clicked.connect(Dialog.searchdetail)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "目标站："))
        self.label_2.setText(_translate("Dialog", "月："))
        self.label_3.setText(_translate("Dialog", "票    价："))
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
        self.label_5.setText(_translate("Dialog", "剩余车票："))
        self.find.setText(_translate("Dialog", "查找"))
        self.sell.setText(_translate("Dialog", "销售"))
        self.refund.setText(_translate("Dialog", "退票"))
        self.label_7.setText(_translate("Dialog", "日："))
