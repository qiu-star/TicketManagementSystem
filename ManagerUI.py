# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManagerUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Manager(object):
    def setupUi(self, Manager):
        Manager.setObjectName("Manager")
        Manager.resize(772, 385)
        self.trainbtn = QtWidgets.QPushButton(Manager)
        self.trainbtn.setGeometry(QtCore.QRect(90, 100, 121, 41))
        self.trainbtn.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.trainbtn.setObjectName("trainbtn")
        self.stationbtn = QtWidgets.QPushButton(Manager)
        self.stationbtn.setGeometry(QtCore.QRect(90, 180, 121, 41))
        self.stationbtn.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.stationbtn.setObjectName("stationbtn")
        self.trainnumbtn = QtWidgets.QPushButton(Manager)
        self.trainnumbtn.setGeometry(QtCore.QRect(90, 260, 121, 41))
        self.trainnumbtn.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.trainnumbtn.setObjectName("trainnumbtn")
        self.pushButton_4 = QtWidgets.QPushButton(Manager)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 100, 121, 41))
        self.pushButton_4.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Manager)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 180, 121, 41))
        self.pushButton_5.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Manager)
        self.pushButton_6.setGeometry(QtCore.QRect(550, 100, 121, 41))
        self.pushButton_6.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.line = QtWidgets.QFrame(Manager)
        self.line.setGeometry(QtCore.QRect(263, 80, 20, 261))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Manager)
        self.line_2.setGeometry(QtCore.QRect(60, 70, 651, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Manager)
        self.line_3.setGeometry(QtCore.QRect(500, 80, 20, 261))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label = QtWidgets.QLabel(Manager)
        self.label.setGeometry(QtCore.QRect(100, 30, 121, 31))
        self.label.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Manager)
        self.label_2.setGeometry(QtCore.QRect(340, 30, 121, 31))
        self.label_2.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Manager)
        self.label_3.setGeometry(QtCore.QRect(570, 30, 121, 31))
        self.label_3.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Manager)
        self.trainbtn.clicked.connect(Manager.updatetrain)
        self.stationbtn.clicked.connect(Manager.updatestation)
        self.trainnumbtn.clicked.connect(Manager.updatedeparturetime)
        self.pushButton_4.clicked.connect(Manager.addconductor)
        self.pushButton_5.clicked.connect(Manager.addmanager)
        self.pushButton_6.clicked.connect(Manager.showsell)
        QtCore.QMetaObject.connectSlotsByName(Manager)

    def retranslateUi(self, Manager):
        _translate = QtCore.QCoreApplication.translate
        Manager.setWindowTitle(_translate("Manager", "Dialog"))
        self.trainbtn.setText(_translate("Manager", "车辆修改"))
        self.stationbtn.setText(_translate("Manager", "站点修改"))
        self.trainnumbtn.setText(_translate("Manager", "车次修改"))
        self.pushButton_4.setText(_translate("Manager", "售票员管理"))
        self.pushButton_5.setText(_translate("Manager", "管理员管理"))
        self.pushButton_6.setText(_translate("Manager", "售票统计"))
        self.label.setText(_translate("Manager", "调度功能"))
        self.label_2.setText(_translate("Manager", "维护功能"))
        self.label_3.setText(_translate("Manager", "统计功能"))
