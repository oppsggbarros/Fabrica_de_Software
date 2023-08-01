'''from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel
import sys

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Hello World!!!")
		button = QPushButton("Jho soy um butão")
		self.setCentralWidget(button)
		button.clicked.connect(self.imprimir)
	def imprimir(self):
		print("Gabriel")


app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()'''

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel
from PyQt5.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Progamin")
        self.setFixedSize(600,400)
        self.lbl = QLabel("Hello World")
        font = self.lbl.font()
        font.setPointSize(35)
        self.lbl.setFont(font)
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.lbl)


app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()