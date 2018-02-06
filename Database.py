import pymongo


class Database:

    indices_definidos = False

    def __init__(self):
        try:
            self.client = pymongo.MongoClient('localhost', 27017)
            self.db = self.client['maindb']

            # definição dos indices da coleção bibliotecarios.
            self.define_indices_bibliotecarios()
        except IOError:
            print('Erro ao acessar banco de dados.')


    def define_indices_bibliotecarios(self):

        if not self.indices_definidos:
            try:
                self.db.bibliotecarios.create_index([("usuario", pymongo.ASCENDING)], unique=True)
                self.db.bibliotecarios.create_index([("senha", pymongo.HASHED)])
                self.db.bibliotecarios.create_index([("cpf", pymongo.ASCENDING)], unique=True)
            except ConnectionError:
                print("Impossivel criar indices, banco indisponivel.")
        else:
            print("indices já definidos.")