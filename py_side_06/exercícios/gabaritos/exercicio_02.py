""""
CRIE UM PROGRAMA QUE RECEBA DADOS DE UM CLIENTE.
NESSE PROGRAMA DEVE TER UM LINE EDIT PARA INFORMAR O NOME.
COMBO BOX PARA INFORMAR SEXO.
LINE EDIT PARA CONSULTA DE CEP
LINEEDIT BAIRRO, CIDADE, LOUGRADOURO DEVE SER PREENHCIDO AUTOMATICAMENTE.

"""

import consulta_correios
import requests


import sys
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout,
                               QComboBox, QLabel,QLineEdit, QWidget)

opcoes = ['Selecione seu sexo','Masculino', 'Feminino', 'Prefiro não informar']

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Endereço completo")
        self.setFixedSize(QSize(400, 600))
        
        self.lbl_nome = QLabel("Nome: ")
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Digite seu nome")
        self.lbl_sexo = QLabel('Informe o seu sexo: ')
        self.cb_sexo = QComboBox()
        [self.cb_sexo.addItem(o) for o in opcoes]
        self.lbl_cep = QLabel('Informe o seu CEP: ')
        self.input_cep = QLineEdit()
        self.lbl_logradouro = QLabel('Logradouro: ')
        self.input_cep.setPlaceholderText("xxxxx-xxx")
        self.input_logradouro = QLineEdit()
        self.input_logradouro.setPlaceholderText("Digite seu logradouro")
        self.lbl_bairro = QLabel('Informe o seu bairro: ')
        self.input_bairro = QLineEdit()
        self.input_bairro.setPlaceholderText("Digite seu bairro")
        self.lbl_cidade = QLabel('Informe a sua cidade: ')
        self.input_cidade = QLineEdit()
        self.input_cidade.setPlaceholderText("Digite sua cidade")
        
        layout = QVBoxLayout()
        layout.addWidget(self.lbl_nome)
        layout.addWidget(self.input_name)
        layout.addWidget(self.lbl_sexo)
        layout.addWidget(self.cb_sexo)
        layout.addWidget(self.lbl_cep)
        layout.addWidget(self.input_cep)
        layout.addWidget(self.lbl_logradouro)
        layout.addWidget(self.input_logradouro)
        layout.addWidget(self.lbl_bairro)
        layout.addWidget(self.input_bairro)
        layout.addWidget(self.lbl_cidade)
        layout.addWidget(self.input_cidade)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
        self.input_cep.textChanged.connect(self.buscar_cep)
        
        
        
        #self.txt_cep.editingFinished.connect(self.buscar_cep)

    def buscar_cep(self):
        cep = self.input_cep.text()

        cep = cep.replace("-", "").replace(".", "").replace(" ", "")
        print(cep)

        if len(cep) == 8:
            link = f'https://viacep.com.br/ws/{cep}/json/'

            requisicao = requests.get(link)

            print(requisicao)

            address = requisicao.json()

            uf = address['uf']
            cidade = address['localidade']
            bairro = address['bairro']
            # print(address)
            self.input_logradouro.setText(address['logradouro'])
            self.input_bairro.setText(address['bairro'])
            self.input_cidade.setText(address['localidade'])
            print(f"Logradouro: {address['logradouro']}")
            print(f"Bairro: {address['bairro']}")
            print(f"Cidade: {address['localidade']}")
        else:
            self.input_logradouro.setText(address[''])
            self.input_bairro.setText(address[''])
            self.input_cidade.setText(address[''])
            print("CEP Inválido")
        
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()