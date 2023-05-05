import threading

from PySide6.QtCore import QTimer


class Terminal:
    def __init__(self):
        self.messageServer = None
        self.ui = None
        self.timer = QTimer()
        self.timer.setInterval(20)
        self.timer.timeout.connect(self.appendText)
        self.str = ""
        self.lock = threading.Lock()

    def timerStart(self):
        self.timer.start(20)

    def registerUi(self, ui):
        self.ui = ui
        self.ui.sendButton.clicked.connect(self.send)

    def registerMessageServer(self, server):
        self.messageServer = server

    def inputData(self, data):
        self.lock.acquire()
        self.str = self.str + str(data.replace(b'\x00', b''), 'utf-8')
        self.lock.release()

    def outputData(self):
        return self.ui.inputText.toPlainText()

    def appendText(self):
        self.lock.acquire()
        if self.str != "":
            self.ui.outputText.insertPlainText(self.str)
            self.str = ""
        self.lock.release()
        self.ui.outputText.verticalScrollBar().setValue(self.ui.outputText.verticalScrollBar().maximum())

    def send(self):
        if self.messageServer is not None:
            print(self.outputData().encode('utf-8'))
            self.messageServer.send(self.outputData().encode('utf-8'))
            self.ui.inputText.clear()
