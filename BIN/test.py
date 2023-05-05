from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit
from PySide6.QtCore import Qt


class MyTextEdit(QTextEdit):
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return and self.hasFocus():
            Func()
        else:
            super().keyPressEvent(event)


def Func():
    print("Enter key pressed while MyTextEdit has focus")


app = QApplication([])
window = QMainWindow()

text_edit = MyTextEdit()
window.setCentralWidget(text_edit)

window.show()
app.exec()
