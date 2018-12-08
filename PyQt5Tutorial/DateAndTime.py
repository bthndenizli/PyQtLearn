from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QToolTip, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont

import sys


def DateAndTime():
    # Date
    now = QDate.currentDate()

    print(now)
    print(now.toString(Qt.ISODate))
    print(now.toString(Qt.DefaultLocaleLongDate))

    # Date and time
    datetime = QDateTime.currentDateTime()

    print(datetime)
    print(datetime.toString())

    # Time
    time = QTime.currentTime()

    print(time)
    print(time.toString(Qt.DefaultLocaleLongDate))


def UTCTime():
    now = QDateTime.currentDateTime()
    print(f"Local Time: {now.toString()}")
    print(f"Universal datetime: ", now.toUTC().toString())

    print(f"The offset from UTC is {now.offsetFromUtc()} seconds")


def UnixEpoch():
    now = QDateTime.currentDateTime()
    unix_time = now.toSecsSinceEpoch()
    print(unix_time)

    d = QDateTime.fromSecsSinceEpoch(unix_time)
    print(d.toString())


if __name__ == '__main__':
    pass
