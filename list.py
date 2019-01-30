import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class Rand(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu = ['Krok.ui', 'gosp.ui', 'guak.ui']
        uic.loadUi('listik.ui', self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Rand()
    ex.show()
    sys.exit(app.exec_())
