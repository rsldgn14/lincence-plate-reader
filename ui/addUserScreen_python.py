# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ASUS/PycharmProjects/imageprocessingprojexct/ui/addUserScreen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(451, 319)
        Form.setMinimumSize(QtCore.QSize(451, 319))
        Form.setMaximumSize(QtCore.QSize(451, 319))
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 60, 321, 102))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.addNameInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.addNameInput.setObjectName("addNameInput")
        self.verticalLayout_2.addWidget(self.addNameInput)
        self.addSurnameInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.addSurnameInput.setObjectName("addSurnameInput")
        self.verticalLayout_2.addWidget(self.addSurnameInput)
        self.addPlateInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.addPlateInput.setObjectName("addPlateInput")
        self.verticalLayout_2.addWidget(self.addPlateInput)
        self.addBlockInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.addBlockInput.setObjectName("addBlockInput")
        self.verticalLayout_2.addWidget(self.addBlockInput)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setGeometry(QtCore.QRect(60, 180, 75, 23))
        self.addButton.setObjectName("addButton")
        self.exitButton = QtWidgets.QPushButton(Form)
        self.exitButton.setGeometry(QtCore.QRect(140, 180, 75, 23))
        self.exitButton.setObjectName("exitButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add User"))
        self.label_4.setText(_translate("Form", "Name"))
        self.label_5.setText(_translate("Form", "Surname"))
        self.label_3.setText(_translate("Form", "Plate"))
        self.label_2.setText(_translate("Form", "Block"))
        self.addButton.setText(_translate("Form", "Add"))
        self.exitButton.setText(_translate("Form", "Exit"))

