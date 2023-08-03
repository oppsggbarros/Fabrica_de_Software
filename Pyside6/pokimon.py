import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("pikomons")
        self.setGeometry(100, 100, 300, 150)

        self.result_label = QLabel(self)
        self.result_label.setGeometry(10, 90, 280, 30)

        self.button_Pokemon1 = QPushButton("Pokemon1", self)
        self.button_pokemon1.setGeometry(190, 10, 100, 70)
        self.button_pokemon1.clicked.connect(self.pokemon1)

    def pokemon1(self):
        
        self.result_label.setPixmap("imagem.jpg")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
