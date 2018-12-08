# encoding: utf-8

# Debug
import cgitb

cgitb.enable()
#

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QScroller
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QLineEdit

from random import randint


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.num = randint(1, 100)

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Guess Number')

        self.blt1 = QPushButton('I Guess', self)
        self.blt1.setGeometry(115, 150, 70, 30)
        self.blt1.setToolTip('<b>click here to guess number</b>')
        self.blt1.clicked.connect(self.showMessage)

        self.text = QLineEdit('Enter number here', self)
        self.text.selectAll()
        self.text.setFocus()
        self.text.setGeometry(80, 50, 150, 30)

        self.show()

    def showMessage(self):

        guessNumber = int(self.text.text())
        print(self.num)

        if guessNumber > self.num:
            QMessageBox.about(self, 'Result', 'Too large')
            self.text.setFocus()
        elif guessNumber < self.num:
            QMessageBox.about(self, 'Result', 'Too samll')
            self.text.setFocus()
        else:
            QMessageBox.about(self, 'See Result', r"You're right! Next challenge.")
            self.num = randint(1, 100)
            self.text.clear()
            self.text.setFocus()

    '''
    如果关闭此对象的实例化部件，则生成QCloseEvent
    '''

    def closeEvent(self, QCloseEvent):

        reply = QMessageBox.question(self, 'Confirm', 'To quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
