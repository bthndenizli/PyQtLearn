import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Example1(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()


class KeyEventExample2(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


class SenderExample(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


class MouseEventExample(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        x = 0
        y = 0

        self.text = "x: {0},  y: {1}".format(x, y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)


class Communicate(QObject):
    closeApp = pyqtSignal()
    printMsg = pyqtSignal()
    Signal_OneParameter = pyqtSignal(int)


class EmitExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.count = 0

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        self.c.printMsg.connect(lambda: print('msg'))
        self.c.Signal_OneParameter.connect(lambda count: print(count))

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def keyPressEvent(self, *args, **kwargs):
        self.c.printMsg.emit()
        self.count = self.count + 1
        self.c.Signal_OneParameter.emit(self.count)

    def mousePressEvent(self, e):
        self.c.closeApp.emit()


class EmitParamerExample(QWidget):
    def __init__(self):
        super(EmitParamerExample, self).__init__()
        self.initUI()

    # 重载, 传入参数可以是 int, int 两个整型, 也可以是 int, str 类型
    OnClicked = pyqtSignal([int, int], [int, str])

    def initUI(self):

        self.OnClicked[int, int].connect(self.OnValueChanged_int)
        self.OnClicked[int, str].connect(self.OnValueChanged_string)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.OnClicked[int, int].emit(event.x(), event.y())
            event.accept()
        elif event.button() == Qt.RightButton:
            self.OnClicked[int, str].emit(event.x(), str(event.y()))
            event.accept()
        else:
            super().mousePressEvent(self, event)

    def OnValueChanged_int(self, x, y):
        print(f'Left button ({x}, {y})')

    def OnValueChanged_string(self, x, szy):
        print(f'Right button ({x}, ' + szy + ')')


class PrinterSettingExample(QWidget):
    helpSignal = pyqtSignal(str)
    printSignal = pyqtSignal(list)
    # 声明一个多重载版本的信号，包括了一个带int和str类型参数的信号，以及带str参数的信号
    previewSignal = pyqtSignal([int, str], [str])

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.creatContorls("打印控制：")
        self.creatResult("操作结果：")

        layout = QHBoxLayout()
        layout.addWidget(self.controlsGroup)
        layout.addWidget(self.resultGroup)
        self.setLayout(layout)

        self.helpSignal.connect(self.showHelpMessage)  # str
        self.printSignal.connect(self.printPaper)  # list
        self.previewSignal[str].connect(self.previewPaper)  # str
        self.previewSignal[int, str].connect(self.previewPaperWithArgs)  # int ,str
        self.printButton.clicked.connect(self.emitPrintSignal)
        self.previewButton.clicked.connect(self.emitPreviewSignal)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('defined signal')
        self.show()

    def creatContorls(self, title):
        self.controlsGroup = QGroupBox(title)
        self.printButton = QPushButton("打印")
        self.previewButton = QPushButton("预览")
        numberLabel = QLabel("打印份数：")
        pageLabel = QLabel("纸张类型：")
        self.previewStatus = QCheckBox("全屏预览")
        self.numberSpinBox = QSpinBox()
        self.numberSpinBox.setRange(1, 100)
        self.styleCombo = QComboBox(self)
        self.styleCombo.addItem("A4")
        self.styleCombo.addItem("A5")

        controlsLayout = QGridLayout()
        controlsLayout.addWidget(numberLabel, 0, 0)
        controlsLayout.addWidget(self.numberSpinBox, 0, 1)
        controlsLayout.addWidget(pageLabel, 0, 2)
        controlsLayout.addWidget(self.styleCombo, 0, 3)
        controlsLayout.addWidget(self.printButton, 0, 4)
        controlsLayout.addWidget(self.previewStatus, 3, 0)
        controlsLayout.addWidget(self.previewButton, 3, 1)
        self.controlsGroup.setLayout(controlsLayout)

    def creatResult(self, title):
        self.resultGroup = QGroupBox(title)
        self.resultLabel = QLabel("")
        layout = QHBoxLayout()
        layout.addWidget(self.resultLabel)
        self.resultGroup.setLayout(layout)

    def emitPreviewSignal(self):
        if self.previewStatus.isChecked() == True:
            self.previewSignal[int, str].emit(1080, " Full Screen")
        elif self.previewStatus.isChecked() == False:
            self.previewSignal[str].emit("Preview")

    def emitPrintSignal(self):
        pList = []
        pList.append(self.numberSpinBox.value())
        pList.append(self.styleCombo.currentText())
        self.printSignal.emit(pList)

    def printPaper(self, list):
        self.resultLabel.setText("Print: " + "份数：" + str(list[0]) + " 纸张：" + str(list[1]))

    def previewPaperWithArgs(self, style, text):
        self.resultLabel.setText(str(style) + text)

    def previewPaper(self, text):
        self.resultLabel.setText(text)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            self.helpSignal.emit("help message")

    def showHelpMessage(self, message):
        self.resultLabel.setText(message)
        # self.statusBar().showMessage(message)





class EventDealExample(QWidget):
    def __init__(self):
        super().__init__()
        self.justDoubleClicked = False
        self.key = ""
        self.text = ""
        self.message = ""
        self.resize(400, 300)
        self.move(100, 100)
        self.setWindowTitle("Events")
        QTimer.singleShot(0, self.giveHelp)  # Avoids first resize msg

        self.show()

    def giveHelp(self):
        self.text = "Click to toggle mouse tracking"
        self.update()

    def closeEvent(self, event):
        print("Closed")

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        oneAction = menu.addAction("&One")
        twoAction = menu.addAction("&Two")
        oneAction.triggered.connect(self.one)
        twoAction.triggered.connect(self.two)
        if not self.message:
            menu.addSeparator()
            threeAction = menu.addAction("Thre&e")
            threeAction.triggered.connect(self.three)
        menu.exec_(event.globalPos())

    def one(self):
        self.message = "Menu option One"
        self.update()

    def two(self):
        self.message = "Menu option Two"
        self.update()

    def three(self):
        self.message = "Menu option Three"
        self.update()

    def paintEvent(self, event):
        text = self.text
        i = text.find("\n\n")
        if i >= 0:
            text = text[0:i]
        if self.key:
            text += "\n\nYou pressed: {0}".format(self.key)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.drawText(self.rect(), Qt.AlignCenter, text)
        if self.message:
            painter.drawText(self.rect(), Qt.AlignBottom | Qt.AlignHCenter,
                             self.message)
            QTimer.singleShot(5000, self.clearMessage)
            QTimer.singleShot(5000, self.update)

    def clearMessage(self):
        self.message = ""

    def resizeEvent(self, event):
        self.text = "Resized to QSize({0}, {1})".format(
            event.size().width(), event.size().height())
        self.update()

    def mouseReleaseEvent(self, event):
        if self.justDoubleClicked:
            self.justDoubleClicked = False
        else:
            self.setMouseTracking(not self.hasMouseTracking())
            if self.hasMouseTracking():
                self.text = "Mouse tracking is on.\n" + \
                            "Try moving the mouse!\n" + \
                            "Single click to switch it off"
            else:
                self.text = "Mouse tracking is off.\n" + \
                            "Single click to switch it on"
            self.update()

    def mouseMoveEvent(self, event):
        if not self.justDoubleClicked:
            globalPos = self.mapToGlobal(event.pos())
            self.text = "The mouse is at\nQPoint({0}, {1}) " + \
                        "in widget coords, and\n" + \
                        "QPoint({2}, {3}) in screen coords".format(
                            event.pos().x(), event.pos().y(), globalPos.x(),
                            globalPos.y())
            self.update()

    def mouseDoubleClickEvent(self, event):
        self.justDoubleClicked = True
        self.text = "Double-clicked."
        self.update()

    def keyPressEvent(self, event):
        self.key = ""
        if event.key() == Qt.Key_Home:
            self.key = "Home"
        elif event.key() == Qt.Key_End:
            self.key = "End"
        elif event.key() == Qt.Key_PageUp:
            if event.modifiers() & Qt.ControlModifier:
                self.key = "Ctrl+PageUp"
            else:
                self.key = "PageUp"
        elif event.key() == Qt.Key_PageDown:
            if event.modifiers() & Qt.ControlModifier:
                self.key = "Ctrl+PageDown"
            else:
                self.key = "PageDown"
        elif Qt.Key_A <= event.key() <= Qt.Key_Z:
            if event.modifiers() & Qt.ShiftModifier:
                self.key = "Shift+"
            self.key += event.text()
        if self.key:
            self.key = self.key
            self.update()
        else:
            QWidget.keyPressEvent(self, event)

    def event(self, event):
        if (event.type() == QEvent.KeyPress and
                event.key() == Qt.Key_Tab):
            self.key = "Tab captured in  event()"
            self.update()
            return True
        return QWidget.event(self, event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EventDealExample()
    sys.exit(app.exec_())
