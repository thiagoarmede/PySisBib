from datetime import date


class Periodico:

    def __init__(self, id:str, issn:str, nome:str, editora:str, data_cad:date, forma_aquis:str, secao:str, estante:str, prateleira:str, copias:int):
        self.__id = id
        self.__issn = issn
        self.__nome = nome
        self.__editora = editora
        self.__data_cad = data_cad
        self.__forma_aquis = forma_aquis
        self.__secao = secao
        self.__estante = estante
        self.__prateleira = prateleira
        self.__copias = copias
        #variaveis inicializadas vazias
        self.__data_baixa = None
        self.__motivo_baixa = None

