import psycopg2
import sys
from PyQt5 import QtWidgets, QtGui
from LoginUI import Ui_Form

class Login(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    loginui = Login()
    loginui.show()
    sys.exit(app.exec())