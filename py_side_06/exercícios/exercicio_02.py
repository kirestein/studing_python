""""
CRIE UM PROGRAMA QUE RECEBA DADOS DE UM CLIENTE.
NESSE PROGRAMA DEVE TER UM LINE EDIT PARA INFORMAR O NOME.
COMBO BOX PARA INFORMAR SEXO.
LINE EDIT PARA CONSULTA DE CEP
LINEEDIT BAIRRO, CIDADE, LOUGRADOURO DEVE SER PREENHCIDO AUTOMATICAMENTE.

"""

import pycep_correios


import sys
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout,
                               QComboBox, QLabel,QLineEdit, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Endereço completo")
        
        
        #self.txt_cep.editingFinished.connect(self.buscar_cep)

    def buscar_cep(self):
        pass
        
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()