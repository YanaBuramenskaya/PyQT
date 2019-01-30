import sys
import math
from PyQt5 import uic
import random
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class Rand(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu = ['Krok.ui', 'gosp.ui', 'guak.ui']
        uic.loadUi(random.choice(self.menu), self)
        self.back.clicked.connect(self.clic)

    def clic(self):
        from program import Main
        self.new = Main()
        self.new.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Rand()
    ex.show()
    sys.exit(app.exec_())
