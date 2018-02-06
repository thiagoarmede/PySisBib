# import dos modulos do Qt
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.uic import loadUi
# import das views
from views.KeyWindow import KeyWindow
from views.InitWindow import InitWindow
from views.LoginErrorWindow import LoginErrorWindow
# import dos models
from models.Bibliotecario import Bibliotecario

import time
import sys


class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        loadUi('./ui/mainwindow.ui', self)

        # Outras janelas a serem abertas.
        self.key_win = None
        self.init_win = None
        self.janela_erro = None

        # signals e slots relacionados à janela inicial.
        # cadastro de bibliotecário.
        self.botao_add_bib.clicked.connect(self.abre_autenticacao)

        # login
        self.botao_login.clicked.connect(self.login)
        self.linha_senha.returnPressed.connect(self.login)

    def abre_autenticacao(self):
        """Antes de cadastrar o bibliotecário, é necessário
        informar a chave de segurança"""
        self.key_win = KeyWindow()
        self.key_win.show()

    def login(self):
        texto_usuario = self.linha_usuario.text()
        texto_senha = self.linha_senha.text()

        if Bibliotecario.autenticar(texto_usuario, texto_senha):
            time.sleep(1)
            self.init_win = InitWindow()
            self.init_win.show()
            self.close()
        else:
            self.linha_usuario.clear()
            self.linha_senha.clear()
            self.janela_erro = LoginErrorWindow()
            self.janela_erro.show()





