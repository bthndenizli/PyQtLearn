from GUI import GatherExample
from PyQt5 import QtCore, QtWidgets, QtGui

import sys


class MainWindow():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        mw = QtWidgets.QMainWindow()
        self.ui = GatherExample.Ui_MainWindow()
        self.ui.setupUi(mw)

        self.connect()

        mw.show()
        sys.exit(app.exec_())

    def connect(self):
        #
        self.ui.calendarWidget.selectionChanged.connect(self.update_date)
        #
        self.ui.dial.valueChanged[int].connect(self.set_lcd)
        #
        self.ui.radioButton_2.clicked.connect(self.ui.progressBar.reset)
        #
        self.ui.radioButton_3.clicked.connect(self.update_process)
        # set font
        self.ui.fontComboBox.activated[str].connect(self.ui.label.setText)

    # slot func
    def update_date(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())

    def update_calender(self):
        pass

    def set_lcd(self, n):
        self.ui.lcdNumber.display(n)

    def update_process(self):
        value = self.ui.lcdNumber.value()
        self.ui.progressBar.setValue(value)


if __name__ == '__main__':
    MainWindow()
