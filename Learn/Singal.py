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


# 信号
class Singal(QObject):
    showmouse = pyqtSignal()


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('Learn')
        # 信号与槽
        self.s = Singal()
        self.s.showmouse.connect(self.about)

        self.show()

    def about(self):
        QMessageBox.about(self, 'About', 'You click Mouse')

    def mousePressEvent(self, QMouseEvent):
        # 按下鼠标发送信号
        self.s.showmouse.emit()


def test():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    test()
