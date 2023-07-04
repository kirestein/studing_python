import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Imagem')
        self.setFixedSize(QSize(500, 500))
        self.lbl = QLabel()
        self.lbl.setPixmap(QPixmap('tree.jpg'))
        self.lbl.setScaledContents(True)
        
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.setCentralWidget(self.lbl)
        
        
app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec()