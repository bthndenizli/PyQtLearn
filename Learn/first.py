# encoding: utf-8

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

from Learn import PushButton_UI, firstUI


def test_1():
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())


def test_2():
    app = QApplication(sys.argv)

    MainWindow = QMainWindow()
    ui = firstUI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())


def test_3():
    app = QApplication(sys.argv)

    try:
        if len(sys.argv) < 2:
            raise ValueError
        else:
            title = " ".join(sys.argv[1:])

    except ValueError:
        title = "DefalitTitle"

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle(title)
    w.show()

    sys.exit(app.exec_())


def test_4():
    app = QApplication(sys.argv)

    try:
        if len(sys.argv) < 2:
            raise ValueError
        else:
            title = " ".join(sys.argv[1:])

    except ValueError:
        title = "DefalitTitle"

    MainWindow = QMainWindow()
    ui = firstUI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle(title)
    MainWindow.show()

    sys.exit(app.exec_())


class Ico(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Title')
        self.setWindowIcon(QIcon('xdbcb8.ico'))

        qbtn = QPushButton('quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(70, 30)
        qbtn.move(50, 50)

        self.show()


def test_5():
    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())


def test_6():
    app = QApplication(sys.argv)

    mw = QMainWindow()

    ui = PushButton_UI.Ui_MainWindow()
    ui.setupUi(mw)
    mw.show()

    sys.exit(app.exec_())



if __name__ == '__main__':
    test_6()
