import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Média das notas")
        self.setGeometry(100, 100, 300, 200)

        self.label1 = QLabel("Nota 1:", self)
        self.label1.setGeometry(10, 10, 80, 30)

        self.input1 = QLineEdit(self)
        self.input1.setGeometry(100, 10, 80, 30)

        self.label2 = QLabel("Nota 2:", self)
        self.label2.setGeometry(10, 50, 80, 30)

        self.input2 = QLineEdit(self)
        self.input2.setGeometry(100, 50, 80, 30)
        
        self.label3 = QLabel("Nota 3:", self)
        self.label3.setGeometry(10, 90, 80, 30)
        
        self.input3 = QLineEdit(self)
        self.input3.setGeometry(100, 90, 80, 30)
        
        self.label4 = QLabel("Nota 4:", self)
        self.label4.setGeometry(10, 130, 80, 30)
        
        self.input4 = QLineEdit(self)
        self.input4.setGeometry(100, 130, 80, 30)

        self.result_label = QLabel(self)
        self.result_label.setGeometry(10, 90, 280, 30)

        self.button = QPushButton("Calcular", self)
        self.button.setGeometry(190, 10, 100, 70)
        self.button.clicked.connect(self.calcular_soma)

    def calcular_soma(self):
        num1 = int(self.input1.text())
        num2 = int(self.input2.text())
        num3 = int(self.input3.text())
        num4 = int(self.input4.text())
        media = (num1+num2+num3+num4)/4
        self.result_label.setText(f"A soma é: {media}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
