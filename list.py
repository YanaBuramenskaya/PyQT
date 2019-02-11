from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QScrollArea

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton

import sys


class ShowMeList(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(250, 250, 250, 150)
        self.setWindowTitle('Список рецептов')
        self.initUI()

    def createLayout_group(self):
        from program import lst
        sgroupbox = QGroupBox(self)
        layout_groupbox = QVBoxLayout(sgroupbox)
        for i in range(len(lst)):
            item = QCheckBox(lst[i], sgroupbox)
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


        self.layout_SArea.addWidget(self.home)
        self.layout_SArea.addWidget(self.createLayout_group())
        self.layout_SArea.addStretch(1)

    def gohome(self):
        from program import Main
        self.new = Main()
        self.new.show()
        self.close()


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