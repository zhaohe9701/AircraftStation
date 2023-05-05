# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'treminalWindowagJeCB.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QHBoxLayout,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_TerminalWindow(object):
    def setupUi(self, TerminalWindow):
        if not TerminalWindow.objectName():
            TerminalWindow.setObjectName(u"TerminalWindow")
        TerminalWindow.resize(827, 807)
        TerminalWindow.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(30, 30, 30);\n"
"}")
        self.formLayout = QFormLayout(TerminalWindow)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.outputText = QTextEdit(TerminalWindow)
        self.outputText.setObjectName(u"outputText")
        self.outputText.setStyleSheet(u"QTextEdit\n"
"{\n"
"	font-family:Consolas;\n"
"	color:rgb(255,255,255);\n"
"	background-color:rgb(51,51,51);\n"
"	border:0px ;\n"
"}")
        self.outputText.setReadOnly(True)

        self.verticalLayout.addWidget(self.outputText)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, -1, -1, -1)
        self.addHeadBox = QCheckBox(TerminalWindow)
        self.addHeadBox.setObjectName(u"addHeadBox")
        self.addHeadBox.setStyleSheet(u"QCheckBox\n"
"{\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout.addWidget(self.addHeadBox)

        self.addEnterBox = QCheckBox(TerminalWindow)
        self.addEnterBox.setObjectName(u"addEnterBox")
        self.addEnterBox.setStyleSheet(u"QCheckBox\n"
"{\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout.addWidget(self.addEnterBox)

        self.enterSendBox = QCheckBox(TerminalWindow)
        self.enterSendBox.setObjectName(u"enterSendBox")
        self.enterSendBox.setStyleSheet(u"QCheckBox\n"
"{\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout.addWidget(self.enterSendBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.inputText = QTextEdit(TerminalWindow)
        self.inputText.setObjectName(u"inputText")
        self.inputText.setMaximumSize(QSize(16777215, 250))
        self.inputText.setStyleSheet(u"QTextEdit\n"
"{\n"
"	font-family:Consolas;\n"
"	color:rgb(255,255,255);\n"
"	background-color:rgb(51,51,51);\n"
"	border:0px ;\n"
"}")

        self.verticalLayout.addWidget(self.inputText)

        self.sendButton = QPushButton(TerminalWindow)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setStyleSheet(u"QPushButton\n"
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

        self.verticalLayout.addWidget(self.sendButton)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout)


        self.retranslateUi(TerminalWindow)

        QMetaObject.connectSlotsByName(TerminalWindow)
    # setupUi

    def retranslateUi(self, TerminalWindow):
        TerminalWindow.setWindowTitle(QCoreApplication.translate("TerminalWindow", u"Form", None))
        self.addHeadBox.setText(QCoreApplication.translate("TerminalWindow", u"\u547d\u4ee4\u5934", None))
        self.addEnterBox.setText(QCoreApplication.translate("TerminalWindow", u"\u56de\u8f66\u7b26", None))
        self.enterSendBox.setText(QCoreApplication.translate("TerminalWindow", u"\u56de\u8f66\u53d1\u9001", None))
        self.sendButton.setText(QCoreApplication.translate("TerminalWindow", u"\u53d1\u9001", None))
    # retranslateUi

