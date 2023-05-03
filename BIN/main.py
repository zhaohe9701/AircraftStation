from PySide6.QtWidgets import QApplication
from ui import FsMainWindow
import sys


def main():
    app = QApplication(sys.argv)
    window = FsMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
