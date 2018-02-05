import pymongo


class Database:

    def __init__(self):
        try:
            self.db = pymongo.MongoClient('localhost', 27017)['maindb']
        except IOError:
            print('Erro ao acessar banco de dados.')

