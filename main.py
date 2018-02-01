from PyQt5.QtWidgets import QApplication
from views.MainWindow import MainWindow
import sys

root = QApplication(sys.argv)

app = MainWindow()
app.show()

sys.exit(root.exec_())
