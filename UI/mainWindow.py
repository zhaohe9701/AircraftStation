# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowTEDHnq.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLineEdit,
    QMainWindow, QSizePolicy, QSpacerItem, QStackedWidget,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(904, 660)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 2, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalWidget_3 = QWidget(self.centralwidget)
        self.horizontalWidget_3.setObjectName(u"horizontalWidget_3")
        self.horizontalWidget_3.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(70, 70, 70);\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(8, -1, -1, -1)
        self.toolButton_4 = QToolButton(self.horizontalWidget_3)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setStyleSheet(u"/* \u9ed8\u8ba4 */\n"
"QToolButton{   \n"
"	border-top: 0px outset transparent;  \n"
"	border-bottom: 0px outset transparent;\n"
"	border-right: 0px outset transparent;\n"
"	border-left: 0px outset transparent;\n"
"	border-radius: 6px;\n"
"    min-width: 30px;  \n"
"    min-height: 20px;\n"
"}\n"
"\n"
"/* \u9f20\u6807\u60ac\u505c */\n"
"QToolButton:hover{\n"
"	background-color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"/* \u70b9\u51fb\u548c\u6309\u4e0b */\n"
"QToolButton:pressed,QToolButton:checked{\n"
"	background-color: rgb(90, 90, 90);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../icon/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setIconSize(QSize(30, 18))
        self.toolButton_4.setCheckable(True)
        self.toolButton_4.setChecked(False)
        self.toolButton_4.setAutoRepeat(False)
        self.toolButton_4.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.toolButton_4)

        self.horizontalSpacer = QSpacerItem(38, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(self.horizontalWidget_3)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(200, 25))
        self.lineEdit.setStyleSheet(u"QWidget{\n"
"	border-radius: 6px;\n"
"	background-color: rgb(80, 80, 80);\n"
"	border:0.5px solid rgb(130,130,130);\n"
"	color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.horizontalWidget_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalWidget_2 = QWidget(self.centralwidget)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        self.verticalWidget_2.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(51, 51, 51);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.connectWindowButton = QToolButton(self.verticalWidget_2)
        self.connectWindowButton.setObjectName(u"connectWindowButton")
        self.connectWindowButton.setMinimumSize(QSize(42, 40))
        self.connectWindowButton.setCursor(QCursor(Qt.ArrowCursor))
        self.connectWindowButton.setAcceptDrops(False)
        self.connectWindowButton.setToolTipDuration(-1)
        self.connectWindowButton.setStyleSheet(u"/* \u9ed8\u8ba4 */\n"
"QToolButton{   \n"
"		border-top: 0px outset transparent;  \n"
"	border-bottom: 0px outset transparent;\n"
"	border-right: 0px outset transparent;\n"
"	border-left: 2px outset transparent;\n"
"    min-width: 40px;  \n"
"    min-height: 40px;\n"
"}\n"
"\n"
"/* \u9f20\u6807\u60ac\u505c */\n"
"QToolButton:hover{\n"
"	border-left: 2px outset rgb(255, 255, 255); \n"
"}\n"
"\n"
"/* \u70b9\u51fb\u548c\u6309\u4e0b */\n"
"QToolButton:pressed,QToolButton:checked{\n"
"	border-left: 2px outset rgb(255, 255, 255); \n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../icon/connect_g.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u"../icon/connect_w.png", QSize(), QIcon.Normal, QIcon.On)
        self.connectWindowButton.setIcon(icon1)
        self.connectWindowButton.setIconSize(QSize(40, 40))
        self.connectWindowButton.setCheckable(True)
        self.connectWindowButton.setAutoExclusive(True)
        self.connectWindowButton.setPopupMode(QToolButton.DelayedPopup)
        self.connectWindowButton.setArrowType(Qt.NoArrow)

        self.verticalLayout_3.addWidget(self.connectWindowButton)

        self.controlWindowButton = QToolButton(self.verticalWidget_2)
        self.controlWindowButton.setObjectName(u"controlWindowButton")
        self.controlWindowButton.setStyleSheet(u"/* \u9ed8\u8ba4 */\n"
"QToolButton{   \n"
"		border-top: 0px outset transparent;  \n"
"	border-bottom: 0px outset transparent;\n"
"	border-right: 0px outset transparent;\n"
"	border-left: 2px outset transparent;\n"
"    min-width: 40px;  \n"
"    min-height: 40px;\n"
"}\n"
"\n"
"/* \u9f20\u6807\u60ac\u505c */\n"
"QToolButton:hover{\n"
"	border-left: 2px outset rgb(255, 255, 255); \n"
"}\n"
"\n"
"/* \u70b9\u51fb\u548c\u6309\u4e0b */\n"
"QToolButton:pressed,QToolButton:checked{\n"
"	border-left: 2px outset rgb(255, 255, 255); \n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../icon/controller_g.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u"../icon/controller_w.png", QSize(), QIcon.Normal, QIcon.On)
        self.controlWindowButton.setIcon(icon2)
        self.controlWindowButton.setIconSize(QSize(40, 40))
        self.controlWindowButton.setCheckable(True)
        self.controlWindowButton.setAutoExclusive(True)
        self.controlWindowButton.setArrowType(Qt.NoArrow)

        self.verticalLayout_3.addWidget(self.controlWindowButton)

        self.positionWindowButton = QToolButton(self.verticalWidget_2)
        self.positionWindowButton.setObjectName(u"positionWindowButton")
        self.positionWindowButton.setStyleSheet(u"/* \u9ed8\u8ba4 */\n"
"QToolButton{   \n"
"		border-top: 0px outset transparent;  \n"
"	border-bottom: 0px outset transparent;\n"
"	border-right: 0px outset transparent;\n"
"	border-left: 2px outset transparent;\n"
"    min-width: 40px;  \n"
"    min-height: 40px;\n"
"}\n"
"\n"
"/* \u9f20\u6807\u60ac\u505c */\n"
"QToolButton:hover{\n"
"	border-left: 2px outset rgb(255, 255, 255); \n"
"}\n"
"\n"
"/* \u70b9\u51fb\u548c\u6309\u4e0b */\n"
"QToolButton:pressed,QToolButton:checked{\n"
"	border-left: 2px outset rgb(255, 255, 255); \n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../icon/satellite_g.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u"../icon/satellite_w.png", QSize(), QIcon.Normal, QIcon.On)
        icon3.addFile(u"../icon/satellite_w.png", QSize(), QIcon.Selected, QIcon.Off)
        icon3.addFile(u"../icon/satellite_w.png", QSize(), QIcon.Selected, QIcon.On)
        self.positionWindowButton.setIcon(icon3)
        self.positionWindowButton.setIconSize(QSize(40, 40))
        self.positionWindowButton.setCheckable(True)
        self.positionWindowButton.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.positionWindowButton)

        self.terminalWindowButton = QToolButton(self.verticalWidget_2)
        self.terminalWindowButton.setObjectName(u"terminalWindowButton")
        self.terminalWindowButton.setStyleSheet(u"/* \u9ed8\u8ba4 */\n"
"QToolButton{   \n"
"		border-top: 0px outset transparent;  \n"
"	border-bottom: 0px outset transparent;\n"
"	border-right: 0px outset transparent;\n"
"	border-left: 2px outset transparent;\n"
"    min-width: 40px;  \n"
"    min-height: 40px;\n"
"}\n"
"\n"
"/* \u9f20\u6807\u60ac\u505c */\n"
"QToolButton:hover{\n"
"	border-left: 2px outset rgb(255, 255, 255); \n"
"}\n"
"\n"
"/* \u70b9\u51fb\u548c\u6309\u4e0b */\n"
"QToolButton:pressed,QToolButton:checked{\n"
"	border-left: 2px outset rgb(255, 255, 255); \n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"../icon/terminal_g.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u"../icon/terminal_w.png", QSize(), QIcon.Normal, QIcon.On)
        self.terminalWindowButton.setIcon(icon4)
        self.terminalWindowButton.setIconSize(QSize(40, 40))
        self.terminalWindowButton.setCheckable(True)
        self.terminalWindowButton.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.terminalWindowButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.verticalWidget_2)

        self.MainStackedWidget = QStackedWidget(self.centralwidget)
        self.MainStackedWidget.setObjectName(u"MainStackedWidget")
        self.MainStackedWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.MainStackedWidget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(30, 30, 30);\n"
"}")
        self.MainStackedWidget.setLineWidth(1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.MainStackedWidget.addWidget(self.page)

        self.horizontalLayout_2.addWidget(self.MainStackedWidget)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalWidget_4 = QWidget(self.centralwidget)
        self.horizontalWidget_4.setObjectName(u"horizontalWidget_4")
        self.horizontalWidget_4.setMinimumSize(QSize(0, 12))
        self.horizontalWidget_4.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(56, 136, 221);\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.verticalLayout.addWidget(self.horizontalWidget_4)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.connectWindowButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.controlWindowButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.positionWindowButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.terminalWindowButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

