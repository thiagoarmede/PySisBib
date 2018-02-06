from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


class ConfirmWindow(QWidget):

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        loadUi('./ui/confirmwindow.ui', self)
        self.botao_ok.clicked.connect(self.fechar)

    def fechar(self):
        self.close()