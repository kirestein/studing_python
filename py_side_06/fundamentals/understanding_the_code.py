
#? Importing the components we need
from PySide6.QtWidgets import QApplication, QMainWindow

#? The sys module is responsible for processing command line arguments

app = QApplication(sys.argv)

#? Create a window
win = QMainWindow()
win.show()

#? Start the event loop
app.exec()