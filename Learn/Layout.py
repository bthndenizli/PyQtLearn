# encoding: utf-8

# Debug
import cgitb

cgitb.enable()
#

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QScroller
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLCDNumber
from PyQt5.QtWidgets import QDial
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QtDebugMsg
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFormLayout


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Learn')

        blt1 = QPushButton('scissor', self)
        blt2 = QPushButton('stone', self)
        blt3 = QPushButton('cloth', self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)  # 增加伸缩量
        hbox.addWidget(blt1)
        hbox.addStretch(1)  # 增加伸缩量
        hbox.addWidget(blt2)
        hbox.addStretch(1)  # 增加伸缩量
        hbox.addWidget(blt3)
        hbox.addStretch(1)  # 增加伸缩量

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.show()


def test():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


class Example1(QWidget):
    def __init__(self):
        super(Example1, self).__init__()
        self.initUI()

    def initUI(self):
        # 创建QGridLayout的实例并将其设置为应用程序窗口的布局
        grid = QGridLayout()
        self.setLayout(grid)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Learn')

        self.lcd = QLCDNumber()
        # QGridLayout.addwidget 的参数:
        # 控件名，行，列，占用行数，占用列数，对齐方式
        # 例如, 下面就是添加 LCD数字, 在0行, 0列, 行长度为4, 列长度为1
        grid.addWidget(self.lcd, 0, 0, 3, 0)
        # 窗口小部件之间设置间距
        grid.setSpacing(10)

        names = ['Cls', 'Bc', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(4, 9) for j in range (4, 8)]
        for (pos, name) in zip(positions, names):
            if (name == ''):
                continue
            button = QPushButton(name)
            # 按网格空位的顺序添加进网格布局
            grid.addWidget(button, *pos)
            button.clicked.connect(self.Cli)

        self.show()

    def Cli(self):
        sender = self.sender().text()
        ls = ['/', '*', '-', '=', '+']
        if sender in ls:
            self.lcd.display('A')
        else:
            self.lcd.display(sender)



def test1():
    app = QApplication(sys.argv)
    ex = Example1()
    sys.exit(app.exec_())


class Example2(QWidget):
    def __init__(self):
        super(Example2, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Learn')

        formlayout = QFormLayout()
        self.setLayout(formlayout)

        nameLable = QLabel('Name')
        nameLineEdit = QLineEdit("")
        introductionLabel = QLabel("Introduction")
        introductionLineEdit = QLineEdit("")

        formlayout.addRow(nameLable, nameLineEdit)
        formlayout.addRow(introductionLabel, introductionLineEdit)
        formlayout.setFieldGrowthPolicy(2)

        self.show()



def test2():
    app = QApplication(sys.argv)
    ex = Example2()
    sys.exit(app.exec_())


if __name__ == '__main__':
    test2()
