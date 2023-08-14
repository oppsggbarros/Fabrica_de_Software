from typing import Optional
import brazilcep
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFrame
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Busca CEPE")
        
        
        
        
        
endereco = brazilcep.get_address_from_cep('79052200')
print(endereco)
        
