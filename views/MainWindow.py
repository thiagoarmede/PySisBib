from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        loadUi('./ui/mainwindow.ui', self)
