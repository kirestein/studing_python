from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Organization in classes')
        
        self.setFixedSize(QSize(500, 500))
        #? creating a button
        self.btn = QPushButton('Download')
        
        #? creating a layout
        layout = QVBoxLayout()
        #? adding the button to the layout
        layout.addWidget(self.btn)
        
        #? creating a container
        container = QWidget()
        #? adding the layout to the container
        container.setLayout(layout)
        #? adding the container to the central widget
        self.setCentralWidget(container)
        
        self.btn.clicked.connect(self.download)
        
    def download(self):
        print('Downloading...')
        
        
        
app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec()