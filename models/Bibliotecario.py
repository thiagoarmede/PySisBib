from Database import Database


class Bibliotecario:

    def __init__(self, usuario: str, senha: str, nome: str, idade: int, cpf: str):
        self.usuario = usuario
        self.senha = senha
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        # variável que referencia a coleção "bibliotecários" do banco de dados.

    def insere_bibliotecario(self):
        database = Database()
        bibliotecarios = database.db.bibliotecarios
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
            result = bibliotecarios.insert_one(bib_inserir).inserted_id
            print(result)
            return True if result else False
        except ConnectionError:
            print('Servidor indisponível.');

    @staticmethod
    def autenticar(usuario, senha):
        database = Database()
        # utilizando coleção bibliotecarios.
        bibliotecarios = database.db.bibliotecarios

        try:
            bib = bibliotecarios.find_one({
                "usuario": usuario,
                "senha": senha
            })
        except ConnectionError:
            print("Servidor indisponível.")

        # fechando conexão.
        database.client.close()
        return True if bib else None


