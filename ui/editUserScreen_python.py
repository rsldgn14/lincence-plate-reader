# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ASUS/PycharmProjects/imageprocessingprojexct/ui/editUserScreen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(880, 498)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(540, 10, 331, 181))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.editUserIdInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.editUserIdInput.setEnabled(False)
        self.editUserIdInput.setObjectName("editUserIdInput")
        self.verticalLayout.addWidget(self.editUserIdInput)
        self.editUserNameInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.editUserNameInput.setObjectName("editUserNameInput")
        self.verticalLayout.addWidget(self.editUserNameInput)
        self.editUserSurnameInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.editUserSurnameInput.setObjectName("editUserSurnameInput")
        self.verticalLayout.addWidget(self.editUserSurnameInput)
        self.editUserPlateInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.editUserPlateInput.setObjectName("editUserPlateInput")
        self.verticalLayout.addWidget(self.editUserPlateInput)
        self.editUserBlockInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.editUserBlockInput.setObjectName("editUserBlockInput")
        self.verticalLayout.addWidget(self.editUserBlockInput)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.editUserSaveBtn = QtWidgets.QPushButton(Form)
        self.editUserSaveBtn.setGeometry(QtCore.QRect(540, 210, 161, 23))
        self.editUserSaveBtn.setObjectName("editUserSaveBtn")
        self.editUserExitBtn = QtWidgets.QPushButton(Form)
        self.editUserExitBtn.setGeometry(QtCore.QRect(710, 210, 161, 23))
        self.editUserExitBtn.setObjectName("editUserExitBtn")
        self.updateUserTable = QtWidgets.QTableWidget(Form)
        self.updateUserTable.setGeometry(QtCore.QRect(10, 10, 521, 481))
        self.updateUserTable.setObjectName("updateUserTable")
        self.updateUserTable.setColumnCount(0)
        self.updateUserTable.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Edit User"))
        self.label.setText(_translate("Form", "ID"))
        self.label_2.setText(_translate("Form", "Name"))
        self.label_3.setText(_translate("Form", "Surname"))
        self.label_4.setText(_translate("Form", "Plate"))
        self.label_5.setText(_translate("Form", "Block"))
        self.editUserSaveBtn.setText(_translate("Form", "Save"))
        self.editUserExitBtn.setText(_translate("Form", "Exit"))

