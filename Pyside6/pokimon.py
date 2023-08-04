from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFrame
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,600)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Pokedex")
        
        self.button_snivy = QPushButton('Snivy')
        self.button_bulbasaur = QPushButton('bulbasaur')
        
        self.image_frame = QFrame(self)
        self.image_frame.setFrameShape(QFrame.Box)
        self.image_frame.setFixedSize(600,400)
        self.image_frame.setLayout(QVBoxLayout())
        
        self.image_label = QLabel(self.image_frame)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_frame.layout().addWidget(self.image_label)
        
        layout = QVBoxLayout()
        layout.addWidget(self.button_snivy)
        layout.addWidget(self.button_bulbasaur)
        layout.addWidget(self.image_frame)
        
        self.button_snivy.clicked.connect(self.display_snivy)
        self.button_bulbasaur.clicked.connect(self.display_bulbasaur)
        
        self.setLayout(layout)
    
    def display_snivy(self):
        pixmap = QPixmap('Snivy.jpg')
        self.image(pixmap)
    
    def display_bulbasaur(self):
        pixmap = QPixmap('bulbasaur.jpg')
        self.image(pixmap)
        
    def image(self, pixmap):
        scale_pixmap = pixmap.scaled(600,400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(scale_pixmap)
        
       
        
    

app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()