from views.CadastrarBibliotecarioWindow import CadastrarBibliotecarioWindow
from views.MainWindow import MainWindow


class MainWindowController:

    def open_add_bibliotecario(self):
        self.main_window.close()
        self.cad_bib_win = CadastrarBibliotecarioWindow()
        self.cad_bib_win.show()

    def __init__(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.main_window.botao_add_bibliotecario.clicked.connect(self.open_add_bibliotecario)
        self.cad_bib_win = None
