import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class InputDialogExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.initWidget()
        self.initLayout()
        self.connnect()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()

    def initWidget(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

    def initLayout(self):
        pass

    def connnect(self):
        self.btn.clicked.connect(self.showDialog)

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name')
        if ok:
            self.le.setText(text)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InputDialogExample()
    sys.exit(app.exec_())

