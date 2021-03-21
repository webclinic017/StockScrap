# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'downloadIHKoCC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_main_dl(object):
    def setupUi(self, main_dl):
        if not main_dl.objectName():
            main_dl.setObjectName(u"main_dl")
        main_dl.resize(241, 108)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_dl.sizePolicy().hasHeightForWidth())
        main_dl.setSizePolicy(sizePolicy)
        main_dl.setMinimumSize(QSize(241, 108))
        main_dl.setMaximumSize(QSize(241, 108))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        main_dl.setFont(font)
        main_dl.setStyleSheet(u"background-color: rgb(225, 225, 255);")
        self.horizontalLayout = QHBoxLayout(main_dl)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.fr_main = QFrame(main_dl)
        self.fr_main.setObjectName(u"fr_main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fr_main.sizePolicy().hasHeightForWidth())
        self.fr_main.setSizePolicy(sizePolicy1)
        self.fr_main.setMinimumSize(QSize(223, 90))
        self.fr_main.setMaximumSize(QSize(223, 90))
        self.fr_main.setFont(font)
        self.fr_main.setFrameShape(QFrame.NoFrame)
        self.fr_main.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.fr_main)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 2, 202, 83))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_download = QLabel(self.layoutWidget)
        self.lb_download.setObjectName(u"lb_download")
        sizePolicy.setHeightForWidth(self.lb_download.sizePolicy().hasHeightForWidth())
        self.lb_download.setSizePolicy(sizePolicy)
        self.lb_download.setMinimumSize(QSize(200, 20))
        self.lb_download.setMaximumSize(QSize(200, 20))
        self.lb_download.setFont(font)

        self.verticalLayout.addWidget(self.lb_download)

        self.lb_stockName = QLabel(self.layoutWidget)
        self.lb_stockName.setObjectName(u"lb_stockName")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lb_stockName.sizePolicy().hasHeightForWidth())
        self.lb_stockName.setSizePolicy(sizePolicy2)
        self.lb_stockName.setMinimumSize(QSize(200, 28))
        self.lb_stockName.setMaximumSize(QSize(200, 28))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(15)
        self.lb_stockName.setFont(font1)

        self.verticalLayout.addWidget(self.lb_stockName)

        self.prog_progbar = QProgressBar(self.layoutWidget)
        self.prog_progbar.setObjectName(u"prog_progbar")
        self.prog_progbar.setMinimumSize(QSize(200, 20))
        self.prog_progbar.setMaximumSize(QSize(200, 20))
        self.prog_progbar.setValue(24)

        self.verticalLayout.addWidget(self.prog_progbar)


        self.horizontalLayout.addWidget(self.fr_main)


        self.retranslateUi(main_dl)

        QMetaObject.connectSlotsByName(main_dl)
    # setupUi

    def retranslateUi(self, main_dl):
        main_dl.setWindowTitle(QCoreApplication.translate("main_dl", u"Downloading", None))
        self.lb_download.setText(QCoreApplication.translate("main_dl", u"<html><head/><body><p><span style=\" font-size:10pt;\">Downloading Financial Data ...</span></p></body></html>", None))
        self.lb_stockName.setText(QCoreApplication.translate("main_dl", u"<html><head/><body><p><span style=\" font-size:16pt;\">TICKER</span></p></body></html>", None))
    # retranslateUi

