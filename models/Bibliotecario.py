from Database import Database


class Bibliotecario:

    def __init__(self, usuario: str, senha: str, nome: str, idade: str, cpf: str):
        self.usuario = usuario
        self.senha = senha
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        # variável que referencia a coleção "bibliotecários" do banco de dados.

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
            self.bibliotecarios.insert_one(bib_inserir).inserted_id
        except IOError:
            print('Impossivel inserir no banco de dados.');

    @staticmethod
    def autenticar(usuario, senha):
        bibliotecarios = Database().db.bibliotecarios
        bib = bibliotecarios.find_one({
            "usuario": usuario,
            "senha": senha
        })

        return True if bib else None


