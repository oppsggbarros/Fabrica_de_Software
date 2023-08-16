from UI_login import UI_MainWindow

import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QSizePolicy, QVBoxLayout, QWidget)
import icon_rc

class MainWindow(QMainWindow, UI_MainWindow):
    def __init__(self):
        super().__init()
        self.setupUi(self)
        self.setWindowTitle("Login")

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    w =QMainWindow()
    w.show()
    app.exec()
