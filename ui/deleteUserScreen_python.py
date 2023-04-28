# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ASUS/PycharmProjects/imageprocessingprojexct/ui/deleteUserScreen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(883, 497)
        Form.setMinimumSize(QtCore.QSize(883, 497))
        Form.setMaximumSize(QtCore.QSize(883, 497))
        self.deleteButton = QtWidgets.QPushButton(Form)
        self.deleteButton.setGeometry(QtCore.QRect(710, 470, 75, 23))
        self.deleteButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteButton.setObjectName("deleteButton")
        self.deleteUserTable = QtWidgets.QTableWidget(Form)
        self.deleteUserTable.setGeometry(QtCore.QRect(10, 10, 691, 481))
        self.deleteUserTable.setObjectName("deleteUserTable")
        self.deleteUserTable.setColumnCount(0)
        self.deleteUserTable.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Delete User"))
        self.deleteButton.setText(_translate("Form", "Delete"))

