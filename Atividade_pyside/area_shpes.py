import sys
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel, QLineEdit
from PySide6.QtGui import QPixmap


class Shape():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        