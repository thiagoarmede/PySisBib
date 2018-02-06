from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from models.Bibliotecario import Bibliotecario
from views.ConfirmWindow import ConfirmWindow


class CadastrarBibliotecarioWindow(QWidget):

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        loadUi('./ui/addbibliotecario.ui', self)
        # janelas extras
        self.confirm_window = None

        # eventos
        self.botao_cadastrar.clicked.connect(self.cadastrar_bibliotecario)
        self.botao_voltar.clicked.connect(self.close)

    def cadastrar_bibliotecario(self):

        dados = {
            "nome": self.linha_nome.text(),
            "idade": self.spin_idade.value(),
            "cpf": self.linha_cpf.text(),
            "usuario": self.linha_usuario.text(),
            "senha": self.linha_senha.text()
        }

        bib_inserir = Bibliotecario(dados["usuario"], dados["senha"], dados["nome"], dados["idade"], dados["cpf"])
        inseriu = bib_inserir.insere_bibliotecario()

        print("Inseriu")
        self.linha_nome.clear()
        self.spin_idade.setValue(18)
        self.linha_cpf.clear()
        self.linha_usuario.clear()
        self.linha_senha.clear()

        print("limpou campos")
        if inseriu:
            self.confirm_window = ConfirmWindow()
            self.confirm_window.show()
        else:
            self.confirm_window = ConfirmWindow()
            self.confirm_window.label.setText("Erro!, Cadastro não efetuado.")
            self.confirm_window.show()






