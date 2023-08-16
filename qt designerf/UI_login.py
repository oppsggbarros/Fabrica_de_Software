# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import icon_rc

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(510, 731)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Qframe_login = QFrame(self.centralwidget)
        self.Qframe_login.setObjectName(u"Qframe_login")
        self.Qframe_login.setFrameShape(QFrame.StyledPanel)
        self.Qframe_login.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Qframe_login)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_imagem = QLabel(self.Qframe_login)
        self.lbl_imagem.setObjectName(u"lbl_imagem")
        self.lbl_imagem.setPixmap(QPixmap(u":/icon/bulbasaur.jpg"))
        self.lbl_imagem.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.lbl_imagem)

        self.user = QFrame(self.Qframe_login)
        self.user.setObjectName(u"user")
        self.user.setFrameShape(QFrame.StyledPanel)
        self.user.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.user)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_Usuario = QLabel(self.user)
        self.lbl_Usuario.setObjectName(u"lbl_Usuario")
        font = QFont()
        font.setPointSize(15)
        self.lbl_Usuario.setFont(font)

        self.verticalLayout_2.addWidget(self.lbl_Usuario)

        self.le_usuario = QLineEdit(self.user)
        self.le_usuario.setObjectName(u"le_usuario")
        font1 = QFont()
        font1.setPointSize(12)
        self.le_usuario.setFont(font1)
        self.le_usuario.setClearButtonEnabled(False)

        self.verticalLayout_2.addWidget(self.le_usuario)


        self.verticalLayout_3.addWidget(self.user)

        self.senha = QFrame(self.Qframe_login)
        self.senha.setObjectName(u"senha")
        self.senha.setFrameShape(QFrame.StyledPanel)
        self.senha.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.senha)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_Senha = QLabel(self.senha)
        self.lbl_Senha.setObjectName(u"lbl_Senha")
        self.lbl_Senha.setFont(font)

        self.verticalLayout.addWidget(self.lbl_Senha)

        self.le_senha = QLineEdit(self.senha)
        self.le_senha.setObjectName(u"le_senha")
        self.le_senha.setFont(font1)
        self.le_senha.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.le_senha)


        self.verticalLayout_3.addWidget(self.senha)

        self.label = QLabel(self.Qframe_login)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icon/Snivy.jpg"))
        self.label.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_4.addWidget(self.Qframe_login)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_imagem.setText("")
        self.lbl_Usuario.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.le_usuario.setText("")
        self.le_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu username:", None))
        self.lbl_Senha.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.le_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite sua senha:", None))
        self.label.setText("")
    # retranslateUi

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    w =QMainWindow()
    ui = Ui_MainWindow( )
    ui.setupUi(w)
    w.show()

    app.exec()
