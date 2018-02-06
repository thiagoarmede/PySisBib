from PyQt5.QtWidgets import QApplication
from views.MainWindow import MainWindow
import sys

# inicio de instancia da janela inicial da aplicação
root = QApplication(sys.argv)

app = MainWindow()
app.show()

sys.exit(root.exec_())
