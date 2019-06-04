# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/folderDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 60, 350, 92))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.folderOpenButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folderOpenButton.sizePolicy().hasHeightForWidth())
        self.folderOpenButton.setSizePolicy(sizePolicy)
        self.folderOpenButton.setMinimumSize(QtCore.QSize(75, 26))
        self.folderOpenButton.setMaximumSize(QtCore.QSize(180, 126))
        self.folderOpenButton.setObjectName("folderOpenButton")
        self.gridLayout.addWidget(self.folderOpenButton, 0, 2, 1, 1)
        self.actionEdit = QtWidgets.QLineEdit(self.widget)
        self.actionEdit.setObjectName("actionEdit")
        self.gridLayout.addWidget(self.actionEdit, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.actionComboBox = QtWidgets.QComboBox(self.widget)
        self.actionComboBox.setObjectName("actionComboBox")
        self.gridLayout.addWidget(self.actionComboBox, 1, 2, 1, 1)
        self.folderEdit = QtWidgets.QComboBox(self.widget)
        self.folderEdit.setMinimumSize(QtCore.QSize(180, 0))
        self.folderEdit.setEditable(True)
        self.folderEdit.setObjectName("folderEdit")
        self.gridLayout.addWidget(self.folderEdit, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.folderOpenButton.setText(_translate("Dialog", "Open..."))
        self.label.setText(_translate("Dialog", "Select folder"))
        self.label_2.setText(_translate("Dialog", "Action"))


