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
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QScroller
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLCDNumber
from PyQt5.QtWidgets import QDial
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import qApp
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QTextBrowser
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QFontDialog
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtPrintSupport import QPageSetupDialog
from PyQt5.QtPrintSupport import QPrintDialog
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtCore import QtDebugMsg


class Example1(QWidget):

    def __init__(self):
        super(Example1, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 550)
        self.setWindowTitle('Learn')

        self.InputDialog()

        self.show()

    def InputDialog(self):
        self.lb1 = QLabel('Name: ', self)
        self.lb1.move(20, 20)

        self.lb2 = QLabel('年龄：', self)
        self.lb2.move(20, 80)

        self.lb3 = QLabel('性别：', self)
        self.lb3.move(20, 140)

        self.lb4 = QLabel('身高（cm）：', self)
        self.lb4.move(20, 200)

        self.lb5 = QLabel('基本信息：', self)
        self.lb5.move(20, 260)

        self.lb6 = QLabel('学点编程', self)
        self.lb6.move(80, 20)

        self.lb7 = QLabel('18', self)
        self.lb7.move(80, 80)

        self.lb8 = QLabel('男', self)
        self.lb8.move(80, 140)

        self.lb9 = QLabel('175', self)
        self.lb9.move(120, 200)

        self.tb = QTextBrowser(self)
        self.tb.move(20, 320)

        self.bt1 = QPushButton('修改姓名', self)
        self.bt1.move(200, 20)

        self.bt2 = QPushButton('修改年龄', self)
        self.bt2.move(200, 80)

        self.bt3 = QPushButton('修改性别', self)
        self.bt3.move(200, 140)

        self.bt4 = QPushButton('修改身高', self)
        self.bt4.move(200, 200)

        self.bt5 = QPushButton('修改信息', self)
        self.bt5.move(200, 260)

        self.bt1.clicked.connect(self.showDialog)
        self.bt2.clicked.connect(self.showDialog)
        self.bt3.clicked.connect(self.showDialog)
        self.bt4.clicked.connect(self.showDialog)
        self.bt5.clicked.connect(self.showDialog)

    def showDialog(self):
        sender = self.sender()
        sex = ['Male', 'Female']

        if sender == self.bt1:
            text, ok = QInputDialog.getText(self, 'modify name', 'Please input name')
            if ok:
                self.lb6.setText(text)
        elif sender == self.bt2:
            text, ok = QInputDialog.getInt(self, 'modify age', 'Please input age', min=1)
            if ok:
                self.lb7.setText(str(text))
        elif sender == self.bt3:
            text, ok = QInputDialog.getItem(self, 'modify sex', 'Please input sex', sex)
            if ok:
                self.lb8.setText(text)
        elif sender == self.bt4:
            text, ok = QInputDialog.getInt(self, 'modify height', 'Please input height', min=1)
            if ok:
                self.lb9.setText(str(text))
        elif sender == self.bt5:
            text, ok = QInputDialog.getText(self, 'modify message', 'Please input message')
            if ok:
                self.tb.setText(text)


class Example2(QWidget):

    def __init__(self):
        super(Example2, self).__init__()
        self.printer = QPrinter()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧--记得好看点')

        self.tx = QTextEdit(self)
        self.tx.setGeometry(20, 20, 300, 270)

        self.blt1 = QPushButton('Open File', self)
        self.blt1.move(350, 20)
        self.blt2 = QPushButton('Select Font', self)
        self.blt2.move(350, 70)
        self.blt3 = QPushButton('Select Color', self)
        self.blt3.move(350, 120)

        self.blt4 = QPushButton('Open multiple file', self)
        self.blt4.move(350, 170)
        self.blt5 = QPushButton('Page Setting', self)
        self.blt5.move(350, 220)
        self.blt6 = QPushButton('Print Document', self)
        self.blt6.move(350, 270)

        self.blt7 = QPushButton('Save File', self)
        self.blt7.move(350, 320)

        self.blt1.clicked.connect(self.openfile)
        self.blt2.clicked.connect(self.choicefont)
        self.blt3.clicked.connect(self.choicecolor)

        self.blt4.clicked.connect(self.openfiles)
        self.blt5.clicked.connect(self.pagesettings)
        self.blt6.clicked.connect(self.printdocument)
        self.blt7.clicked.connect(self.savefile)

        self.show()

    def savefile(self):
        fileName = QFileDialog.getSaveFileName(self, 'Save File', './', "Text files (*.txt)")
        if fileName[0]:
            with open(fileName[0], 'w', encoding='utf=8', errors='ignore') as f:
                f.write(self.tx.toPlainText())

    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', './')
        if fname[0]:
            with open(fname[0], 'r', encoding='gb18030', errors='ignore') as f:
                self.tx.setText(f.read())

    def choicefont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.tx.setCurrentFont(font)

    def choicecolor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.tx.setTextColor(color)

    def openfiles(self):
        fnames = QFileDialog.getOpenFileNames(self, 'Open Multiple File', './')
        if fnames[0]:
            for fname in fnames[0]:
                with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
                    self.tx.append(f.read())

    def pagesettings(self):
        printsetdialog = QPageSetupDialog(self.printer, self)
        printsetdialog.exec_()

    def printdocument(self):
        printdialog = QPrintDialog(self.printer, self)
        if QDialog.Accepted == printdialog.exec_():
            self.tx.print(self.printer)


class Example3(QWidget):
    def __init__(self):
        super(Example3, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 330, 300)
        self.setWindowTitle('Learn')

        self.la = QLabel('Here Display the Message we select', self)
        self.la.move(20, 20)

        self.bt1 = QPushButton('Tip', self)
        self.bt1.move(20, 70)
        self.bt2 = QPushButton('询问', self)
        self.bt2.move(120, 70)
        self.bt3 = QPushButton('警告', self)
        self.bt3.move(220, 70)
        self.bt4 = QPushButton('错误', self)
        self.bt4.move(20, 140)
        self.bt5 = QPushButton('关于', self)
        self.bt5.move(120, 140)
        self.bt6 = QPushButton('关于Qt', self)
        self.bt6.move(220, 140)

        self.bt1.clicked.connect(self.info)
        self.bt2.clicked.connect(self.question)
        self.bt3.clicked.connect(self.warning)
        self.bt4.clicked.connect(self.critical)
        self.bt5.clicked.connect(self.about)
        self.bt6.clicked.connect(self.aboutqt)

        self.show()

    def info(self):
        reply = QMessageBox.information(self, 'Tip', 'Tip MessageBox !', QMessageBox.Ok | QMessageBox.Close,
                                        QMessageBox.Close)
        if reply == QMessageBox.Ok:
            self.la.setText('你选择了Ok！')
        else:
            self.la.setText('你选择了Close！')

    def question(self):
        option = (QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        reply = QMessageBox.question(self, 'Question', 'Question MessageBox', *option)
        if reply == QMessageBox.Yes:
            self.la.setText('你选择了Ok！')
        elif reply == QMessageBox.No:
            self.la.setText('你选择了No！')
        else:
            self.la.setText('你选择了Cancel！')

    def warning(self):
        cb = QCheckBox('All Document operate like this')
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Warn')
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText('Warning MeaassgeBox')
        msgBox.setInformativeText('出现更改愿意保存吗?')

        Save = msgBox.addButton('Save', QMessageBox.AcceptRole)
        NoSave = msgBox.addButton('NoSave', QMessageBox.RejectRole)
        Cancel = msgBox.addButton('Cancel', QMessageBox.DestructiveRole)

        msgBox.setDefaultButton(Save)
        msgBox.setCheckBox(cb)

        cb.stateChanged.connect(self.check)
        reply = msgBox.exec() # 重要

        if reply == QMessageBox.AcceptRole:
            self.la.setText('你选择了保存！')
        elif reply == QMessageBox.RejectRole:
            self.la.setText('你选择了取消！')
        else:
            self.la.setText('你选择了不保存！')

    def check(self):
        if self.sender().isChecked():
            self.la.setText('你打勾了哦')
        else:
            self.la.setText('怎么又不打了啊')

    def critical(self):
        # reply = QMessageBox.critical(self,'错误','这是一个错误消息对话框', QMessageBox.Retry | QMessageBox.Abort | QMessageBox.Ignore , QMessageBox.Retry)
        msgBox = QMessageBox()
        msgBox.setWindowTitle('错误')
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("这是一个错误消息对话框")
        msgBox.setStandardButtons(QMessageBox.Retry | QMessageBox.Abort | QMessageBox.Ignore)
        msgBox.setDefaultButton(QMessageBox.Retry)
        msgBox.setDetailedText('这是详细的信息：学点编程吧，我爱你！')
        reply = msgBox.exec()

        if reply == QMessageBox.Retry:
            self.la.setText('你选择了Retry！')
        elif reply == QMessageBox.Abort:
            self.la.setText('你选择了Abort！')
        else:
            self.la.setText('你选择了Ignore！')

    def about(self):
        # QMessageBox.about(self,'关于','这是一个关于消息对话框!')
        msgBox = QMessageBox(QMessageBox.NoIcon, '关于', '不要意淫了，早点洗洗睡吧!')
        msgBox.setIconPixmap(QPixmap("./src/img/save.png"))
        msgBox.exec()

    def aboutqt(self):
        QMessageBox.aboutQt(self, '关于Qt')


def test_1():
    app = QApplication(sys.argv)
    ex = Example1()
    sys.exit(app.exec_())


def test_2():
    app = QApplication(sys.argv)
    ex = Example2()
    sys.exit(app.exec_())


def test_3():
    app = QApplication(sys.argv)
    ex = Example3()
    sys.exit(app.exec_())


if __name__ == '__main__':
    test_3()
