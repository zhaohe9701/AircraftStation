# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'positionWindowbyecMI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QDial, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_PositionWindow(object):
    def setupUi(self, PositionWindow):
        if not PositionWindow.objectName():
            PositionWindow.setObjectName(u"PositionWindow")
        PositionWindow.resize(847, 616)
        PositionWindow.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(30, 30, 30);\n"
"}")
        self.formLayout = QFormLayout(PositionWindow)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mapWidget = QWebEngineView(PositionWindow)
        self.mapWidget.setObjectName(u"mapWidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapWidget.sizePolicy().hasHeightForWidth())
        self.mapWidget.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.mapWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(PositionWindow)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"QLabel\n"
"{\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(PositionWindow)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        self.lineEdit.setStyleSheet(u"QWidget{\n"
"	border-radius: 6px;\n"
"	background-color: rgb(80, 80, 80);\n"
"	border:0.5px solid rgb(130,130,130);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(PositionWindow)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy2.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy2)
        self.lineEdit_2.setStyleSheet(u"QWidget{\n"
"	border-radius: 6px;\n"
"	background-color: rgb(80, 80, 80);\n"
"	border:0.5px solid rgb(130,130,130);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.label_7 = QLabel(PositionWindow)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setStyleSheet(u"QLabel\n"
"{\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout.addWidget(self.label_7)

        self.lineEdit_3 = QLineEdit(PositionWindow)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy2.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy2)
        self.lineEdit_3.setStyleSheet(u"QWidget{\n"
"	border-radius: 6px;\n"
"	background-color: rgb(80, 80, 80);\n"
"	border:0.5px solid rgb(130,130,130);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.label_9 = QLabel(PositionWindow)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setStyleSheet(u"QLabel\n"
"{\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout.addWidget(self.label_9)

        self.lineEdit_5 = QLineEdit(PositionWindow)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy2.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy2)
        self.lineEdit_5.setStyleSheet(u"QWidget{\n"
"	border-radius: 6px;\n"
"	background-color: rgb(80, 80, 80);\n"
"	border:0.5px solid rgb(130,130,130);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit_5)

        self.label_8 = QLabel(PositionWindow)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setStyleSheet(u"QLabel\n"
"{\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout.addWidget(self.label_8)

        self.lineEdit_4 = QLineEdit(PositionWindow)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy2.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy2)
        self.lineEdit_4.setStyleSheet(u"QWidget{\n"
"	border-radius: 6px;\n"
"	background-color: rgb(80, 80, 80);\n"
"	border:0.5px solid rgb(130,130,130);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit_4)

        self.dial = QDial(PositionWindow)
        self.dial.setObjectName(u"dial")
        self.dial.setWrapping(True)
        self.dial.setNotchTarget(0.000000000000000)
        self.dial.setNotchesVisible(True)

        self.verticalLayout.addWidget(self.dial)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(PositionWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"    color:rgb(255,255,255); /*\u6587\u5b57\u989c\u8272*/\n"
"    background-color:rgb(51,51,51);/*\u80cc\u666f\u8272*/\n"
"	border-style:inset;\n"
"    border-width:1px;/*\u8fb9\u6846\u5bbd\u5ea6*/\n"
"    border-color:rgb(100,100,100); /*\u8fb9\u6846\u989c\u8272*/\n"
"    border-radius:3px; /*\u8fb9\u6846\u5012\u89d2*/\n"
"}\n"
" \n"
" \n"
"/*\u9f20\u6807\u60ac\u6d6e\u65f6\u7684\u6548\u679c*/\n"
"QPushButton:hover\n"
"{\n"
"    border-color:rgb(31,156,220); /*\u8fb9\u6846\u989c\u8272*/\n"
"}\n"
"/*\u5982\u679c\u6309\u4e0b\u4e0e\u60ac\u6d6e\u60f3\u540c\u65f6\u4ea7\u751f\u6548\u679c\uff0chover\u5fc5\u987b\u5199\u5728pressed\u7684\u540e\u9762*/\n"
"/*\u9f20\u6807\u6309\u4e0b\u65f6\u7684\u6548\u679c*/\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(100, 100, 100); /*\u6539\u53d8\u80cc\u666f\u8272*/\n"
"}\n"
" \n"
"\n"
" \n"
"\n"
"")

        self.verticalLayout.addWidget(self.pushButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)


        self.retranslateUi(PositionWindow)

        QMetaObject.connectSlotsByName(PositionWindow)
    # setupUi

    def retranslateUi(self, PositionWindow):
        PositionWindow.setWindowTitle(QCoreApplication.translate("PositionWindow", u"Form", None))
        self.label.setText(QCoreApplication.translate("PositionWindow", u"\u5750\u6807\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("PositionWindow", u"\u901f\u5ea6\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("PositionWindow", u"\u9ad8\u5ea6\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("PositionWindow", u"\u822a\u5411\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("PositionWindow", u"\u6dfb\u52a0\u822a\u70b9", None))
    # retranslateUi

