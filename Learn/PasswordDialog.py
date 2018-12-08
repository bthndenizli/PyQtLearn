# encoding: utf-8

# Debug
import cgitb

cgitb.enable()
#

# import sys

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QEvent
from PyQt5.QtCore import QRegExp
from PyQt5.QtCore import QObject

from PyQt5.QtGui import QKeyEvent
from PyQt5.QtGui import QKeySequence
from PyQt5.QtGui import QRegExpValidator


class PasswordDialog(QDialog):
    def __init__(self):
        super(PasswordDialog, self).__init__()
        self.initUI()

    def initLayout(self):
        # Layout
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.bt1)
        self.hbox.addWidget(self.bt2)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.lb)
        self.vbox.addWidget(self.edit)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)

    def initUI(self):
        self.resize(350, 100)
        self.setWindowTitle('Password Input Dialog')

        # Widget
        self.lb = QLabel('Please enter the password', self)

        self.edit = QLineEdit(self)

        self.bt1 = QPushButton('Ok', self)
        self.bt2 = QPushButton('Cancel', self)

        self.initLayout()

        # EditLine
        self.edit.installEventFilter(self)
        self.edit.setContextMenuPolicy(Qt.NoContextMenu)
        self.edit.setPlaceholderText("密码6-15位，只能有数字和字母，必须以字母开头")
        self.edit.setEchoMode(QLineEdit.Password)
        regx = QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$")
        validator = QRegExpValidator(regx, self.edit)
        self.edit.setValidator(validator)

        # Connect
        self.bt1.clicked.connect(self.Ok)
        self.bt1.clicked.connect(self.Cancel)


    def Ok(self):
        self.text = self.edit.text()
        print(self.text)
        if len(self.text) == 0:
            QMessageBox.warning(self, "Warning", "Password is Empty!")
        elif len(self.text) < 6:
            QMessageBox.warning(self, "Waring", "Length of Password less than 6")
        elif len(self.text) > 15:
            QMessageBox.warning(self, "Waring", "Length of Password more than 15")
        else:
            self.done(self, 1)

    def Cancel(self):
        self.done(self, 0)


    def eventFilter(self, object, event):
        if object ==  self.edit:
            # 跳过这些鼠标移动事件和鼠标双击事件
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return  True
            # 跳过键盘快捷键全选,复制,粘贴
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(QKeySequence.Paste):
                    return True
            return QDialog.eventFilter(self, object, event)

    def getPassword(self):
        return self.text