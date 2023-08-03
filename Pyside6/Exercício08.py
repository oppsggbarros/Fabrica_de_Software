import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculo de horas trabalhadas")
        self.setGeometry(100, 100, 330, 150)

        self.label1 = QLabel("O quanto você\nganha por hora:", self)
        self.label1.setGeometry(5, 10, 90, 30)

        self.input1 = QLineEdit(self)
        self.input1.setGeometry(100, 10, 80, 30)
        
        self.label2 = QLabel("Quantidade de\nhoras trabalhadas\nno mês:", self)
        self.label2.setGeometry(5, 50, 90, 40)
        
        self.input2 = QLineEdit(self)
        self.input2.setGeometry(100, 50, 80, 30)

        self.result_label = QLabel(self)
        self.result_label.setGeometry(10, 90, 280, 30)

        self.button = QPushButton("Calcular", self)
        self.button.setGeometry(190, 10, 100, 70)
        self.button.clicked.connect(self.calcular_soma)

    def calcular_soma(self):
        num1 = int(self.input1.text())
        num2 = int(self.input2.text())
        total = num1*num2
        self.result_label.setText(f"A quantidade que ele ganhou no mês foi de {total} Reais")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
