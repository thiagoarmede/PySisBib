from main import db


class Bibliotecario:

    def __init__(self, usuario: str, senha: str, nome: str, idade: str, cpf: str):
        self.usuario = usuario
        self.senha = senha
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def insere_bibliotecario(self):
        # dicionário que armazenará os dados da classe e os inserirá no banco.
        bib_inserir = {
            "nome": self.nome,
            "idade": self.idade,
            "cpf": self.cpf,
            "usuario": self.usuario,
            "senha": self.senha
        }
        # inserção no banco de dados.
        try:
            bibliotecarios = db.bibliotecarios
            bibliotecarios.insert_one(bib_inserir).inserted_id
        except:
            raise IOError('Impossivel inserir no banco de dados.');
