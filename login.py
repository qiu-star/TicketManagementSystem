import psycopg2
import sys
from PyQt5 import QtWidgets, QtGui
from LoginUI import Ui_Form
from ConductorUI import Ui_Dialog

class Login(QtWidgets.QWidget, Ui_Form):
    def __init__(self, conductorui):
        super(Login, self).__init__()
        self.setupUi(self)
        self.conductorui = conductorui

    def accept(self):
        if(self.ifconductor.isChecked()):
            self.conn = psycopg2.connect(database="TicketManagementSystem", user=self.nametext.toPlainText(),
                                         password=self.passwordtext.toPlainText(), host="localhost", port="5432")
            self.conductorui.connectDB(self.conn)
            self.conductorui.show()
            self.close()
        elif(self.ifmanager.isChecked()):
            self.conn = psycopg2.connect(database="TicketManagementSystem", user=self.nametext.toPlainText(),
                                         password=self.passwordtext.toPlainText(), host="localhost", port="5432")
            pass
        else:
            #弹出窗口，说不能不选择角色就登录
            pass

    def exec(self):
        sys.exit(app.exec())

class Conductor(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(Conductor, self).__init__()
        self.setupUi(self)

    def connectDB(self,conn):
        self.conn = conn
        self.cur = self.conn.cursor()

        #self.cur.execute("select s_sname from station;")
        #slist = self.cur.fetchall()
        #print(slist)
        #self.aimstation.addItems(['大连', '西安'])

    def searchdetail(self):
        pass
        #cur.execute("select * from searchdetail()")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    conductorui = Conductor()
    loginui = Login(conductorui)
    loginui.show()
    sys.exit(app.exec())