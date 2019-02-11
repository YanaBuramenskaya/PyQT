import sys
import math
from PyQt5 import uic
import random
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class AddMeNew(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('add.ui', self)
        self.back.clicked.connect(self.home)
        
    def home(self):
        from program import Main
        self.new = Main()
        self.new.show()
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddMeNew()
    ex.show()
    sys.exit(app.exec_())
