import sys
import math
from Show import Rand
from list import List
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Main.ui', self)
        self.randomBtn.clicked.connect(self.randclic)
        self.list.btn.clicked.connect(self.showlist)

    def randclic(self):
        self.new = Rand()
        self.new.show()
        self.close()

    def showlist(self):
        self.new =

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
