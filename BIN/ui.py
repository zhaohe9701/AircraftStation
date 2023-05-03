from PySide6.QtWidgets import QMainWindow, QWidget
from UI.mainWindow import Ui_MainWindow
from UI.connectWindow import Ui_ConnectWindow
from UI.positionWindow import Ui_PositionWindow
from UI.terminalWindow import Ui_TerminalWindow
from BIN.map import MapWidget
from uart import uart


class FsConnectWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ConnectWindow()
        self.ui.setupUi(self)
        self.changePage()
        self.ui.connectWaySelectBox.currentTextChanged.connect(self.changePage)
        self.ui.refreshButton.clicked.connect(self.refreshUart)
        self.ui.connectPushButton.clicked.connect(self.connectAircraft)

    def changePage(self):
        if self.ui.connectWaySelectBox.currentText() == "UART":
            self.ui.connectSetWidget.setCurrentWidget(self.ui.uartPage)
        elif self.ui.connectWaySelectBox.currentText() == "WIFI":
            self.ui.connectSetWidget.setCurrentWidget(self.ui.wlanPage)

    def refreshUart(self):
        uartList = uart.findPort()
        self.ui.portNumBox.clear()
        self.ui.portNumBox.addItems(uartList)

    def connectAircraft(self):
        if self.ui.connectPushButton.text() == "连接":
            if self.ui.connectWaySelectBox.currentText() == "UART":
                self.connectByUart()
                return
        if self.ui.connectPushButton.text() == "断开":
            if self.ui.connectWaySelectBox.currentText() == "UART":
                self.closeByUart()
                return

    def connectByUart(self):
        res, errStr = uart.openPort(port=self.ui.portNumBox.currentText(),
                               baudRate=self.ui.baudRateBox.currentText(),
                               byteSize=self.ui.dataLenBox.currentText(),
                               parity=self.ui.checkPattermBox.currentText(),
                               stopBits=self.ui.stopLenBox.currentText()
                               )
        print(errStr)
        if res:
            self.ui.connectPushButton.setText("断开")

    def closeByUart(self):
        uart.closePort()
        self.ui.connectPushButton.setText("连接")

class FsTerminalWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TerminalWindow()
        self.ui.setupUi(self)




class FsPositionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PositionWindow()
        self.ui.setupUi(self)
        self.map = MapWidget()
        self.map.setUpMap(self.ui.mapWidget)


class FsMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connectWin = FsConnectWindow()
        self.positionWin = FsPositionWindow()
        self.terminalWin = FsTerminalWindow()
        self.addChildWindow()
        self.connectToFunc()

    def addChildWindow(self):
        self.ui.MainStackedWidget.addWidget(self.connectWin)
        self.ui.MainStackedWidget.addWidget(self.positionWin)
        self.ui.MainStackedWidget.addWidget(self.terminalWin)
    def showConnectWin(self):
        self.ui.MainStackedWidget.setCurrentIndex(1)

    def showPositionWin(self):
        self.ui.MainStackedWidget.setCurrentIndex(2)

    def showTerminalWin(self):
        self.ui.MainStackedWidget.setCurrentIndex(3)

    def connectToFunc(self):
        self.ui.connectWindowButton.clicked.connect(self.showConnectWin)
        self.ui.positionWindowButton.clicked.connect(self.showPositionWin)
        self.ui.terminalWindowButton.clicked.connect(self.showTerminalWin)
