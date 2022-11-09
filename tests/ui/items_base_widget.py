# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'items.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ItemsWidget(object):
    def setupUi(self, ItemsWidget):
        if not ItemsWidget.objectName():
            ItemsWidget.setObjectName(u"ItemsWidget")
        ItemsWidget.resize(487, 198)
        self.verticalLayout = QVBoxLayout(ItemsWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(ItemsWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(ItemsWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(ItemsWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.pushButton_4 = QPushButton(ItemsWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(ItemsWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(ItemsWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(ItemsWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setCheckable(False)

        self.verticalLayout.addWidget(self.pushButton_2)


        self.retranslateUi(ItemsWidget)

        QMetaObject.connectSlotsByName(ItemsWidget)
    # setupUi

    def retranslateUi(self, ItemsWidget):
        ItemsWidget.setWindowTitle(QCoreApplication.translate("ItemsWidget", u"Items", None))
        self.label.setText(QCoreApplication.translate("ItemsWidget", u"Hello Oxygen Design", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("ItemsWidget", u"input text", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("ItemsWidget", u"input text", None))
        self.pushButton_4.setText(QCoreApplication.translate("ItemsWidget", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("ItemsWidget", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("ItemsWidget", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("ItemsWidget", u"Exit", None))
    # retranslateUi

