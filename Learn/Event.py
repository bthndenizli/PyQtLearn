# encoding: utf-8

# Debug
import cgitb

cgitb.enable()
#

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPen
from PyQt5.QtCore import QCoreApplication
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


class Example_1(QWidget):
    def __init__(self):
        super(Example_1, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Learn some program')

        lcd = QLCDNumber(self)
        dial = QDial(self)
        slider = QSlider(Qt.Horizontal, self)

        lcd.setGeometry(100, 50, 150, 60)
        dial.setGeometry(120, 120, 100, 100)
        slider.setGeometry(120, 220, 100, 20)

        dial.valueChanged.connect(lcd.display)
        slider.valueChanged.connect(lcd.display)
        self.show()


class Example_2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Learn some program')

        self.lab = QLabel('direction', self)
        self.lab.setGeometry(150, 100, 50, 50)

        self.show()

    def keyPressEvent(self, keyevent):
        if keyevent == Qt.Key_Up:
            self.lab.setText('Up')
        elif keyevent == Qt.Key_Down:
            self.lab.setText('Down')
        elif keyevent == Qt.Key_Left:
            self.lab.setText('Left')
        elif keyevent == Qt.Key_Right:
            self.lab.setText('Right')
        elif keyevent == Qt.Key_Return:
            self.lab.setText('R')
        else:
            self.lab.setText('Right')


# 跟踪鼠标
class Example_3(QWidget):
    distance_from_center = 0

    def __init__(self):
        super(Example_3, self).__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(200, 200, 1000, 500)
        self.setWindowTitle('Learn')
        self.label = QLabel(self)
        self.label.resize(500, 40)
        self.show()
        self.pos = None

    def mouseMoveEvent(self, QMouseEvent):
        d = (QMouseEvent.y() - 250) ** 2 + (QMouseEvent.x() - 500) ** 2
        distance_from_center = round(d ** 0.5)
        s = f"坐标: (x: {QMouseEvent.x()}, y: {QMouseEvent.y()})" + " 离中心点距离: " + str(distance_from_center)
        self.label.setText(s)
        self.pos = QMouseEvent.pos()
        self.update()

    def paintEvent(self, QPaintEvent):
        if self.pos:
            q = QPainter(self)
            q.drawLine(0, 0, self.pos.x(), self.pos.y())


def test_1():
    app = QApplication(sys.argv)
    ex = Example_1()
    sys.exit(app.exec_())


def test_2():
    app = QApplication(sys.argv)
    ex = Example_2()
    sys.exit(app.exec_())


def test_3():
    app = QApplication(sys.argv)
    ex = Example_3()
    sys.exit(app.exec_())


if __name__ == '__main__':
    test_2()
