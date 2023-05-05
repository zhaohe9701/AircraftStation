# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connectWindowIJYgaC.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)
import icon.icon_rc

class Ui_ConnectWindow(object):
    def setupUi(self, ConnectWindow):
        if not ConnectWindow.objectName():
            ConnectWindow.setObjectName(u"ConnectWindow")
        ConnectWindow.setWindowModality(Qt.NonModal)
        ConnectWindow.resize(498, 510)
        ConnectWindow.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(30, 30, 30);\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(ConnectWindow)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame = QFrame(ConnectWindow)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"QLabel\n"
"{\n"
"	color:rgb(255,255,255);\n"
"}")
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setTextFormat(Qt.PlainText)

        self.verticalLayout.addWidget(self.label)

        self.connectWaySelectBox = QComboBox(self.frame)
        self.connectWaySelectBox.addItem("")
        self.connectWaySelectBox.addItem("")
        self.connectWaySelectBox.setObjectName(u"connectWaySelectBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.connectWaySelectBox.sizePolicy().hasHeightForWidth())
        self.connectWaySelectBox.setSizePolicy(sizePolicy1)
        self.connectWaySelectBox.setMinimumSize(QSize(0, 0))
        self.connectWaySelectBox.setMaximumSize(QSize(300, 16777215))
        self.connectWaySelectBox.setStyleSheet(u"QComboBox\n"
"{\n"
"	border-radius:3px;\n"
"	background-color:rgba(60,60,60,200);\n"
"    color:rgb(255,255,255);\n"
"    border:0px ;\n"
"	padding-top: 2px;\n"
"	padding-left: 2px;\n"
"}\n"
"QComboBox:disabled\n"
"{\n"
"	background-color:rgba(50,50,50,200);\n"
"    color:rgb(160,160,160);\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"	background-color:rgba(45,45,45,200);\n"
"	border:1px solid rgb(31,156,220) ;\n"
"}\n"
"/*\u70b9\u51fbcombox\u7684\u6837\u5f0f*/\n"
"QComboBox:on\n"
"{\n"
"	border-radius:3px;\n"
"    color:rgb(255,255,255);\n"
"    border:1px solid rgb(31,156,220) ;\n"
"}\n"
"/*\u4e0b\u62c9\u6846\u7684\u6837\u5f0f*/\n"
"QComboBox QAbstractItemView \n"
"{\n"
"    outline: 0px solid gray;  /*\u53d6\u6d88\u9009\u4e2d\u865a\u7ebf*/\n"
"    border: 1px solid rgb(31,156,220);  \n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(45,45,45);   \n"
"    selection-background-color: rgb(90,90,90);   \n"
"	border-radius:3px;\n"
"	\n"
"}\n"
" /*\u9009\u4e2d\u6bcf\u4e00\u9879\u9ad8\u5ea6*/\n"
"QComboBox QAbs"
                        "tractItemView::item\n"
" { \n"
"	height: 25px;  \n"
" }\n"
"/*\u9009\u4e2d\u6bcf\u4e00\u9879\u7684\u5b57\u4f53\u989c\u8272\u548c\u80cc\u666f\u989c\u8272*/\n"
"QComboBox QAbstractItemView::item:selected \n"
"{\n"
"    color: rgb(31,163,246);\n"
"	background-color: rgb(90,90,90); \n"
"}\n"
" /*\u4e0b\u62c9\u7bad\u5934\u7684\u8fb9\u6846*/\n"
"QComboBox::drop-down \n"
"{\n"
"	border:none;\n"
"}\n"
" /*\u4e0b\u62c9\u7bad\u5934\u6837\u5f0f*/\n"
"QComboBox::down-arrow \n"
"{\n"
"    right:8px;/*\u63a7\u5236\u7bad\u5934\u5de6\u53f3\u504f\u79fb*/\n"
"    width: 12px;  \n"
"    height: 12px;   \n"
"	image:url(:/icon/arrow-down.png)\n"
"}\n"
" /*\u4e0b\u62c9\u7bad\u5934\u70b9\u51fb\u6837\u5f0f*/\n"
"")

        self.verticalLayout.addWidget(self.connectWaySelectBox)

        self.connectSetWidget = QStackedWidget(self.frame)
        self.connectSetWidget.setObjectName(u"connectSetWidget")
        self.connectSetWidget.setStyleSheet(u"")
        self.connectSetWidget.setFrameShadow(QFrame.Plain)
        self.connectSetWidget.setLineWidth(1)
        self.uartPage = QWidget()
        self.uartPage.setObjectName(u"uartPage")
        self.formLayout_2 = QFormLayout(self.uartPage)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.uartPage)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(u"QLabel\n"
"{\n"
"	color:rgb(255,255,255);\n"
"}")
        self.label_5.setFrameShadow(QFrame.Plain)
        self.label_5.setTextFormat(Qt.PlainText)

        self.horizontalLayout.addWidget(self.label_5)

        self.refreshButton = QToolButton(self.uartPage)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setStyleSheet(u"/* \u9ed8\u8ba4 */\n"
"QToolButton{   \n"
"	border: 0px outset transparent;  \n"
"}\n"
"\n"
"/* \u9f20\u6807\u60ac\u505c */\n"
"QToolButton:hover{\n"
"	background-color:rgb(100, 100, 100); \n"
"}\n"
"\n"
"/* \u70b9\u51fb\u548c\u6309\u4e0b */\n"
"QToolButton:pressed,QToolButton:checked{\n"
"	background-color:rgb(100, 100, 100); \n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../icon/reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.refreshButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.portNumBox = QComboBox(self.uartPage)
        self.portNumBox.setObjectName(u"portNumBox")
        self.portNumBox.setMinimumSize(QSize(0, 0))
        self.portNumBox.setMaximumSize(QSize(16777215, 16777215))
        self.portNumBox.setStyleSheet(u"QComboBox\n"
"{\n"
"	border-radius:3px;\n"
"	background-color:rgba(60,60,60,200);\n"
"    color:rgb(255,255,255);\n"
"    border:0px ;\n"
"	padding-top: 2px;\n"
"	padding-left: 2px;\n"
"}\n"
"QComboBox:disabled\n"
"{\n"
"	background-color:rgba(50,50,50,200);\n"
"    color:rgb(160,160,160);\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"	background-color:rgba(45,45,45,200);\n"
"	border:1px solid rgb(31,156,220) ;\n"
"}\n"
"/*\u70b9\u51fbcombox\u7684\u6837\u5f0f*/\n"
"QComboBox:on\n"
"{\n"
"	border-radius:3px;\n"
"    color:rgb(255,255,255);\n"
"    border:1px solid rgb(31,156,220) ;\n"
"}\n"
"/*\u4e0b\u62c9\u6846\u7684\u6837\u5f0f*/\n"
"QComboBox QAbstractItemView \n"
"{\n"
"    outline: 0px solid gray;  /*\u53d6\u6d88\u9009\u4e2d\u865a\u7ebf*/\n"
"    border: 1px solid rgb(31,156,220);  \n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(45,45,45);   \n"
"    selection-background-color: rgb(90,90,90);   \n"
"	border-radius:3px;\n"
"	\n"
"}\n"
" /*\u9009\u4e2d\u6bcf\u4e00\u9879\u9ad8\u5ea6*/\n"
"QComboBox QAbs"
                        "tractItemView::item\n"
" { \n"
"	height: 25px;  \n"
" }\n"
"/*\u9009\u4e2d\u6bcf\u4e00\u9879\u7684\u5b57\u4f53\u989c\u8272\u548c\u80cc\u666f\u989c\u8272*/\n"
"QComboBox QAbstractItemView::item:selected \n"
"{\n"
"    color: rgb(31,163,246);\n"
"	background-color: rgb(90,90,90); \n"
"}\n"
" /*\u4e0b\u62c9\u7bad\u5934\u7684\u8fb9\u6846*/\n"
"QComboBox::drop-down \n"
"{\n"
"	border:none;\n"
"}\n"
" /*\u4e0b\u62c9\u7bad\u5934\u6837\u5f0f*/\n"
"QComboBox::down-arrow \n"
"{\n"
"    right:8px;/*\u63a7\u5236\u7bad\u5934\u5de6\u53f3\u504f\u79fb*/\n"
"    width: 12px;  \n"
"    height: 12px;   \n"
"	image:url(:/icon/arrow-down.png)\n"
"}\n"
" /*\u4e0b\u62c9\u7bad\u5934\u70b9\u51fb\u6837\u5f0f*/\n"
"")

        self.verticalLayout_2.addWidget(self.portNumBox)

        self.label_3 = QLabel(self.uartPage)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"QLabel\n"
"{\n"
"	color:rgb(255,255,255);\n"
"}")
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_3.setTextFormat(Qt.PlainText)

        self.verticalLayout_2.addWidget(self.label_3)

        self.baudRateBox = QComboBox(self.uartPage)
        self.baudRateBox.addItem("")
        self.baudRateBox.addItem("")
        self.baudRateBox.addItem("")
        self.baudRateBox.addItem("")
        self.baudRateBox.setObjectName(u"baudRateBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.baudRateBox.sizePolicy().hasHeightForWidth())
        self.baudRateBox.setSizePolicy(sizePolicy3)
        self.baudRateBox.setMinimumSize(QSize(0, 0))
        self.baudRateBox.setMaximumSize(QSize(16777215, 16777215))
        self.baudRateBox.setStyleSheet(u"QComboBox\n"
"{\n"
"	border-radius:3px;\n"
"	background-color:rgba(60,60,60,200);\n"
"    color:rgb(255,255,255);\n"
"    border:0px ;\n"
"	padding-top: 2px;\n"
"	padding-left: 2px;\n"
"}\n"
"QComboBox:disabled\n"
"{\n"
"	background-color:rgba(50,50,50,200);\n"
"    color:rgb(160,160,160);\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"	background-color:rgba(45,45,45,200);\n"
"	border:1px solid rgb(31,156,220) ;\n"
"}\n"
"/*\u70b9\u51fbcombox\u7684\u6837\u5f0f*/\n"
"QComboBox:on\n"
"{\n"
"	border-radius:3px;\n"
"    color:rgb(255,255,255);\n"
"    border:1px solid rgb(31,156,220) ;\n"
"}\n"
"/*\u4e0b\u62c9\u6846\u7684\u6837\u5f0f*/\n"
"QComboBox QAbstractItemView \n"
"{\n"
"    outline: 0px solid gray;  /*\u53d6\u6d88\u9009\u4e2d\u865a\u7ebf*/\n"
"    border: 1px solid rgb(31,156,220);  \n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(45,45,45);   \n"
"    selection-background-color: rgb(90,90,90);   \n"
"	border-radius:3px;\n"
"	\n"
"}\n"
" /*\u9009\u4e2d\u6bcf\u4e00\u9879\u9ad8\u5ea6*/\n"
"QComboBox QAbs"
                        "tractItemView::item\n"
" { \n"
"	height: 25px;  \n"
" }\n"
"/*\u9009\u4e2d\u6bcf\u4e00\u9879\u7684\u5b57\u4f53\u989c\u8272\u548c\u80cc\u666f\u989c\u8272*/\n"
"QComboBox QAbstractItemView::item:selected \n"
"{\n"
"    color: rgb(31,163,246);\n"
"	background-color: rgb(90,90,90); \n"
"}\n"
" /*\u4e0b\u62c9\u7bad\u5934\u7684\u8fb9\u6846*/\n"
"QComboBox::drop-down \n"
"{\n"
"	\n"
"    width: 30px; /* \u8bbe\u7f6e\u4e0b\u62c9\u89e6\u53d1\u533a\u57df\u7684\u5bbd\u5ea6 */\n"
"	border:none;\n"
"\n"
"}\n"
" /*\u4e0b\u62c9\u7bad\u5934\u6837\u5f0f*/\n"
"QComboBox::down-arrow \n"
"{\n"
"    right:1px;/*\u63a7\u5236\u7bad\u5934\u5de6\u53f3\u504f\u79fb*/\n"
"    width: 12px;  \n"
"    height: 12px;   \n"
"	image:url(:/icon/arrow-down.png)\n"
"}\n"
" /*\u4e0b\u62c9\u7bad\u5934\u70b9\u51fb\u6837\u5f0f*/\n"
"")
        self.baudRateBox.setEditable(True)

        self.verticalLayout_2.addWidget(self.baudRateBox)

        self.label_4 = QLabel(self.uartPage)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"QLabel\n"
"{\n"
"	color:rgb(255,255,255);\n"
"}")
        self.label_4.setFrameShadow(QFrame.Plain)
        self.label_4.setTextFormat(Qt.PlainText)

        self.verticalLayout_2.addWidget(self.label_4)

        self.dataLenBox = QComboBox(self.uartPage)
        self.dataLenBox.addItem("")
        self.dataLenBox.addItem("")
        self.dataLenBox.addItem("")
        self.dataLenBox.addItem("")
        self.dataLenBox.setObjectName(u"dataLenBox")
        self.dataLenBox.setMinimumSize(QSize(0, 0))
        self.dataLenBox.setMaximumSize(QSize(16777215, 16777215))
        self.dataLenBox.setStyleSheet(u"QComboBox\n"
"{\n"
"	border-radius:3px;\n"
"	background-color:rgba(60,60,60,200);\n"
"    color:rgb(255,255,255);\n"
"    border:0px ;\n"
"	padding-top: 2px;\n"
"	padding-left: 2px;\n"
"}\n"
"QComboBox:disabled\n"
"{\n"
"	background-color:rgba(50,50,50,200);\n"
"    color:rgb(160,160,160);\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"	background-color:rgba(45,45,45,200);\n"
"	border:1px solid rgb(31,156,220) ;\n"
"}\n"
"/*\u70b9\u51fbcombox\u7684\u6837\u5f0f*/\n"
"QComboBox:on\n"
"{\n"
"	border-radius:3px;\n"
"    color:rgb(255,255,255);\n"
"    border:1px solid rgb(31,156,220) ;\n"
"}\n"
"/*\u4e0b\u62c9\u6846\u7684\u6837\u5f0f*/\n"
"QComboBox QAbstractItemView \n"
"{\n"
"    outline: 0px solid gray;  /*\u53d6\u6d88\u9009\u4e2d\u865a\u7ebf*/\n"
"    border: 1px solid rgb(31,156,220);  \n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(45,45,45);   \n"
"    selection-background-color: rgb(90,90,90);   \n"
"	border-radius:3px;\n"
"	\n"
"}\n"
" /*\u9009\u4e2d\u6bcf\u4e00\u9879\u9ad8\u5ea6*/\n"
"QComboBox QAbs"
                        "tractItemView::item\n"
" { \n"
"	height: 25px;  \n"
" }\n"
"/*\u9009\u4e2d\u6bcf\u4e00\u9879\u7684\u5b57\u4f53\u989c\u8272\u548c\u80cc\u666f\u989c\u8272*/\n"
"QComboBox QAbstractItemView::item:selected \n"
"{\n"
"    color: rgb(31,163,246);\n"
"	background-color: rgb(90,90,90); \n"
"}\n"
" /*\u4e0b\u62c9\u7bad\u5934\u7684\u8fb9\u6846*/\n"
"QComboBox::drop-down \n"
"{\n"
"	border:none;\n"
"}\n"
" /*\u4e0b\u62c9\u7bad\u5934\u6837\u5f0f*/\n"
"QComboBox::down-arrow \n"
"{\n"
"    right:8px;/*\u63a7\u5236\u7bad\u5934\u5de6\u53f3\u504f\u79fb*/\n"
"    width: 12px;  \n"
"    height: 12px;   \n"
"	image:url(:/icon/arrow-down.png)\n"
"}\n"
" /*\u4e0b\u62c9\u7bad\u5934\u70b9\u51fb\u6837\u5f0f*/\n"
"")

        self.verticalLayout_2.addWidget(self.dataLenBox)

        self.label_6 = QLabel(self.uartPage)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet(u"QLabel\n"
"{\n"
"	color:rgb(255,255,255);\n"
"}")
        self.label_6.setFrameShadow(QFrame.Plain)
        self.label_6.setTextFormat(Qt.PlainText)

        self.verticalLayout_2.addWidget(self.label_6)

        self.checkPattermBox = QComboBox(self.uartPage)
        self.checkPattermBox.addItem("")
        self.checkPattermBox.addItem("")
        self.checkPattermBox.addItem("")
        self.checkPattermBox.setObjectName(u"checkPattermBox")
        self.checkPattermBox.setMinimumSize(QSize(0, 0))
        self.checkPattermBox.setMaximumSize(QSize(16777215, 16777215))
        self.checkPattermBox.setStyleSheet(u"QComboBox\n"
"{\n"
"	border-radius:3px;\n"
"	background-color:rgba(60,60,60,200);\n"
"    color:rgb(255,255,255);\n"
"    border:0px ;\n"
"	padding-top: 2px;\n"
"	padding-left: 2px;\n"
"}\n"
"QComboBox:disabled\n"
"{\n"
"	background-color:rgba(50,50,50,200);\n"
"    color:rgb(160,160,160);\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"	background-color:rgba(45,45,45,200);\n"
"	border:1px solid rgb(31,156,220) ;\n"
"}\n"
"/*\u70b9\u51fbcombox\u7684\u6837\u5f0f*/\n"
"QComboBox:on\n"
"{\n"
"	border-radius:3px;\n"
"    color:rgb(255,255,255);\n"
"    border:1px solid rgb(31,156,220) ;\n"
"}\n"
"/*\u4e0b\u62c9\u6846\u7684\u6837\u5f0f*/\n"
"QComboBox QAbstractItemView \n"
"{\n"
"    outline: 0px solid gray;  /*\u53d6\u6d88\u9009\u4e2d\u865a\u7ebf*/\n"
"    border: 1px solid rgb(31,156,220);  \n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(45,45,45);   \n"
"    selection-background-color: rgb(90,90,90);   \n"
"	border-radius:3px;\n"
"	\n"
"}\n"
" /*\u9009\u4e2d\u6bcf\u4e00\u9879\u9ad8\u5ea6*/\n"
"QComboBox QAbs"
                        "tractItemView::item\n"
" { \n"
"	height: 25px;  \n"
" }\n"
"/*\u9009\u4e2d\u6bcf\u4e00\u9879\u7684\u5b57\u4f53\u989c\u8272\u548c\u80cc\u666f\u989c\u8272*/\n"
"QComboBox QAbstractItemView::item:selected \n"
"{\n"
"    color: rgb(31,163,246);\n"
"	background-color: rgb(90,90,90); \n"
"}\n"
" /*\u4e0b\u62c9\u7bad\u5934\u7684\u8fb9\u6846*/\n"
"QComboBox::drop-down \n"
"{\n"
"	border:none;\n"
"}\n"
" /*\u4e0b\u62c9\u7bad\u5934\u6837\u5f0f*/\n"
"QComboBox::down-arrow \n"
"{\n"
"    right:8px;/*\u63a7\u5236\u7bad\u5934\u5de6\u53f3\u504f\u79fb*/\n"
"    width: 12px;  \n"
"    height: 12px;   \n"
"	image:url(:/icon/arrow-down.png)\n"
"}\n"
" /*\u4e0b\u62c9\u7bad\u5934\u70b9\u51fb\u6837\u5f0f*/\n"
"")

        self.verticalLayout_2.addWidget(self.checkPattermBox)

        self.label_7 = QLabel(self.uartPage)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet(u"QLabel\n"
"{\n"
"	color:rgb(255,255,255);\n"
"}")
        self.label_7.setFrameShadow(QFrame.Plain)
        self.label_7.setTextFormat(Qt.PlainText)

        self.verticalLayout_2.addWidget(self.label_7)

        self.stopLenBox = QComboBox(self.uartPage)
        self.stopLenBox.addItem("")
        self.stopLenBox.addItem("")
        self.stopLenBox.addItem("")
        self.stopLenBox.setObjectName(u"stopLenBox")
        self.stopLenBox.setMinimumSize(QSize(0, 0))
        self.stopLenBox.setMaximumSize(QSize(16777215, 16777215))
        self.stopLenBox.setStyleSheet(u"QComboBox\n"
"{\n"
"	border-radius:3px;\n"
"	background-color:rgba(60,60,60,200);\n"
"    color:rgb(255,255,255);\n"
"    border:0px ;\n"
"	padding-top: 2px;\n"
"	padding-left: 2px;\n"
"}\n"
"QComboBox:disabled\n"
"{\n"
"	background-color:rgba(50,50,50,200);\n"
"    color:rgb(160,160,160);\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"	background-color:rgba(45,45,45,200);\n"
"	border:1px solid rgb(31,156,220) ;\n"
"}\n"
"/*\u70b9\u51fbcombox\u7684\u6837\u5f0f*/\n"
"QComboBox:on\n"
"{\n"
"	border-radius:3px;\n"
"    color:rgb(255,255,255);\n"
"    border:1px solid rgb(31,156,220) ;\n"
"}\n"
"/*\u4e0b\u62c9\u6846\u7684\u6837\u5f0f*/\n"
"QComboBox QAbstractItemView \n"
"{\n"
"    outline: 0px solid gray;  /*\u53d6\u6d88\u9009\u4e2d\u865a\u7ebf*/\n"
"    border: 1px solid rgb(31,156,220);  \n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(45,45,45);   \n"
"    selection-background-color: rgb(90,90,90);   \n"
"	border-radius:3px;\n"
"	\n"
"}\n"
" /*\u9009\u4e2d\u6bcf\u4e00\u9879\u9ad8\u5ea6*/\n"
"QComboBox QAbs"
                        "tractItemView::item\n"
" { \n"
"	height: 25px;  \n"
" }\n"
"/*\u9009\u4e2d\u6bcf\u4e00\u9879\u7684\u5b57\u4f53\u989c\u8272\u548c\u80cc\u666f\u989c\u8272*/\n"
"QComboBox QAbstractItemView::item:selected \n"
"{\n"
"    color: rgb(31,163,246);\n"
"	background-color: rgb(90,90,90); \n"
"}\n"
" /*\u4e0b\u62c9\u7bad\u5934\u7684\u8fb9\u6846*/\n"
"QComboBox::drop-down \n"
"{\n"
"	border:none;\n"
"}\n"
" /*\u4e0b\u62c9\u7bad\u5934\u6837\u5f0f*/\n"
"QComboBox::down-arrow \n"
"{\n"
"    right:8px;/*\u63a7\u5236\u7bad\u5934\u5de6\u53f3\u504f\u79fb*/\n"
"    width: 12px;  \n"
"    height: 12px;   \n"
"	image:url(:/icon/arrow-down.png)\n"
"}\n"
" /*\u4e0b\u62c9\u7bad\u5934\u70b9\u51fb\u6837\u5f0f*/\n"
"")

        self.verticalLayout_2.addWidget(self.stopLenBox)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_2)

        self.connectSetWidget.addWidget(self.uartPage)
        self.wlanPage = QWidget()
        self.wlanPage.setObjectName(u"wlanPage")
        self.formLayout_3 = QFormLayout(self.wlanPage)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(self.wlanPage)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setStyleSheet(u"QLabel\n"
"{\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout_4.addWidget(self.label_8)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = QLineEdit(self.wlanPage)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setStyleSheet(u"QWidget{\n"
"	border-radius: 6px;\n"
"	background-color:rgba(60,60,60,200);\n"
"	border:0px ;\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.wlanPage)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        self.lineEdit_2.setStyleSheet(u"QWidget{\n"
"	border-radius: 6px;\n"
"	background-color:rgba(60,60,60,200);\n"
"	border:0px ;\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.wlanPage)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy1.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy1)
        self.lineEdit_3.setStyleSheet(u"QWidget{\n"
"	border-radius: 6px;\n"
"	background-color:rgba(60,60,60,200);\n"
"	border:0px ;\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout_2.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.wlanPage)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy1.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy1)
        self.lineEdit_4.setStyleSheet(u"QWidget{\n"
"	border-radius: 6px;\n"
"	background-color:rgba(60,60,60,200);\n"
"	border:0px ;\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout_2.addWidget(self.lineEdit_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.label_10 = QLabel(self.wlanPage)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setStyleSheet(u"QLabel\n"
"{\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout_4.addWidget(self.label_10)

        self.lineEdit_5 = QLineEdit(self.wlanPage)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy1.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy1)
        self.lineEdit_5.setStyleSheet(u"QWidget{\n"
"	border-radius: 6px;\n"
"	background-color:rgba(60,60,60,200);\n"
"	border:0px ;\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout_4.addWidget(self.lineEdit_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.formLayout_3.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_4)

        self.connectSetWidget.addWidget(self.wlanPage)

        self.verticalLayout.addWidget(self.connectSetWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.connectPushButton = QPushButton(self.frame)
        self.connectPushButton.setObjectName(u"connectPushButton")
        sizePolicy1.setHeightForWidth(self.connectPushButton.sizePolicy().hasHeightForWidth())
        self.connectPushButton.setSizePolicy(sizePolicy1)
        self.connectPushButton.setMinimumSize(QSize(0, 50))
        self.connectPushButton.setStyleSheet(u"QPushButton\n"
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
        self.connectPushButton.setCheckable(False)
        self.connectPushButton.setChecked(False)
        self.connectPushButton.setAutoRepeat(False)
        self.connectPushButton.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.connectPushButton)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout_4.addWidget(self.frame)

        QWidget.setTabOrder(self.connectWaySelectBox, self.refreshButton)
        QWidget.setTabOrder(self.refreshButton, self.portNumBox)
        QWidget.setTabOrder(self.portNumBox, self.baudRateBox)
        QWidget.setTabOrder(self.baudRateBox, self.dataLenBox)
        QWidget.setTabOrder(self.dataLenBox, self.checkPattermBox)
        QWidget.setTabOrder(self.checkPattermBox, self.stopLenBox)
        QWidget.setTabOrder(self.stopLenBox, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        QWidget.setTabOrder(self.lineEdit_5, self.connectPushButton)

        self.retranslateUi(ConnectWindow)

        self.connectSetWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(ConnectWindow)
    # setupUi

    def retranslateUi(self, ConnectWindow):
        ConnectWindow.setWindowTitle(QCoreApplication.translate("ConnectWindow", u"Form", None))
        self.label.setText(QCoreApplication.translate("ConnectWindow", u"\u8fde\u63a5\u65b9\u5f0f", None))
        self.connectWaySelectBox.setItemText(0, QCoreApplication.translate("ConnectWindow", u"UART", None))
        self.connectWaySelectBox.setItemText(1, QCoreApplication.translate("ConnectWindow", u"WIFI", None))

        self.label_5.setText(QCoreApplication.translate("ConnectWindow", u"\u4e32\u53e3\u53f7", None))
        self.refreshButton.setText(QCoreApplication.translate("ConnectWindow", u"...", None))
        self.label_3.setText(QCoreApplication.translate("ConnectWindow", u"\u6ce2\u7279\u7387", None))
        self.baudRateBox.setItemText(0, QCoreApplication.translate("ConnectWindow", u"921600", None))
        self.baudRateBox.setItemText(1, QCoreApplication.translate("ConnectWindow", u"9600", None))
        self.baudRateBox.setItemText(2, QCoreApplication.translate("ConnectWindow", u"115200", None))
        self.baudRateBox.setItemText(3, QCoreApplication.translate("ConnectWindow", u"1500000", None))

        self.label_4.setText(QCoreApplication.translate("ConnectWindow", u"\u6570\u636e\u4f4d", None))
        self.dataLenBox.setItemText(0, QCoreApplication.translate("ConnectWindow", u"8", None))
        self.dataLenBox.setItemText(1, QCoreApplication.translate("ConnectWindow", u"5", None))
        self.dataLenBox.setItemText(2, QCoreApplication.translate("ConnectWindow", u"6", None))
        self.dataLenBox.setItemText(3, QCoreApplication.translate("ConnectWindow", u"7", None))

        self.label_6.setText(QCoreApplication.translate("ConnectWindow", u"\u6821\u9a8c\u4f4d", None))
        self.checkPattermBox.setItemText(0, QCoreApplication.translate("ConnectWindow", u"\u65e0\u6821\u9a8c", None))
        self.checkPattermBox.setItemText(1, QCoreApplication.translate("ConnectWindow", u"\u5947\u6821\u9a8c", None))
        self.checkPattermBox.setItemText(2, QCoreApplication.translate("ConnectWindow", u"\u5076\u6821\u9a8c", None))

        self.label_7.setText(QCoreApplication.translate("ConnectWindow", u"\u505c\u6b62\u4f4d", None))
        self.stopLenBox.setItemText(0, QCoreApplication.translate("ConnectWindow", u"1", None))
        self.stopLenBox.setItemText(1, QCoreApplication.translate("ConnectWindow", u"1.5", None))
        self.stopLenBox.setItemText(2, QCoreApplication.translate("ConnectWindow", u"2", None))

        self.label_8.setText(QCoreApplication.translate("ConnectWindow", u"IP", None))
        self.label_10.setText(QCoreApplication.translate("ConnectWindow", u"PORT", None))
        self.connectPushButton.setText(QCoreApplication.translate("ConnectWindow", u"\u8fde\u63a5", None))
    # retranslateUi

