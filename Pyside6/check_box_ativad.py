import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QVBoxLayout, QWidget, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Check box")
        
        self.setWindowTitle("Cadastro")
        self.setGeometry(200, 250, 200, 250)

        self.label1 = QLabel("Nome:", self)
        self.label1.setGeometry(10, 10, 80, 30)

        self.input1 = QLineEdit(self)
        self.input1.setGeometry(100, 10, 80, 30)

        self.label2 = QLabel("CPF:", self)
        self.label2.setGeometry(10, 50, 80, 30)

        self.input2 = QLineEdit(self)
        self.input2.setGeometry(100, 50, 80, 30)
        
        self.label3 = QLabel("Endereço:", self)
        self.label3.setGeometry(10, 90, 80, 30)
        
        self.input3 = QLineEdit(self)
        self.input3.setGeometry(100, 90, 80, 30)
        
        self.button = QPushButton("Cadastrar", self)
        self.button.setGeometry(100, 180, 80, 30)
        
        self.ck = QCheckBox("Masculino")
        self.ck.setGeometry(10, 130, 80, 30)
        
        self.label2 = QLabel()
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.ck)
        
        container = QWidget()
        container.setLayout(layout)
        
        
        
app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()