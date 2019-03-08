# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 93)
        self.voiceTextLine = QtWidgets.QLineEdit(Dialog)
        self.voiceTextLine.setGeometry(QtCore.QRect(20, 20, 251, 51))
        self.voiceTextLine.setObjectName("voiceTextLine")
        self.commitChangeButton = QtWidgets.QPushButton(Dialog)
        self.commitChangeButton.setGeometry(QtCore.QRect(290, 20, 91, 51))
        self.commitChangeButton.setObjectName("commitChangeButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Google TTS 工具"))
        self.commitChangeButton.setText(_translate("Dialog", "转换"))


