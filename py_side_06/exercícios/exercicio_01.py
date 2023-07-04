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
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Cálculo do metro Cúbico")
       
        
        

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()