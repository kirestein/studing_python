import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QFrame, QVBoxLayout, QLabel
from PySide6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('QLineEdit')
        self.setFixedSize(QSize(300, 300))
        
        #? Criamos o LineEdit atribuindo ele a uma variável
        self.input = QLineEdit()
        self.input.setPlaceholderText('Digite algo')
        self.lbl = QLabel('Digite algo')
        
        #? Criamos um layout e adicionamos o LineEdit a ele
        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.input)
        
        #? Criamos a janela e adicionamos o layout a ele
        container = QFrame()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
        self.input.textChanged.connect(self.text_changed)
        
    #? Função para alterar o texto do QLabel
    def text_changed(self):
        self.lbl.setText(self.input.text())
        
        
app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec()