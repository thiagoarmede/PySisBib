from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from Database import Database
from views.CadastrarBibliotecarioWindow import CadastrarBibliotecarioWindow
import time


class KeyWindow(QWidget):

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        loadUi('./ui/keywindow.ui', self)
        # janelas
        self.cad_bib_win = None

        # associando eventos
        self.botao_ok.clicked.connect(self.autenticar)
        self.botao_cancelar.clicked.connect(self.close)

    def autenticar(self):
        database = Database()
        key = self.linha_key.text()
        authkey = database.db.authkey
        print('Iniciou conexão com o banco de dados.')

        try:
            key_db = authkey.find_one({
                "key": key
            })
        except ConnectionError:
            print("Servidor indisponível.")

        if key:
            time.sleep(0.5)
            self.cad_bib_win = CadastrarBibliotecarioWindow()
            self.cad_bib_win.show()
            self.close()
        else:
            self.close()

        database.client.close()