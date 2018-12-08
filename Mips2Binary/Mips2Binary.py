'''
Transform Mips to BinaryCode
'''

# Debug
import cgitb

cgitb.enable()
#


import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import MBmap


class TransformMw(QWidget):
    def __init__(self):
        super(TransformMw, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Mips2Binary')
        self.resize(800, 600)

        self.initMemberData()
        self.initWidget()
        self.initLayout()

        self.connect()

        self.show()

    def initMemberData(self):
        self.text = ""

    def initWidget(self):
        self.lb_Mips = QLabel('Mips', self)
        self.te_Mips = QTextEdit(self)
        self.te_Mips.setAcceptRichText(False)
        self.te_Mips.setFont(QFont("微软雅黑", 10))

        self.bt_Mips2Binary = QPushButton('Mips2Binary', self)
        self.bt_openfile = QPushButton('OpenFile', self)
        self.bt_choicefont = QPushButton('Font', self)
        self.bt_choicecolor = QPushButton('Color', self)

        self.lb_Binary = QLabel('Binary', self)
        self.bt_Binary2Mips = QPushButton('Binary2Mips', self)
        self.te_Binary = QTextEdit(self)
        self.te_Binary.setFont(QFont("微软雅黑", 10))

        self.bt_byte_format = QPushButton('按字节对齐', self)
        self.bt_B2H = QPushButton('十六进制', self)

        self.bt_about = QPushButton('关于', self)

    def initLayout(self):
        hboxtop = QHBoxLayout()
        hboxtop.addWidget(self.bt_openfile)
        hboxtop.addSpacing(1)
        hboxtop.addWidget(self.bt_choicefont)
        hboxtop.addSpacing(1)
        hboxtop.addWidget(self.bt_choicecolor)
        hboxtop.addSpacing(1)
        hboxtop.addWidget(self.bt_about)
        hboxtop.addStretch(1)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.lb_Mips)
        hbox1.addSpacing(2)
        hbox1.addWidget(self.bt_Mips2Binary)
        hbox1.addStretch(1)

        vbox_Mips = QVBoxLayout()
        vbox_Mips.addLayout(hbox1)
        vbox_Mips.addSpacing(1)
        vbox_Mips.addWidget(self.te_Mips)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.lb_Binary)
        hbox2.addSpacing(2)
        hbox2.addWidget(self.bt_B2H)
        hbox2.addSpacing(1)
        hbox2.addWidget(self.bt_byte_format)
        hbox2.addSpacing(2)
        hbox2.addWidget(self.bt_Binary2Mips)
        hbox2.addStretch(1)

        vbox_Binary = QVBoxLayout()
        vbox_Binary.addLayout(hbox2)
        vbox_Binary.addSpacing(1)
        vbox_Binary.addWidget(self.te_Binary)

        hboxCentral = QHBoxLayout()
        hboxCentral.addLayout(vbox_Mips)
        hboxCentral.addSpacing(5)
        hboxCentral.addLayout(vbox_Binary)

        vboxGeneral = QVBoxLayout()
        vboxGeneral.addLayout(hboxtop)
        vboxGeneral.addLayout(hboxCentral)

        self.setLayout(vboxGeneral)

    def connect(self):
        self.bt_Mips2Binary.clicked.connect(self.Mips2Binary)
        self.bt_Binary2Mips.clicked.connect(self.Binary2Mips)
        self.bt_openfile.clicked.connect(self.openfile)
        self.bt_choicefont.clicked.connect(self.choicefont)
        self.bt_choicecolor.clicked.connect(self.choicecolor)
        self.bt_byte_format.clicked.connect(self.toByteFormat)
        self.bt_B2H.clicked.connect(self.Bin2Hex)
        self.bt_about.clicked.connect(self.aboutAuthor)

    def aboutAuthor(self):
        message = '技术支持: PyQt\n关于作者: ? ? ?\n友情提示:\n复制粘贴撤销全选快捷键可用\n请勿输入极端值'
        reply = QMessageBox.about(self, 'About', message)

    def toByteFormat(self):
        self.text = self.te_Binary.toPlainText()
        binary_lines = self.text.splitlines()
        self.te_Binary.clear()
        for line in binary_lines:
            line = line.replace(' ','')
            if len(line) == 32:
                newline = line[0:8] + ' ' + line[8: 16] + ' ' + line[16:24] + ' ' + line[24:32]
                self.te_Binary.append(newline)
            else:
                self.te_Binary.append('ParseError')

    def Mips2Binary(self):
        self.text = self.te_Mips.toPlainText()
        mips_lines = self.text.splitlines()
        self.te_Binary.clear()
        for line in mips_lines:
            self.te_Binary.append(MBmap.M2B(line))

    def Binary2Mips(self):
        QMessageBox.information(self, 'Sorry', '本功能暂时还没有(不会有了')

    def Bin2Hex(self):
        self.text = self.te_Binary.toPlainText()
        binary_lines = self.text.splitlines()
        self.te_Binary.clear()
        for line in binary_lines:
            self.te_Binary.append(MBmap.B2H(line))

    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, '打开文件', './')
        if fname[0]:
            with open(fname[0], 'r', encoding='utf-8', errors='ignore') as f:
                self.te_Mips.setText(f.read())

    def choicefont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.te_Mips.selectAll()
            self.te_Mips.setCurrentFont(font)
            self.te_Mips.setFocus()

    def choicecolor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.te_Mips.selectAll()
            self.te_Mips.setTextColor(col)
            self.te_Mips.setFocus()



def run_app():
    app = QApplication(sys.argv)
    ex = TransformMw()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_app()
