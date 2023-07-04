'''
    Setando o parcialmente marcado
'''

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('checkbox')
        self.setFixedSize(QSize(500, 500))
        
        #? Widgets
        self.lbl = QLabel('Você bebe? ')
        self.ck = QCheckBox('Sim')
        self.ck.setTristate(True)
        # self.ck.setCheckState(Qt.Checked) #? seta o estado do checkbox
        self.lbl_02 = QLabel()
        
        #? Layout
        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.ck)
        layout.addWidget(self.lbl_02)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
        self.ck.stateChanged.connect(self.state)
    #? Funçaões
    def state(self, s):
        # print('Preencha o formulário abaixo: ')
        
        #? estou verificando se o checkbox está selecionado (2 = checked, 0 = unchecked)
        if s == 2:
            self.lbl_02.setText('Preencha o formulário abaixo: ')
            print(s)
        else:
            self.lbl_02.setText('')
            print(s)
            

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec()