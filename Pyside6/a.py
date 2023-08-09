import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Janela Principal")
        self.setFixedSize(800,400)

        self.button = QPushButton("Abrir janela secundária", self)
        self.button.clicked.connect(self.open_secondary_window)
        self.button.setGeometry(100,100,500,100)
        

    def open_secondary_window(self):
        self.secondary_window = SecondaryWindow()
        self.secondary_window.show()

class SecondaryWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Janela Secundária")
        self.setGeometry(200, 200, 500, 300)

        layout = QVBoxLayout()

        label = QLabel("Bulbassalto")
        layout.addWidget(label)

        image_label = QLabel(self)
        pixmap = QPixmap("bulbasaur.jpg")  # Cria o objeto QPixmap a partir do arquivo de imagem
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)

        close_button = QPushButton("Fechar", self)
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()
