import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('QLabel')
        self.setFixedSize(QSize(500, 500))
        
        self.lbl_01 = QLabel('Hello')
        #? setando o tamanho da fonte
        font = self.lbl_01.font()
        font.setPointSize(20)
        self.lbl_01.setFont(font)
        #? Setando alinhamento centralizado horizontalmente e vericalmente
        self.lbl_01.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.setCentralWidget(self.lbl_01)
        
        
        
app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec()