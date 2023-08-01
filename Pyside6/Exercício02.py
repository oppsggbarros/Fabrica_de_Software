from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel
from PyQt5.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Progamin")
        
        self.button = QPushButton("Butão", self)
        self.setFixedSize(600,400)
        self.button.setGeometry(190, 10, 100, 70)
        self.result_label = QLabel(self)
        self.result_label.setGeometry(10, 90, 280, 30)
        
        self.button.clicked.connect(self.imprimir)
        
    def imprimir(self):
        numero = 4
        if numero % 2 == 0:
            self.result_label.setText(f"Este número é {numero} par")
        else:
            self.result_label.setText(f"Este número é {numero} impar")

app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()