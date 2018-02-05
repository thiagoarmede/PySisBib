from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from Database import Database
from views.CadastrarBibliotecarioWindow import CadastrarBibliotecarioWindow

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
        key = self.linha_key.text()
        authkey = Database().db.authkey
        key_db = authkey.find_one({
            "key": key
        })

        if key:
            self.cad_bib_win.show()
            self.close()
        else:
            self.close()
