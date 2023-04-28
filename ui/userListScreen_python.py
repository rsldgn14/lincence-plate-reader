# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ASUS/PycharmProjects/imageprocessingprojexct/ui/userListScreen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_List(object):
    def setupUi(self, List):
        List.setObjectName("List")
        List.resize(750, 596)
        List.setMinimumSize(QtCore.QSize(750, 596))
        List.setMaximumSize(QtCore.QSize(750, 596))
        self.userListTable = QtWidgets.QTableWidget(List)
        self.userListTable.setGeometry(QtCore.QRect(10, 10, 731, 581))
        self.userListTable.setMinimumSize(QtCore.QSize(731, 581))
        self.userListTable.setMaximumSize(QtCore.QSize(731, 581))
        self.userListTable.setObjectName("userListTable")
        self.userListTable.setColumnCount(0)
        self.userListTable.setRowCount(0)

        self.retranslateUi(List)
        QtCore.QMetaObject.connectSlotsByName(List)

    def retranslateUi(self, List):
        _translate = QtCore.QCoreApplication.translate
        List.setWindowTitle(_translate("List", "Form"))

