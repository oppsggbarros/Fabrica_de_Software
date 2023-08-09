import sys
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel, QLineEdit
from PySide6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastro")
        self.setGeometry(100, 100, 300, 200)

        self.label1 = QLabel("Nome:", self)
        self.label1.setGeometry(10, 10, 80, 30)

        self.input1 = QLineEdit(self)
        self.input1.setGeometry(100, 10, 80, 30)

        self.label2 = QLabel("CPF:", self)
        self.label2.setGeometry(10, 50, 80, 30)

        self.input2 = QLineEdit(self)
        self.input2.setGeometry(100, 50, 80, 30)
        
        self.label3 = QLabel("Fone:", self)
        self.label3.setGeometry(10, 90, 80, 30)
        
        self.input3 = QLineEdit(self)
        self.input3.setGeometry(100, 90, 80, 30)
        
        self.label4 = QLabel("Endereço:", self)
        self.label4.setGeometry(10, 130, 80, 30)
        
        self.input4 = QLineEdit(self)
        self.input4.setGeometry(100, 130, 80, 30)

        self.button = QPushButton("Cadastrar", self)
        self.button.setGeometry(190, 10, 100, 70)
        self.button.clicked.connect(self.cadastro)
        
    def cadastro(self):
        self.secodary_window = SecondaryWindow()
        self.secodary_window.show()
class SecondaryWindow(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Janela Secundária")
        self.setGeometry(200, 200, 500, 300) 
        
        self.label5 = QLabel("Nome:", self)
        self.label5.setGeometry
        
app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()