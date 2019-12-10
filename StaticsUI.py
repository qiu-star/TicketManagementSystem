# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StaticsUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Statics(object):
    def setupUi(self, Statics):
        Statics.setObjectName("Statics")
        Statics.resize(754, 535)
        self.label = QtWidgets.QLabel(Statics)
        self.label.setGeometry(QtCore.QRect(290, 40, 151, 51))
        self.label.setStyleSheet("font: 20pt \"方正颜宋简体\";")
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Statics)
        self.tableWidget.setGeometry(QtCore.QRect(160, 110, 421, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.retranslateUi(Statics)
        QtCore.QMetaObject.connectSlotsByName(Statics)

    def retranslateUi(self, Statics):
        _translate = QtCore.QCoreApplication.translate
        Statics.setWindowTitle(_translate("Statics", "Dialog"))
        self.label.setText(_translate("Statics", "售票统计"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Statics", "员工号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Statics", "员工姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Statics", "共计卖出票数"))
