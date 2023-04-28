# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ASUS/PycharmProjects/imageprocessingprojexct/ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(747, 597)
        self.uploadButton = QtWidgets.QPushButton(Dialog)
        self.uploadButton.setGeometry(QtCore.QRect(160, 510, 111, 41))
        self.uploadButton.setObjectName("uploadButton")
        self.showImage = QtWidgets.QPushButton(Dialog)
        self.showImage.setGeometry(QtCore.QRect(30, 60, 75, 23))
        self.showImage.setObjectName("showImage")
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(30, 90, 75, 23))
        self.closeButton.setObjectName("closeButton")
        self.plateNumber = QtWidgets.QLabel(Dialog)
        self.plateNumber.setGeometry(QtCore.QRect(20, 310, 171, 41))
        self.plateNumber.setText("")
        self.plateNumber.setObjectName("plateNumber")
        self.platePhoto = QtWidgets.QLabel(Dialog)
        self.platePhoto.setGeometry(QtCore.QRect(30, 140, 221, 201))
        self.platePhoto.setMinimumSize(QtCore.QSize(221, 201))
        self.platePhoto.setMaximumSize(QtCore.QSize(221, 201))
        self.platePhoto.setText("")
        self.platePhoto.setObjectName("platePhoto")
        self.readPlateButton = QtWidgets.QPushButton(Dialog)
        self.readPlateButton.setGeometry(QtCore.QRect(40, 510, 111, 41))
        self.readPlateButton.setObjectName("readPlateButton")
        self.addUserButton = QtWidgets.QPushButton(Dialog)
        self.addUserButton.setGeometry(QtCore.QRect(630, 540, 101, 31))
        self.addUserButton.setObjectName("addUserButton")
        self.viewAllUsersButton = QtWidgets.QPushButton(Dialog)
        self.viewAllUsersButton.setGeometry(QtCore.QRect(630, 420, 101, 31))
        self.viewAllUsersButton.setObjectName("viewAllUsersButton")
        self.deleteUserButton = QtWidgets.QPushButton(Dialog)
        self.deleteUserButton.setGeometry(QtCore.QRect(630, 460, 101, 31))
        self.deleteUserButton.setObjectName("deleteUserButton")
        self.updateUserButton = QtWidgets.QPushButton(Dialog)
        self.updateUserButton.setGeometry(QtCore.QRect(630, 500, 101, 31))
        self.updateUserButton.setObjectName("updateUserButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 71, 31))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.uploadButton.setText(_translate("Dialog", "Upload Image"))
        self.showImage.setText(_translate("Dialog", "Show"))
        self.closeButton.setText(_translate("Dialog", "Close"))
        self.readPlateButton.setText(_translate("Dialog", "Read Plate"))
        self.addUserButton.setText(_translate("Dialog", "Add User"))
        self.viewAllUsersButton.setText(_translate("Dialog", "View All Users"))
        self.deleteUserButton.setText(_translate("Dialog", "Delete User"))
        self.updateUserButton.setText(_translate("Dialog", "Update User"))
        self.label.setText(_translate("Dialog", "For Testing"))

