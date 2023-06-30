"""
# ! Nesta aula será trabalhado o conceito de classes e vamos colocar um botão na janela para testar
"""
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My First Window")
        self.button = QPushButton("Click Me!")
        self.setCentralWidget(self.button)
        
        self.button.setCheckable(True) # ? Altera o estado do botão, o que antes retornava False agora retorna True
        self.button.clicked.connect(self.show_it)
        self.button.clicked.connect(self.button_clicked)
        
        self.setFixedSize(QSize(600, 400))
        
    def show_it(self):
        print('Testing the button')
        
    def button_clicked(self, s):
        print("Clicked", s)
        

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec()