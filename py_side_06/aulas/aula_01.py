# from PySide6.QTWidgets import QApplication, QWidget
from PySide6.QtWidgets import QApplication, QWidget

import sys

app = QApplication(sys.argv)

win = QWidget()
win.show()

app.exec()

