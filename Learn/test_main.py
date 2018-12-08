# encoding: utf-8

# C:\Users\Administrator\PycharmProjects\untitled1\src\img\


# Debug
import cgitb

cgitb.enable()
#

import sys
import webbrowser

from Learn.PasswordDialog import PasswordDialog
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QProgressDialog
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QButtonGroup
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QLCDNumber
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QToolBox

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtCore import QRegExp
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QTime
from PyQt5.QtCore import QDateTime
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QSize
# from PyQt5.QtCore import

from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QDesktopServices


class PasswordDialogTest(QWidget):
    def __init__(self):
        super(PasswordDialogTest, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 123)
        self.setWindowTitle("PasswordDialogTest")

        self.lb = QLabel('Password Display here', self)
        self.bt = QPushButton('Input Password', self)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.lb)
        self.vbox.addWidget(self.bt)

        self.setLayout(self.vbox)

        self.bt.clicked.connect(self.showPasswordDialog)

        self.show()

    def showPasswordDialog(self):
        pwd = PasswordDialog()
        pwd.bt1.clicked.connect(lambda: self.lb.setText(pwd.getPassword()))
        pwd.exec_()


# 模板
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 600)

        self.initMemberData()
        self.initWidget()
        self.initLayout()

        self.connect()

        self.show()

    def initMemberData(self):
        pass

    def initWidget(self):
        pass

    def initLayout(self):
        pass

    def connect(self):
        pass


class Example1(QWidget):
    def __init__(self):
        super(Example1, self).__init__()
        self.initUI()

    def initLayout(self):
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.lb)
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.edit)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.bt)

        self.setLayout(self.vbox)

    def initUI(self):
        self.resize(300, 150)
        self.setWindowTitle('Learn')

        self.lb = QLabel('Files Number', self)
        self.bt = QPushButton('Begin', self)
        self.edit = QLineEdit('100000', self)

        self.initLayout()

        self.bt.clicked.connect(self.showDialog)

        self.show()

    def showDialog(self):
        num = int(self.edit.text())
        progress = QProgressDialog(self)
        progress.setWindowTitle('Wait')
        progress.setLabelText('Operating...')
        progress.setCancelButtonText("Cancel")
        progress.setMinimumDuration(5)  # 超过5秒才会显示进度对话框
        progress.setWindowModality(Qt.WindowModal)  # 窗口模态对话框(阻塞所有家族中窗口)
        progress.setRange(0, num)

        # for-else
        for i in range(num):
            progress.setValue(i)
            if progress.wasCanceled():
                QMessageBox.warning(self, 'Tips', 'Operation Failed')
                break
        else:
            progress.setValue(num)
            QMessageBox.information(self, 'Tips', 'Operation Succeeded')


class Example2(QWidget):
    def __init__(self):
        super(Example2, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 300)

        self.cb1 = QCheckBox('SelectAll', self)
        self.cb2 = QCheckBox('You Are', self)
        self.cb3 = QCheckBox('My', self)
        self.cb4 = QCheckBox('Baby', self)

        self.bt = QPushButton('Commit', self)

        self.connect()
        self.initLayout()

        self.show()

    def initLayout(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.cb2)
        vbox.addWidget(self.cb3)
        vbox.addWidget(self.cb4)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.bt)
        vbox2.addStretch(1)
        vbox2.addWidget(self.cb1)
        vbox2.addStretch(1)
        vbox2.addLayout(vbox)

        self.setLayout(vbox2)

    def connect(self):
        self.cb1.stateChanged.connect(self.changecb1)
        self.cb2.stateChanged.connect(self.changecb2)
        self.cb3.stateChanged.connect(self.changecb2)
        self.cb4.stateChanged.connect(self.changecb2)
        self.bt.clicked.connect(self.go)

    def changecb1(self):
        if self.cb1.checkState() == Qt.Checked:
            self.cb2.setChecked(True)
            self.cb3.setChecked(True)
            self.cb4.setChecked(True)
        elif self.cb1.checkState() == Qt.Unchecked:
            self.cb2.setChecked(False)
            self.cb3.setChecked(False)
            self.cb4.setChecked(False)

    def changecb2(self):
        if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
            self.cb1.setChecked(True)
        elif not (self.cb2.isChecked() or self.cb3.isChecked() or self.cb4.isChecked()):
            self.cb1.setCheckState(Qt.Unchecked)

    def go(self):
        if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self, 'I Love U', '你是我的宝贝！')
        elif self.cb2.isChecked() and self.cb3.isChecked():
            QMessageBox.information(self, 'I Love U', '你是我的！')
        elif self.cb2.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self, 'I Love U', '你是宝贝！')
        elif self.cb3.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self, 'I Love U', '我的宝贝！')
        elif self.cb2.isChecked():
            QMessageBox.information(self, 'I Love U', '你是！')
        elif self.cb3.isChecked():
            QMessageBox.information(self, 'I Love U', '我的！')
        elif self.cb4.isChecked():
            QMessageBox.information(self, 'I Love U', '宝贝！')
        else:
            QMessageBox.information(self, 'I Love U', '貌似你没有勾选啊！')


class Example3(QWidget):
    def __init__(self):
        super(Example3, self).__init__()
        self.initMemberVariable()
        self.initUI()

    def initMemberVariable(self):
        self.info1 = ''
        self.info2 = ''

    def initUI(self):
        self.resize(400, 400)
        self.initWidget()
        self.initLayout()
        self.ButtonGroup()
        self.connect()

        self.show()

    def initWidget(self):
        self.rb11 = QRadioButton('你是', self)
        self.rb12 = QRadioButton('我是', self)
        self.rb13 = QRadioButton('他是', self)
        self.rb21 = QRadioButton('大美女', self)
        self.rb22 = QRadioButton('大帅哥', self)
        self.rb23 = QRadioButton('小屁孩', self)
        self.bt = QPushButton('submit', self)

    def ButtonGroup(self):
        self.bg1 = QButtonGroup(self)
        self.bg1.addButton(self.rb11, 11)
        self.bg1.addButton(self.rb12, 12)
        self.bg1.addButton(self.rb13, 13)

        self.bg2 = QButtonGroup(self)
        self.bg2.addButton(self.rb21, 21)
        self.bg2.addButton(self.rb22, 22)
        self.bg2.addButton(self.rb23, 23)

    def initLayout(self):
        grid = QGridLayout()
        grid.addWidget(self.bt, 0, 0, 1, 1)
        grid.addWidget(self.rb11, 1, 0)
        grid.addWidget(self.rb12, 2, 0)
        grid.addWidget(self.rb13, 3, 0)
        grid.addWidget(self.rb21, 1, 1)
        grid.addWidget(self.rb22, 2, 1)
        grid.addWidget(self.rb23, 3, 1)

        self.setLayout(grid)

    def connect(self):
        self.bg1.buttonClicked.connect(self.rbclicked)
        self.bg2.buttonClicked.connect(self.rbclicked)
        self.bt.clicked.connect(self.submit)

    def rbclicked(self):
        sender = self.sender()
        if sender == self.bg1:
            if self.bg1.checkedId() == 11:
                self.info1 = 'you are'
            elif self.bg1.checkedId() == 12:
                self.info1 = '我是'
            elif self.bg1.checkedId() == 13:
                self.info1 = '他是'
            else:
                self.info1 = ''
        else:
            if self.bg2.checkedId() == 21:
                self.info2 = '大美女'
            elif self.bg2.checkedId() == 22:
                self.info2 = '大帅哥'
            elif self.bg2.checkedId() == 23:
                self.info2 = '小屁孩'
            else:
                self.info2 = ''

    def submit(self):
        if self.info1 == '' or self.info2 == '':
            QMessageBox.information(self, 'What?', '貌似有没有选的啊，快去选一个吧！')
        else:
            QMessageBox.information(self, 'What?', self.info1 + self.info2)


class Example4(QWidget):
    def __init__(self):
        super(Example4, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 600)

        self.initMemberData()
        self.initWidget()
        self.initLayout()

        self.initSlider()
        self.initLabel()

        self.connect()

        self.show()

    def initMemberData(self):
        pass

    def initLayout(self):
        pass

    def initWidget(self):
        self.sld1 = QSlider(Qt.Vertical, self)
        self.sld2 = QSlider(Qt.Horizontal, self)
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)

    def connect(self):
        self.sld1.valueChanged[int].connect(self.changevalue)
        self.sld2.valueChanged[int].connect(self.changevalue)

    def initSlider(self):
        self.sld1.setGeometry(30, 40, 30, 100)
        self.sld1.setMinimum(0)
        self.sld1.setMaximum(100)
        self.sld1.setTickPosition(QSlider.TicksLeft)

        self.sld2.setGeometry(500, 350, 100, 30)
        self.sld2.setMinimum(0)
        self.sld2.setMaximum(100)
        self.sld2.setTickPosition(QSlider.TicksAbove)

    def initLabel(self):
        self.label1.setPixmap(QPixmap('./src/img/human1.png'))
        self.label1.setGeometry(80, 150, 600, 180)

        self.label2 = QLabel('滑动块1当前值: 0 ', self)
        self.label2.move(70, 70)

        self.label3 = QLabel('滑动块2当前值: 0 ', self)
        self.label3.move(550, 390)

    def changevalue(self, value):

        sender = self.sender()
        if sender == self.sld1:
            self.sld2.setValue(value)
        else:
            self.sld1.setValue(value)
        self.label2.setText('滑动块1当前值:' + str(value))
        self.label3.setText('滑动块2当前值:' + str(value))

        id = (((value + 20) // 20) % 2) + 1
        pimap = QPixmap('./src/img/human' + str(id) + '.png')
        self.label1.setPixmap(pimap)


class Example5(QWidget):
    def __init__(self):
        super(Example5, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 600)

        self.initMemberData()
        self.initWidget()
        self.initLayout()

        self.connect()

        self.show()

    def initMemberData(self):
        self.timer = QBasicTimer()  # 定时器
        self.step = 0

    def initWidget(self):
        self.pb11 = QProgressBar(self)
        self.pb12 = QProgressBar(self)
        self.pb13 = QProgressBar(self)
        self.pb14 = QProgressBar(self)
        self.pb21 = QProgressBar(self)
        self.pb22 = QProgressBar(self)

        self.bt1 = QPushButton('Out Progress', self)
        self.bt2 = QPushButton('In Progress', self)

        self.pb11.setOrientation(Qt.Horizontal)
        self.pb12.setOrientation(Qt.Vertical)
        self.pb13.setOrientation(Qt.Horizontal)
        self.pb14.setOrientation(Qt.Vertical)

        self.pb21.setFormat("%v")
        self.pb22.setInvertedAppearance(True)

    def initLayout(self):
        self.pb11.setGeometry(70, 40, 450, 20)
        self.pb12.setGeometry(490, 40, 20, 400)
        self.pb13.setGeometry(70, 420, 450, 20)
        self.pb14.setGeometry(70, 40, 20, 400)

        self.pb21.setGeometry(200, 100, 200, 20)
        self.pb22.setGeometry(200, 340, 200, 20)

        self.bt1.move(250, 180)
        self.bt2.move(250, 250)

    def connect(self):
        self.bt1.clicked.connect(self.running)
        self.bt2.clicked.connect(self.doaction)

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            QMessageBox.information(self, 'Tips', 'In finished !')
            self.bt2.setText('Again')
            self.step = 0
        else:
            self.step = self.step + 1
            self.pb21.setValue(self.step)
            self.pb22.setValue(self.step)

    def running(self):
        # 如果最小值和最大值都设置为0，那么栏会显示一个繁忙的指示符
        self.pb11.setMinimum(0)
        self.pb11.setMaximum(0)
        self.pb12.setInvertedAppearance(True)
        self.pb12.setMinimum(0)
        self.pb12.setMaximum(0)
        self.pb13.setInvertedAppearance(True)
        self.pb13.setMinimum(0)
        self.pb13.setMaximum(0)
        self.pb14.setMinimum(0)
        self.pb14.setMaximum(0)

    def doaction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.bt2.setText('Continue')
        else:
            self.timer.start(100, self)  # 100 ms 后定时器停止
            self.bt2.setText('Stop')


class HolyShitBox(QSpinBox):
    def valueFromText(self, p_str):
        regExp = QRegExp("(\\d+)(\\s*[xx]\\s\\d+)?")
        if regExp.exactMatch(p_str):
            return int(regExp.cap(1))
        else:
            return 0

    def textFromValue(self, num):
        return f"{num} x {num}"


class Example6(QWidget):
    def __init__(self):
        super(Example6, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(400, 300)

        self.initMemberData()
        self.initWidget()
        self.initLayout()

        self.connect()

        self.show()

    def initMemberData(self):
        pass

    def initWidget(self):
        self.lb1 = QLabel('普通微调框', self)
        self.lb2 = QLabel('加强微调框', self)
        self.lb3 = QLabel('超神微调框', self)

        self.sp1 = QSpinBox(self)
        self.sp2 = QSpinBox(self)
        self.sp3 = HolyShitBox(self)

        self.sl = QSlider(Qt.Horizontal, self)

        self.sp1.setRange(-100, 100)
        self.sp1.setSingleStep(10)  # 步长
        self.sp1.setWrapping(True)  # 循环
        self.sp1.setValue(-100)

        self.sp2.setRange(0, 100)
        self.sp2.setSingleStep(10)
        self.sp2.setValue(10)
        self.sp2.setPrefix("我的帅达到")
        self.sp2.setSuffix(" %，正在充帅中...")
        self.sp2.setSpecialValueText('我的帅达到渣的一逼')  # 特殊: 当当前值等于minimum()时

        self.sp3.setRange(10, 50)
        self.sp3.setValue(10)
        self.sp3.setWrapping(True)  # 循环

        self.sl.setRange(-100, 100)
        self.sl.setTickPosition(QSlider.TicksAbove)
        self.sl.setValue(-100)

    def initLayout(self):
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()

        hbox1.addWidget(self.lb1)
        hbox1.addStretch(1)
        hbox1.addWidget(self.sp1)
        hbox1.addStretch(1)

        hbox2.addWidget(self.lb2)
        hbox2.addStretch(1)
        hbox2.addWidget(self.sp2)
        hbox2.addStretch(1)

        hbox3.addWidget(self.lb3)
        hbox3.addStretch(1)
        hbox3.addWidget(self.sp3)
        hbox3.addStretch(1)

        # hbox4.addStretch(1)
        hbox4.addWidget(self.sl)
        # hbox4.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)

        self.setLayout(vbox)

    def connect(self):
        self.sp1.valueChanged.connect(self.slider1_changevalue)
        self.sp2.valueChanged.connect(self.slider2_changevalue)
        self.sp3.valueChanged.connect(self.spinbox_changevalue)
        self.sl.valueChanged.connect(self.spinbox_changevalue)

    def slider1_changevalue(self, value):
        self.sl.setValue(value)

    def spinbox_changevalue(self, value):
        self.sp1.setValue(value)

    def slider2_changevalue(self, value):
        if self.sp2.value() == self.sp2.maximum():
            QMessageBox.information(self, '提示', '你怎么还再充帅，你不知道你的帅已经引起了别人的嫉妒吗？')
            self.sp2.setSuffix(" %,我踏马太帅了！！")
        elif self.sp2.maximum() < self.sp2.value() < self.sp2.maximum():
            pass


class Example7(QWidget):
    def __init__(self):
        super(Example7, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 600)

        self.initMemberData()
        self.initWidget()
        self.initLayout()

        self.connect()

        self.show()

    def initMemberData(self):
        self.time = QTimer(self)
        self.time.setInterval(1000)  # 1000 ms = 1s 间隔发出时信号
        self.time.start()

    def initWidget(self):
        self.lcd = QLCDNumber(self)
        self.label = QLabel("Rest Time ", self)

        self.lcd.setDigitCount(12)
        self.lcd.setMode(QLCDNumber.Dec)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        stylesheet = "border: 2px solid black; color:black; background: silver;"
        self.lcd.setStyleSheet(stylesheet)

    def initLayout(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.lcd)
        vbox = QVBoxLayout()
        # vbox.addStretch(1)
        vbox.addLayout(hbox)
        # vbox.addStretch(1)
        self.setLayout(vbox)

    def connect(self):
        self.time.timeout.connect(self.refresh)  # 每秒更新LCD

    def refresh(self):
        # 使用了currentMSecsSinceEpoch()
        # 将其转换成当前时间到1970 - 01 - 01 T00：00：00
        # 世界协调时间以来的毫秒数
        startDate = QDateTime.currentMSecsSinceEpoch()
        endDate = QDateTime(QDate(2020, 2, 4), QTime(0, 0, 0)).toMSecsSinceEpoch()
        interval = endDate - startDate
        if interval > 0:  # ms
            interval = interval // 1000  # s
            day = interval // (24 * 3600)
            hour = (interval % (24 * 3600)) // (3600)
            minute = ((interval % (24 * 3600)) % 3600) // 60
            sec = (((interval % (24 * 3600)) % 3600)) % 60
            intervals = str(day) + ':' + str(hour) + ':' + str(minute) + ":" + str(sec)
            self.lcd.display(intervals)
        else:
            intervals_zero = "000:00:00:00"
            self.lcd.display(intervals_zero)


def test_PasswordDialog():
    app = QApplication(sys.argv)
    ex = PasswordDialogTest()
    sys.exit(app.exec_())


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


def test_4():
    app = QApplication(sys.argv)
    ex = Example4()
    sys.exit(app.exec_())


def test_5():
    app = QApplication(sys.argv)
    ex = Example5()
    sys.exit(app.exec_())


def test_6():
    app = QApplication(sys.argv)
    ex = Example6()
    sys.exit(app.exec_())


def test_7():
    app = QApplication(sys.argv)
    ex = Example7()
    sys.exit(app.exec_())


class Example8(QWidget):
    def __init__(self):
        super(Example8, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 600)

        self.initMemberData()
        self.initWidget()
        self.initLayout()

        self.connect()

        self.show()

    def initMemberData(self):
        self.html = '''
                <style type="text/css">
                    table.imagetable {
                        font-family: verdana,arial,sans-serif;
                        font-size:11px;
                        color:#333333;
                        border-width: 1px;
                        border-color: #999999;
                        border-collapse: collapse;
                    }
                    table.imagetable th {
                        background:#b5cfd2 url('cell-blue.jpg');
                        border-width: 1px;
                        padding: 8px;
                        border-style: solid;
                        border-color: #999999;
                    }
                    table.imagetable td {
                        background:#dcddc0 url('cell-grey.jpg');
                        border-width: 1px;
                        padding: 8px;
                        border-style: solid;
                        border-color: #999999;
                    }
                </style>

                <table class="imagetable">
                    <tr>
                        <th>Info Header 1</th><th>Info Header 2</th><th>Info Header 3</th>
                    </tr>
                    <tr>
                        <td>Text 1A</td><td>Text 1B</td><td>Text 1C</td>
                    </tr>
                    <tr>
                        <td>Text 2A</td><td>Text 2B</td><td>Text 2C</td>
                    </tr>
                </table>
            '''
        self.pix = QPixmap('./src/img/sexy.jpg')
        self.movie_pix = QPixmap('./src/img/movie.gif')

    def initWidget(self):
        self.label_input_1 = QLabel('Input_1', self)
        self.label_input_2 = QLabel('Input_2', self)

        self.bt_input_1 = QPushButton('Input-1', self)
        self.bt_input_2 = QPushButton('Input-2', self)

        self.label_show = QLabel('Hhhaahhh', self)
        self.label_show.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        self.rbt_left = QRadioButton('Left', self)
        self.rbt_middle = QRadioButton('middle', self)
        self.rbt_right = QRadioButton('right', self)
        self.bg1 = QButtonGroup()
        self.bg1.addButton(self.rbt_left, 1)
        self.bg1.addButton(self.rbt_middle, 2)
        self.bg1.addButton(self.rbt_right, 3)

        self.label_rich = QLabel(self)
        self.label_rich.setText(self.html)

        self.label_pix = QLabel(self)
        self.label_pix.setStyleSheet("border: 2px solid red")
        self.label_pix.setPixmap(self.pix)
        self.label_pix.setScaledContents(True)

        self.label_movie = QLabel(self)
        self.label_movie.setPixmap(self.movie_pix)
        self.label_movie.setScaledContents(True)

    def initLayout(self):
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.label_show)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.rbt_left)
        hbox2.addWidget(self.rbt_middle)
        hbox2.addWidget(self.rbt_right)

        vbox1 = QHBoxLayout()
        vbox1.addWidget(self.label_input_1)
        vbox1.addWidget(self.bt_input_1)

        vbox2 = QHBoxLayout()
        vbox2.addWidget(self.label_input_2)
        vbox2.addWidget(self.bt_input_2)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.label_rich)
        hbox3.addWidget(self.label_pix)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(vbox1)
        vbox.addLayout(vbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(self.label_movie)

        self.setLayout(vbox)

    def connect(self):
        self.bg1.buttonClicked.connect(self.showlabel)

        self.bt_input_1.clicked.connect(self.showdialog)
        self.bt_input_1.clicked.connect(self.run_movie)

        self.bt_input_2.clicked.connect(self.showdialog)
        self.bt_input_2.clicked.connect(self.run_movie)

    def run_movie(self):
        movie = QMovie('./src/img/movie.gif')
        self.label_movie.setMovie(movie)
        sender = self.sender()
        if sender == self.bt_input_1:
            movie.start()
        elif sender == self.bt_input_2:
            movie.stop()
            self.label_movie.setPixmap(self.movie_pix)

    def showlabel(self):
        if self.bg1.checkedId() == 1:
            self.label_show.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        elif self.bg1.checkedId() == 2:
            self.label_show.setAlignment(Qt.AlignCenter)
        elif self.bg1.checkedId() == 3:
            self.label_show.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

    def showdialog(self):
        sender = self.sender()
        if sender == self.bt_input_1:
            text, ok = QInputDialog.getText(self, 'input-1', 'Please input')
            if ok:
                self.label_input_1.setText(text)
        elif sender == self.bt_input_2:
            text, ok = QInputDialog.getText(self, 'input-2', 'Please input')
            if ok:
                self.label_input_2.setText(text)


def test_8():
    app = QApplication(sys.argv)
    ex = Example8()
    sys.exit(app.exec_())


class Example9(QWidget):
    def __init__(self):
        super(Example9, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 600)

        self.initMemberData()
        self.initWidget()
        self.initLayout()

        self.connect()

        self.show()

    def initMemberData(self):
        pass

    def initWidget(self):
        tb = QToolButton(self)
        tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        tb.setToolTip('Select the way you pay')
        tb.setPopupMode(QToolButton.MenuButtonPopup)
        tb.setText('Pay Way')
        tb.setIcon(QIcon('./src/img/save.png'))
        tb.setAutoRaise(True)

        menu = QMenu(self)
        self.alipayAct = QAction(QIcon('./src/img/save.png'), 'Alipay', self)
        self.wechatAct = QAction(QIcon('./src/img/save.png'), 'wechat', self)
        self.visaAct = QAction(QIcon('./src/img/save.png'), 'visa', self)

        menu.addAction(self.alipayAct)
        menu.addAction(self.wechatAct)
        menu.addSeparator()
        menu.addAction(self.visaAct)

        tb.setMenu(menu)
        self.show()

        self.alipayAct.triggered.connect(self.on_click)
        self.wechatAct.triggered.connect(self.on_click)
        self.visaAct.triggered.connect(self.on_click)

    def on_click(self):
        # print("hahha")
        sender = self.sender()
        if sender == self.alipayAct:
            url = "https://www.alipay.com/"
        elif self.sender() == self.wechatAct:
            url = 'https://pay.weixin.qq.com/index.php'
        elif self.sender() == self.visaAct:
            url = 'https://www.visa.com.cn/'

        QDesktopServices.openUrl(QUrl(url))

    def initLayout(self):
        pass

    def connect(self):
        pass


def test_9():
    app = QApplication(sys.argv)
    ex = Example9()
    sys.exit(app.exec_())


class Example10(QToolBox):
    def __init__(self):
        super(Example10, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 600)
        self.setWindowFlag(Qt.Dialog)

        self.initMemberData()
        self.initWidget()
        self.initLayout()

        self.connect()

        self.show()

    def initMemberData(self):
        self.favorites = [
            [
                {'des': '百度搜索', 'pic': 'image/se/baidu.ico'},
                {'des': '搜狗搜索', 'pic': 'image/se/sougo.ico'},
                {'des': '必应搜索', 'pic': 'image/se/bing.ico'},
                {'des': '360搜索', 'pic': 'image/se/360.ico'},
                {'des': '谷歌搜索', 'pic': 'image/se/google.ico'},
                {'des': '雅虎搜索', 'pic': 'image/se/yahoo.ico'}
            ],
            [
                {'des': '腾讯视频', 'pic': 'image/v/tengxun.ico'},
                {'des': '搜狐视频', 'pic': 'image/v/sohuvideo.ico'},
                {'des': '优酷视频', 'pic': 'image/v/youku.ico'},
                {'des': '土豆视频', 'pic': 'image/v/tudou.ico'},
                {'des': 'AcFun弹幕', 'pic': 'image/v/acfun.ico'},
                {'des': '哔哩哔哩', 'pic': 'image/v/bilibili.ico'}
            ]
        ]

    def initWidget(self):
        for item in self.favorites:
            groupbox = QGroupBox()
            vlayout = QVBoxLayout(groupbox)
            vlayout.setAlignment(Qt.AlignCenter)
            for category in item:
                toolButton = QToolButton()
                toolButton.setText(category['des'])
                toolButton.setIcon(QIcon(category['pic']))
                toolButton.setIconSize(QSize(64, 64))
                toolButton.setAutoRaise(True)
                toolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
                vlayout.addWidget(toolButton)
                toolButton.clicked.connect(self.run)  #
                name = category['des']

            if name == '雅虎搜索':
                self.addItem(groupbox, '搜索引擎')
            else:
                self.addItem(groupbox, '视频网站')

    def initLayout(self):
        pass

    def connect(self):
        pass

    def run(self):
        # if self.sender().text() == '百度搜索':
        #     webbrowser.open('https://www.baidu.com')
        text = self.sender().text()
        for item in self.favorites:
            for category in item:
                if category['des'] == text:
                    url = 'https://www.baidu.com'
                    webbrowser.open(url)
                    return


def test_10():
    app = QApplication(sys.argv)
    ex = Example10()
    sys.exit(app.exec_())


class Example11(QWidget):
    def __init__(self):
        super(Example11, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 600)

        self.initMemberData()
        self.initWidget()
        self.initLayout()

        self.connect()

        self.show()

    def initMemberData(self):
        pass

    def initWidget(self):
        pass

    def initLayout(self):
        pass

    def connect(self):
        pass


def test_11():
    app = QApplication(sys.argv)
    ex = Example11()
    sys.exit(app.exec_())


if __name__ == '__main__':
    test_11()
