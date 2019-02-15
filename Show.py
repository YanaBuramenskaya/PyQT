import sys
import math
from PyQt5 import uic
import random
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class Rand(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu = ['Krok.ui', 'gosp.ui', 'guak.ui']
        self.f = open('arhiv.txt', mode='r')
        self.lines = self.f.readlines()
        for i in range(len(self.lines)):
            self.lines[i] = self.lines[i].split(';')
        self.it = random.randint(0, len(self.lines)-1)
        print(self.lines[self.it][1].rstrip() == 'Krok.ui')
        if self.lines[self.it][1].rstrip() in self.menu:
            self.ind = self.menu.index(self.lines[self.it][1].rstrip())
            print('a')
            uic.loadUi(self.menu[self.ind], self)
            self.back.clicked.connect(self.clic)
        else:
            uic.loadUi('vashe.ui', self)
            self.Name.setText(self.lines[self.it][0])
            self.Label.setText(self.lines[self.it][1])
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
