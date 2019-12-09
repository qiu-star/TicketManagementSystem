import psycopg2
import sys
from PyQt5 import QtWidgets, QtGui
from LoginUI import Ui_Form
from ConductorUI import Ui_Dialog
from SellUI import Ui_Sell
from PyQt5.QtWidgets import  QTableWidgetItem
from RefundUI import Ui_Refund

class Login(QtWidgets.QWidget, Ui_Form):
    def __init__(self, conductorui, sellui, refundui):
        super(Login, self).__init__()
        self.setupUi(self)
        self.conductorui = conductorui
        self.sellui = sellui
        self.refundui = refundui

    def accept(self):
        if(self.ifconductor.isChecked()):
            self.conn = psycopg2.connect(database="TicketManagementSystem", user=self.nametext.toPlainText(),
                                         password=self.passwordtext.toPlainText(), host="localhost", port="5432")
            self.conductorui.connectDB(self.conn, self.sellui, self.refundui, self.nametext.toPlainText())
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

    def connectDB(self,conn, sellui, refundui, conductor):
        self.sellui = sellui
        self.conn = conn
        self.cur = self.conn.cursor()
        self.conductor = conductor
        self.refundui = refundui

        self.cur.execute("select s_sname from station;")
        tmp = self.cur.fetchall()
        slist = []
        for item in tmp:
            slist.append(item[0])#因为返回的结果是[(a,), (b,)]型的
        self.aimstation.addItems(slist)


    def searchdetail(self):
        self.cur.execute("select * from searchdetail( '"+self.aimstation.currentText()
                         +"', cast("+str(self.month.value())+ " as smallint), cast("+ str(self.date.value()) + " as smallint));")
        tmp = self.cur.fetchall()
        tmp = set(tmp)
        self.detail.setRowCount(len(tmp))
        for i, item in enumerate(tmp):
            for j, jtem in enumerate(item):
                if jtem == None:
                    break;
                newitem = QTableWidgetItem(jtem)
                self.detail.setItem(i, j, newitem)
        self.detail.verticalHeader().sectionClicked.connect(self.versectionclicked)
        # self.cur.close()
        # self.conn.close()

    def versectionclicked(self, index):
        #车次
        trainnum = self.detail.selectedItems()[0].text()
        self.cur.execute("select dt_cost from departuretime where dt_trainnum = '"+trainnum+"'")
        self.pricenum = self.cur.fetchall()[0][0]
        self.price.setText(str(self.pricenum))
        #剩票
        self.cur.execute("select * from calcRestTicket('"+trainnum+"');")
        self.restnum = self.cur.fetchall()[0][0]
        self.rest.setText(str(self.restnum))

    def tosell(self):
        # 车次
        trainnum = self.detail.selectedItems()[0].text()
        self.sellui.connectDB(self.conn, trainnum, self.month.value(), self.date.value(),
                              self.aimstation.currentText(), self.pricenum, self.restnum, self.conductor)
        self.sellui.show()

    def torefund(self):
        self.refundui.connectDB(self.conn)
        self.refundui.show()

    def exit(self):
        self.cur.close()
        self.conn.close()
        self.close()


class Sell(QtWidgets.QDialog, Ui_Sell):
    def __init__(self):
        super(Sell, self).__init__()
        self.setupUi(self)
        self.ticketnum.valueChanged.connect(self.valuechanged)

    def valuechanged(self):
        self.sum.setText(str(self.ticketnum.value() * self.price))

    def connectDB(self, conn, trainnum, month, date, aimsname, price, rest, conductor):
        self.conn = conn
        self.cur = self.conn.cursor()
        self.trainnum = trainnum
        self.date = str('2019-')+str(month)+"-"+str(date)
        self.aimsname = aimsname
        self.price = price
        self.ticketnum.setMaximum(rest)
        self.conductor = conductor

    def printticket(self):
        self.cur.execute("select * from sellticket(cast("+ str(self.ticketnum.value())
                        +" as smallint), '"+self.trainnum+"', '"+self.date+"', '"+self.aimsname+"',"+ str(self.price)+", '"
                         +self.conductor+"','"+self.credit.toPlainText()+"');")
        self.cur.fetchall()
        self.conn.commit()
        self.close()

    def exec1(self):
        self.close()

class Refund(QtWidgets.QDialog, Ui_Refund):
    def __init__(self):
        super(Refund, self).__init__()
        self.setupUi(self)

    def connectDB(self, conn):
        self.conn = conn
        self.cur = conn.cursor()

    def searchcredit(self):
        self.cur.execute("select * from searchcredit('"+self.credit.toPlainText()+"');")
        tmp = self.cur.fetchall()
        self.detail.setRowCount(len(tmp))
        self.tcidlist = []
        for i, item in enumerate(tmp):
            sumi = len(item)
            for j, jtem in enumerate(item):
                if(j == sumi - 1):
                    self.tcidlist.append(jtem)
                    continue;
                newitem = QTableWidgetItem(str(jtem))
                self.detail.setItem(i, j, newitem)
        self.detail.clicked.connect(self.showrefundmoney)

    def showrefundmoney(self):
        row = self.detail.selectedItems()[0].row()
        tmp = float(self.detail.item(row, 3).text())
        self.backmoney.setText(str(tmp * 0.8))

    def exit(self):
        self.close()

    def comfirm(self):
        selectrow = self.detail.selectedItems()[0].row()
        self.cur.execute("select refundticket('"+self.tcidlist[selectrow]+"', "+str(self.backmoney.toPlainText())+");")
        self.cur.fetchall()
        self.conn.commit()
        self.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    conductorui = Conductor()
    sellui = Sell()
    refundui = Refund()
    loginui = Login(conductorui, sellui, refundui)
    loginui.show()
    sys.exit(app.exec())