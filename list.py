from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QScrollArea

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton

import sys
import os


class ShowMeList(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(250, 250, 250, 150)
        self.setWindowTitle('Список рецептов')
        self.menu = []
        self.initUI()

    def createLayout_group(self):
        self.lst = []
        self.f = open('arhiv.txt', mode='r')
        self.lines = self.f.readlines()
        for i in range(len(self.lines)):
            self.lst.append(self.lines[i].split(';')[0])
        self.f.close()
        sgroupbox = QGroupBox(self)
        layout_groupbox = QVBoxLayout(sgroupbox)
        for i in range(len(self.lst)):
            item = QCheckBox(self.lst[i], sgroupbox)
            item.stateChanged.connect(self.changelist)
            layout_groupbox.addWidget(item)
        layout_groupbox.addStretch(1)
        return sgroupbox

    def createLayout_Container(self):
        self.scrollarea = QScrollArea(self)
        self.scrollarea.setFixedWidth(250)
        self.scrollarea.setWidgetResizable(True)

        widget = QWidget()
        self.scrollarea.setWidget(widget)
        self.layout_SArea = QVBoxLayout(widget)

        self.home = QPushButton('Назад')
        self.home.clicked.connect(self.gohome)

        self.delete = QPushButton('Удалить')
        self.delete.clicked.connect(self.dellrecipe)

        self.layout_SArea.addWidget(self.home)
        self.layout_SArea.addWidget(self.delete)
        self.layout_SArea.addWidget(self.createLayout_group())
        self.layout_SArea.addStretch(1)

    def gohome(self):
        from program import Main
        self.new = Main()
        self.new.show()
        self.close()

    def dellrecipe(self):
        self.f = open('arhiv.txt', mode='r')
        self.lines = self.f.readlines()
        self.f.close()
        self.o = open('arhiv.txt', mode='w')
        for i in self.lines:
            if i.split(';')[0] not in self.menu:
                self.o.write(i.split(';')[0]+';' + i.split(';')[1])
        self.o.close()

    def changelist(self):
        if self.sender().checkState():
            self.menu.append(self.sender().text())
        else:
            if self.sender().text() in self.menu:
                self.menu.remove(self.sender().text())

    def initUI(self):
        self.lable2 = QLabel()
        self.lable2.setText('BBA')
        self.createLayout_Container()
        self.layout_All = QVBoxLayout(self)
        self.layout_All.addWidget(self.scrollarea)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShowMeList()
    ex.show()
    sys.exit(app.exec_())