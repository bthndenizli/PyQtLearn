from GUI import tableMW
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import  *



def set_table_item():
    ui.tableWidget.setItem(0 , 0,QTableWidgetItem("Data 0"))
    ui.tableWidget.setItem(1 , 1,QTableWidgetItem("Data 1"))
    ui.tableWidget.setItem(2 , 2,QTableWidgetItem("Data 2"))


def button_clickded():
        ui.pushButton.setText('Button Clicked.')
        ui.pushButton_2.setText('Button Clicked.')
        ui.pushButton_3.setText('3')



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = tableMW.Ui_MainWindow()
    ui.setupUi(MainWindow)

    set_table_item()

    ui.pushButton.clicked.connect(button_clickded)
    ui.pushButton_2.clicked.connect(button_clickded)
    ui.pushButton_3.clicked.connect(button_clickded)


    MainWindow.show()
    sys.exit(app.exec_())
