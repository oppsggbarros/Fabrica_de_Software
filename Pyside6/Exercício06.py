import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Área do Círculo")
        self.setGeometry(100, 100, 300, 150)

        self.label1 = QLabel("Informe o raio:", self)
        self.label1.setGeometry(5, 10, 90, 30)

        self.input1 = QLineEdit(self)
        self.input1.setGeometry(100, 10, 80, 30)

        self.result_label = QLabel(self)
        self.result_label.setGeometry(10, 90, 280, 30)

        self.button = QPushButton("Calcular", self)
        self.button.setGeometry(190, 10, 100, 70)
        self.button.clicked.connect(self.calcular_soma)

    def calcular_soma(self):
        num1 = int(self.input1.text())
        if num1 <= 0:
            self.result_label.setText("Não existe Raio negativo")
        else:
            area = num1**2/3
            self.result_label.setText(f"A área do círculo é {area}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
