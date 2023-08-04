import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Check Box")
        self.label = QLabel("Aceita casar comigo ?")
        self.ck = QCheckBox("Aceito")
        self.label2 = QLabel()
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.ck)
        layout.addWidget(self.label2)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        self.ck.stateChanged.connect(self.state)
        
    def state(self, s):
        print(s)
        if s == 2:
            self.label2.setText("NÃO ACEITO")
        else:
            self.label2.setText("")


app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()