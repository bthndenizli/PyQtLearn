import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class CloseCheckExample(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class CenterExample(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        # print(qr)
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class MainWindowExample(QMainWindow):
    def __init__(self):
        super(MainWindowExample, self).__init__()
        self.initUI()

    def initUI(self):
        exitAct = QAction(QIcon('./img/santacap.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Status Bar')
        self.show()


class SubMenuExample(QMainWindow):
    def __init__(self):
        super(SubMenuExample, self).__init__()
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        newAct = QAction('New', self)
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.show()


class CheckMenuExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')

        viewStatAct = QAction('View statubar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)  # Default selection
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')
        self.show()

    def toggleMenu(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()


class ContextMenuExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Context menu')
        self.show()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        newAct = cmenu.addAction('New')
        opnAct = cmenu.addAction('Open')
        quitAct = cmenu.addAction('Quit')
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()


class ToolBarExample(QMainWindow):
    def __init__(self):
        super(ToolBarExample, self).__init__()
        self.initUI()

    def initUI(self):
        self.toolbar = self.addToolBar('Exit')

        exitAct = QAction('Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        self.toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()


class PutTogether(QMainWindow):
    def __init__(self):
        super(PutTogether, self).__init__()
        self.initUI()

    def initUI(self):
        self.menubar = self.menuBar()
        self.toolbar = self.addToolBar('Exit')
        self.statusbar = self.statusBar()

        # exit Action
        extAct = QAction('Exit', self)
        extAct.setShortcut('Ctrl+Q')
        extAct.setStatusTip('Exit application')
        extAct.triggered.connect(self.close)

        # MenuBar: fileMenu
        fileMeun = self.menubar.addMenu('&File')
        fileMeun.addAction(extAct)

        # ToolBar: exitAct
        self.toolbar.addAction(extAct)


        # Text Edit
        self.textEidt = QTextEdit()
        self.setCentralWidget(self.textEidt)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PutTogether()
    sys.exit(app.exec_())
