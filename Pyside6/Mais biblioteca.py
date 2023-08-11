import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDial, QVBoxLayout, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurações da janela principal
        self.setWindowTitle("Exemplo de QDial")
        self.setGeometry(100, 100, 300, 200)

        # Cria um layout vertical
        layout = QVBoxLayout()

        # Cria um widget QDial
        self.dial = QDial()

        # Adiciona o QDial ao layout
        layout.addWidget(self.dial)

        # Cria um widget para conter o layout e define-o como o widget central da janela
        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

        # Conecta o sinal de alteração de valor do QDial a um método
        self.dial.valueChanged.connect(self.dial_value_changed)

    # Método chamado quando o valor do QDial é alterado
    def dial_value_changed(self, value):
        print("Valor selecionado:", value)

# Cria uma instância da aplicação
app = QApplication(sys.argv)

# Cria uma instância da janela personalizada
window = MyWindow()

# Exibe a janela
window.show()

# Inicia o loop de eventos da aplicação
sys.exit(app.exec_())

