# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Circular_SplashZIszGr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(345, 340)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.circularProgressBarBase = QFrame(self.centralwidget)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setGeometry(QRect(10, 10, 320, 320))
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularProgressBarBase)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255,0,127,0), stop:0.750 rgba(85, 170, 255, 255));\n"
"}\n"
"\n"
"")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: rgba(103, 103, 170, 120);\n"
"}")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularProgressBarBase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(25, 25, 270, 270))
        self.container.setStyleSheet(u"QFrame{\n"
"	border-radius: 130px;\n"
"	background-color: rgb(92, 92, 152);\n"
"}")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.container)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 40, 177, 184))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelCredits = QLabel(self.layoutWidget)
        self.labelCredits.setObjectName(u"labelCredits")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(14)
        self.labelCredits.setFont(font)
        self.labelCredits.setStyleSheet(u"background-color:none;")
        self.labelCredits.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelCredits, 6, 0, 1, 1)

        self.labelLoading = QLabel(self.layoutWidget)
        self.labelLoading.setObjectName(u"labelLoading")
        self.labelLoading.setFont(font)
        self.labelLoading.setStyleSheet(u"QLabel{\n"
"	border-radius: 8px;\n"
"	background-color: rgb(127, 127, 158);\n"
"	margin-left: 40px;\n"
"	margin-right: 40px;\n"
"}")
        self.labelLoading.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelLoading, 4, 0, 1, 1)

        self.labelName = QLabel(self.layoutWidget)
        self.labelName.setObjectName(u"labelName")
        self.labelName.setFont(font)
        self.labelName.setStyleSheet(u"background-color:none;")
        self.labelName.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelName, 0, 0, 1, 1)

        self.labelPercentage = QLabel(self.layoutWidget)
        self.labelPercentage.setObjectName(u"labelPercentage")
        self.labelPercentage.setFont(font)
        self.labelPercentage.setStyleSheet(u"background-color:none;")
        self.labelPercentage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPercentage, 1, 0, 1, 1)

        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.labelCredits.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">By:</span><span style=\" font-size:10pt; font-style:italic; color:#ffffff;\"> rawsashimi1604</span></p></body></html>", None))
        self.labelLoading.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">loading...</span></p></body></html>", None))
        self.labelName.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">StockScrap</span></p></body></html>", None))
        self.labelPercentage.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">0</span><span style=\" color:#ffffff; vertical-align:super;\">%</span></p></body></html>", None))
    # retranslateUi

