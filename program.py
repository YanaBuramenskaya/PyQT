import sys
import math
from Show import Rand
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

lst = ['Крок Мадам', 'Гаспачо', 'Гуакамоле']
new_res = []

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Main.ui', self)
        self.randomBtn.clicked.connect(self.randclic)
        self.listBtn.clicked.connect(self.showlist)
        self.addBtn.clicked.connect(self.addnew)

    def randclic(self):
        self.new = Rand()
        self.new.show()
        self.close()

    def showlist(self):
        from list import ShowMeList
        self.new = ShowMeList()
        self.new.show()
        self.close()

    def addnew(self):
        from add import AddMeNew
        self.new = AddMeNew()
        self.new.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
