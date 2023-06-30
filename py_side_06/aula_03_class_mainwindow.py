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
        button = QPushButton("Click Me!")
        self.setCentralWidget(button)
        
        
        button.clicked.connect(self.show_it)
        
        
        
    def show_it(self):
        print('Testing the button')
        
    

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec()