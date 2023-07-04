"""   
    Crie um programa que contenha  uma lineEdit para informar 
    a largura, outro para informar a altura e um para o comprimento.
    Esse programa deverá calcular o metro cúbico de uma área  e 
    resultado deverá ser mostrado uma Label.
    Utilize o QvBoxLayout para deixar os dados organizados.
    Formula:
    A x C x L.
    Altura x comprimento x Largura
    
    
"""

import sys
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QFrame, QVBoxLayout, QLabel, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(300, 300))
        
        self.setWindowTitle("Cálculo do metro Cúbico")
        #? Estamos criando os widgets
        self.altura = QLineEdit()
        self.altura.setPlaceholderText('Digite a altura')
        self.largura = QLineEdit()
        self.largura.setPlaceholderText('Digite a largura')
        self.comprimento = QLineEdit()
        self.comprimento.setPlaceholderText('Digite o comprimento')
        self.resultado = QLabel()
        self.btn_calcular = QPushButton('Calcular')
        
        
        #? Estamos adicionando os widgets ao layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.altura)
        self.layout.addWidget(self.largura)
        self.layout.addWidget(self.comprimento)
        self.layout.addWidget(self.resultado)
        self.layout.addWidget(self.btn_calcular)
        
        self.container = QFrame()
        #? Estamos adicionando o layout ao container
        self.container.setLayout(self.layout)
        
        #? Aqui estamos atribuindo a função volume ao botão
        self.btn_calcular.clicked.connect(self.volume)
        #? Estamos adicionando o container ao centralWidget(nossa janela)
        self.setCentralWidget(self.container)
        
        #? Estamos conectando os dados de entrada com a função volume
        # self.altura.textChanged.connect(self.volume)
        # self.largura.textChanged.connect(self.volume)
        # self.comprimento.textChanged.connect(self.volume)
        
        
    def volume(self):
        altura = float(self.altura.text())
        largura = float(self.largura.text())
        comprimento = float(self.comprimento.text())
        if altura and largura and comprimento:
            resultado = altura * largura * comprimento
            self.resultado.setText(f'Volume: {str(resultado)}')
        
       
        
        

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()