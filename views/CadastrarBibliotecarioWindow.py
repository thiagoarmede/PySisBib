from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


class CadastrarBibliotecarioWindow(QWidget):

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        loadUi('./ui/addbibliotecario.ui', self)


