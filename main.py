from PyQt5.QtWidgets import QApplication
from controllers.MainWindowController import MainWindowController
import sys
import pymongo

# inicio de instancia da janela inicial da aplicação
root = QApplication(sys.argv)

app = MainWindowController()

# inicio da instancia do banco de dados
try:
    client = pymongo.MongoClient('localhost', 27017)
    db = client['maindb']
except IOError:
    print('Erro ao acessar banco de dados.')



sys.exit(root.exec_())
