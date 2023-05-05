from PySide6.QtWidgets import QApplication

from BIN.message import MessageServer
from BIN.terminal import Terminal
from ui import FsMainWindow
import sys


def main():
    app = QApplication(sys.argv)
    window = FsMainWindow()

    terminal = Terminal()
    terminal.registerUi(window.terminalWin.ui)

    terminal.timerStart()
    messageServer = MessageServer()
    messageServer.registerProcessor(terminal)
    messageServer.start()

    terminal.registerMessageServer(messageServer)

    window.show()
    ret = app.exec()
    messageServer.stop()
    sys.exit(ret)


if __name__ == "__main__":
    main()
