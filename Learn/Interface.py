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
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import qApp
from PyQt5.QtWidgets import QMenu
from PyQt5.QtCore import QtDebugMsg


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.InitUI()

    def InitUI(self):
        """
        关联变量: self.membar
        """
        # 主窗口属性
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Learn')

        # 状态栏
        self.statusBar().showMessage("Ready? Go")

        # 菜单栏
        self.menubar = self.menuBar()

        # 文件菜单
        self.FileMenuInit()

        # 工具栏
        self.ToolBarInit()

        self.show()

    def FileMenuInit(self):
        self.exitAct = QAction(QIcon('./src/img/exit.png'), 'Quit(&E)', self)
        self.exitAct.setShortcut('Ctrl+Q')
        self.exitAct.setStatusTip('Quit Program')
        self.exitAct.triggered.connect(qApp.quit)

        # 保存动作
        self.saveAct = QAction(QIcon('./src/img/save.png'), 'Save...', self)
        self.saveAct.setShortcut('Ctrl+S')
        self.saveAct.setStatusTip('Save File')

        # 另存为动作
        self.saveasAct = QAction(QIcon('./src/img/saveas.png'), 'Save as...(&O)', self)
        self.saveasAct.setStatusTip('File Save As')

        # 新建文件动作
        self.newAct = QAction(QIcon('./src/img/new.png'), 'New(&N)', self)
        self.newAct.setShortcut('Ctrl+N')
        self.newAct.setToolTip('Create New File')

        # 保存子菜单
        saveMenu = QMenu('Save Mode(&S)', self)
        saveMenu.addAction(self.saveAct)
        saveMenu.addAction(self.saveasAct)

        # 文件菜单
        fileMenu = self.menubar.addMenu('File(&F)')
        fileMenu.addAction(self.newAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAct)

    def ToolBarInit(self):
        self.toolbar = self.addToolBar('ToolBar')
        self.toolbar.addAction(self.newAct)
        self.toolbar.addAction(self.exitAct)

    def contextMenuEvent(self, QContextMenuEvent):
        '''
        使用上下文菜单，我们必须重新实现contextMenuEvent()方法
        :param QContextMenuEvent:
        :return:
        '''

        cmenu = QMenu(self)
        newAct = cmenu.addAction("New File")
        opnAct = cmenu.addAction("Save File")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(QContextMenuEvent.pos()))
        if action == quitAct:
            qApp.quit()


def test_1():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    test_1()
