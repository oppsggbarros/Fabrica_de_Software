from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Progamin")
        self.setGeometry(100, 100, 300, 150)
        
        self.label1 = QLabel("Número 1:", self)
        self.label1.setGeometry(10, 10, 80, 30)
        
        self.input1 = QLineEdit(self)
        self.input1.setGeometry(100,50,80,30)
        
        self.input2 = QLabel("Número 2:", self)
        self.input2.setGeometry(10, 50, 80, 30)
        
        self.input2 = QLineEdit(self)
        self.input2.setGeometry(100,50,80,30)
        
        self.button = QPushButton("Calcular", self)
        self.button.setGeometry(190, 10, 100, 70)
        
        self.result_label = QLabel(self)
        self.result_label.setGeometry(10, 90, 100, 70)
        self.button.clicked.connect(self.calcular_soma)

    def imprimir(self):
        num1 = int(self.input1.text())
        num2 = int(self.input2.text())
        soma = num1 + num2
        self.result_label.setText(f"A soma dos números é {soma}")
        
app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()