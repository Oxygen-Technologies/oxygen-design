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
        ItemsWidget.resize(698, 395)
        self.verticalLayout = QVBoxLayout(ItemsWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(ItemsWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(ItemsWidget)

        QMetaObject.connectSlotsByName(ItemsWidget)
    # setupUi

    def retranslateUi(self, ItemsWidget):
        ItemsWidget.setWindowTitle(QCoreApplication.translate("ItemsWidget", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("ItemsWidget", u"PushButton", None))
    # retranslateUi

