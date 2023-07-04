'''
    Combo Box é uma lista suspensa de valores.
'''

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox, QFrame, QLabel, QVBoxLayout
from PySide6.QtCore import QSize, Qt

options = ['Selecione uma bebida','Água', 'Suco de Laranja', 'Suco de Caju', 'Refrigerante', 'Cerveja']

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('QComboBox')
        self.setFixedSize(QSize(500, 500))
        self.cb = QComboBox()
        #? Criamos uma lista com as nossas opções e adicionamos as opções ao combo box utilizando o list comprehension
        [self.cb.addItem(o) for o in options]
        
        self.cb.currentIndexChanged.connect(self.change_index)
        self.cb.currentTextChanged.connect(self.change_text)
        
        
        
        layout = QVBoxLayout()
        layout.addWidget(self.cb)
        
        
        container = QFrame()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
    def change_index(self, i):
        print(i)
        
    def change_text(self, s):
        print(s)




app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec()