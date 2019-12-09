import psycopg2
import sys
from PyQt5 import QtWidgets, QtGui
from LoginUI import Ui_Form

class Login(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)

    def accept(self):
        if(self.ifconductor.isChecked()):
            print("con")
            self.conn = psycopg2.connect(database="TicketManagementSystem", user=self.nametext.toPlainText(),
                                         password=self.passwordtext.toPlainText(), host="localhost", port="5432")
            pass
        elif(self.ifmanager.isChecked()):
            self.conn = psycopg2.connect(database="TicketManagementSystem", user=self.nametext.toPlainText(),
                                         password=self.passwordtext.toPlainText(), host="localhost", port="5432")
            pass
        else:
            #弹出窗口，说不能不选择角色就登录
            pass

    def exec(self):
        sys.exit(app.exec())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    loginui = Login()
    loginui.show()
    sys.exit(app.exec())