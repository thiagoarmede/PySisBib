from models.NumChamada import NumChamada
from datetime import date


class Livro:
    """Modelo que pré define um livro no sistema."""
    def __init__(self, data_cad: date, num_chamada: NumChamada, isbn: str, nome: str, autores: list, edicao: int, ano: int, editora: str, forma_aquis: str, prateleira: int):
        self.__data_cad = data_cad
        self.__num_chamada = num_chamada
        self.__isbn = isbn
        self.__nome = nome
        self.__autores = autores
        self.__edicao = edicao
        self.__ano = ano
        self.__editora = editora
        self.__forma_aquis = forma_aquis
        self.__prateleira = prateleira
        # variaveis inicializadas vazias
        self.__data_baixa = None
        self.__motivo_baixa = None




