import psycopg2
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from LoginUI import Ui_Form
from ConductorUI import Ui_Dialog
from SellUI import Ui_Sell
from PyQt5.QtWidgets import  QTableWidgetItem
from RefundUI import Ui_Refund
from ManagerUI import Ui_Manager
from DispatchUI import Ui_Dispatch
from StaticsUI import Ui_Statics

class Login(QtWidgets.QWidget, Ui_Form):
    def __init__(self, conductorui, managerui):
        super(Login, self).__init__()
        self.setupUi(self)
        self.conductorui = conductorui
        self.managerui = managerui

    def accept(self):
        if(self.ifconductor.isChecked()):
            self.conn = psycopg2.connect(database="TicketManagementSystem", user=self.nametext.toPlainText(),
                                         password=self.passwordtext.toPlainText(), host="localhost", port="5432")
            self.conductorui.connectDB(self.conn, self.nametext.toPlainText())
            self.conductorui.show()
            self.close()
        elif(self.ifmanager.isChecked()):
            self.conn = psycopg2.connect(database="TicketManagementSystem", user=self.nametext.toPlainText(),
                                         password=self.passwordtext.toPlainText(), host="localhost", port="5432")
            self.managerui.connectDB(self.conn)
            self.managerui.show()
            self.close()
        else:
            #弹出窗口，说不能不选择角色就登录
            pass

    def exec(self):
        sys.exit(app.exec())

class Conductor(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(Conductor, self).__init__()
        self.setupUi(self)

    def connectDB(self,conn, conductor):
        self.conn = conn
        self.cur = self.conn.cursor()
        self.conductor = conductor

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
        self.sellui = Sell()
        self.sellui.connectDB(self.conn, trainnum, self.month.value(), self.date.value(),
                              self.aimstation.currentText(), self.pricenum, self.restnum, self.conductor)
        self.sellui.show()

    def torefund(self):
        self.refundui = Refund()
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

class Manager(QtWidgets.QDialog, Ui_Manager):
    def __init__(self):
        super(Manager, self).__init__()
        self.setupUi(self)

    def connectDB(self, conn):
        self.conn = conn
        self.cur = conn.cursor()

    def updatetrain(self):
        self.dispatchui = Dispatch()
        self.dispatchui.connectDB(self.conn, 0)
        self.dispatchui.show()

    def updatestation(self):
        self.dispatchui = Dispatch()
        self.dispatchui.connectDB(self.conn, 1)
        self.dispatchui.show()

    def updatedeparturetime(self):
        self.dispatchui = Dispatch()
        self.dispatchui.connectDB(self.conn, 2)
        self.dispatchui.show()

    def addconductor(self):
        self.dispatchui = Dispatch()
        self.dispatchui.connectDB(self.conn, 3)
        self.dispatchui.show()

    def addmanager(self):
        self.dispatchui = Dispatch()
        self.dispatchui.connectDB(self.conn, 4)
        self.dispatchui.show()

    def showsell(self):
        pass

class Dispatch(QtWidgets.QDialog, Ui_Dispatch):
    def __init__(self):
        super(Dispatch, self).__init__()
        self.setupUi(self)
        self.detail.itemChanged.connect(self.tableupdate)

    def connectDB(self, conn, type):
        self.conn = conn
        self.cur = conn.cursor()
        self.type = type
        if(type == 0):
            hlist = ['车ID', '车型', '座位数']
            self.attrs = ['t_tid', 't_ttype', 't_seatnum']
            self.cur.execute("select * from train;")
            list = self.cur.fetchall()
            self.title.setText('车辆修改')
            self.tablename = "train"
            self.pk = 't_tid'
        elif(type == 1):
            hlist = ['站台ID', '站台名', '站台经度', '站台纬度']
            self.attrs = ['s_sid', 's_sname', 's_slongitude', 's_slatitude']
            self.cur.execute("select * from station;")
            list = self.cur.fetchall()
            self.title.setText('站点修改')
            self.tablename = 'station'
            self.pk = 's_sid'
        elif(type == 2):
            hlist = ['车次','车ID', '终点站',  '发车时间', '检票口', '发车月份', '发车日期', '车票价格']
            self.attrs = ['dt_trainnum', 'dt_tid', 'dt_aimsid',  'dt_departuretime', 'dt_ticketentrance', 'dt_month', 'dt_date', 'dt_cost']
            self.cur.execute("select dt_trainnum,dt_tid, s_sname, dt_departuretime,   dt_ticketentrance, dt_month, dt_date, dt_cost from departuretime,station where dt_aimsid = s_sid;")
            list = self.cur.fetchall()
            self.title.setText('车次修改')
            self.tablename = 'departuretime'
            self.pk = 'dt_trainnum'
        elif(type == 3):
            hlist = ['工号', '用户名', '密码']
            self.attrs = ['c_cid', 'c_cname', 'c_cpassword']
            self.cur.execute("select * from conductor;")
            list = self.cur.fetchall()
            self.title.setText('售票员管理')
            self.tablename = 'conductor'
            self.pk = 'c_cid'
        elif(type == 4):
            hlist = ['工号', '用户名', '密码']
            self.attrs = ['m_mid', 'm_mname', 'm_mpassword']
            self.cur.execute("select * from manager;")
            list = self.cur.fetchall()
            self.title.setText('管理员管理')
            self.tablename = 'manager'
            self.pk = 'm_mid'
        self.setdetail(hlist, list);

    def setdetail(self, hlist, list):
        self.cur.execute("begin transaction;")
        self.detail.setColumnCount(len(hlist))
        self.detail.setHorizontalHeaderLabels(hlist)
        self.detail.setRowCount(len(list))
        self.tablelist = []
        for i, item in enumerate(list):
            line = []
            for j, jtem in enumerate(item):
                if jtem == None:
                    break
                line.append(str(jtem))
                newitem = QTableWidgetItem(str(jtem))
                if ((j == 0) and (self.type != 2)):
                    newitem.setFlags(QtCore.Qt.ItemIsEnabled)
                self.detail.setItem(i, j, newitem)
            self.tablelist.append(line)

    def tableupdate(self):
        selects = self.detail.selectedItems()
        if(len(selects) == 0):
            return
        for s in selects:
            row = s.row()
            c = s.column()
            after = s.text()
            if c == 0:
                before = self.tablelist[row][0]
                self.tablelist[row][0] = after
            else:
                before = self.detail.item(row,0).text()
            if (self.type == 2 and c == 2):
                self.cur.execute("select s_sid from station where s_sname = '"+after+"';")
                after = self.cur.fetchall()[0][0]
            attr = self.attrs[c]
            print("update "+self.tablename+" set "+attr+" = '"
                          + after +"' where "+self.pk+" = '"+str(before)+"';")
            self.cur.execute("update "+self.tablename+" set "+attr+" = '"
                         + after +"' where "+self.pk+" = '"+str(before)+"';")
            if (self.type == 3 or self.type == 4) and (c == 2):
                print("alter user " + self.tablelist[row][1] + " with password '" + str(after) + "';")
                self.cur.execute("alter user "+ self.tablelist[row][1] +" with password '"+str(after)+"';")

    def tableadd(self):
        if(self.type == 1):
            self.cur.execute("select max(s_sid) from station;")
            tmp = [int(self.cur.fetchall()[0][0])+1,'undefine', '0', '0']
            self.cur.execute("insert into station(s_sname, s_slongitude, s_slatitude) values('undefine', 0, 0);")
            self.tablelist.append(tmp)
            cnt = self.detail.rowCount()
            self.detail.setRowCount(cnt + 1)
            newitem = QTableWidgetItem(str(tmp[0]))
            newitem.setFlags(QtCore.Qt.ItemIsEnabled)
            self.detail.setItem(cnt, 0, newitem)
        elif(self.type == 0):
            self.cur.execute("select max(t_tid) from train;")
            tmp = [int(self.cur.fetchall()[0][0]) + 1, '空调硬座', 0]
            self.cur.execute("insert into train(t_ttype, t_seatnum) values ('空调软卧', 300);")
            self.tablelist.append(tmp)
            cnt = self.detail.rowCount()
            self.detail.setRowCount(cnt + 1)
            newitem = QTableWidgetItem(str(tmp[0]))
            newitem.setFlags(QtCore.Qt.ItemIsEnabled)
            self.detail.setItem(cnt, 0, newitem)
        elif(self.type == 2):
            self.cur.execute("INSERT INTO departuretime(dt_tid, dt_aimsid, dt_trainnum, dt_departuretime, dt_ticketentrance, dt_month, dt_date, dt_cost) VALUES (201912091, 10011701, 0, '00:00:00', 0, 0, 0, 0);")
            tmp = [0, '201912091', '10011701', '00:00:00', 0, 0, 0]
            self.tablelist.append(tmp)
            cnt = self.detail.rowCount()
            self.detail.setRowCount(cnt + 1)
        elif(self.type == 3):
            self.cur.execute("select max(c_cid) from conductor;")
            i = self.cur.fetchall()[0][0]
            tmp = [int(i) + 1,'conductor0'+str(int(i) + 1 - 201730219) , '0']
            print("insert into conductor(c_cname, c_cpassword) values ('"+str(tmp[1])+"' , '0');")
            self.cur.execute("insert into conductor(c_cname, c_cpassword) values ('"+str(tmp[1])+"' , '0');")
            print("create user " + tmp[1] + " with password '" + tmp[2] + "';")
            self.cur.execute("create user "+tmp[1]+" with password '"+tmp[2]+"';")
            print("grant " + "conductor to "+tmp[1] +";")
            self.cur.execute("grant " + "conductor to "+tmp[1] +";")
            self.tablelist.append(tmp)
            cnt = self.detail.rowCount()
            self.detail.setRowCount(cnt + 1)
            newitem = QTableWidgetItem(str(tmp[0]))
            newitem.setFlags(QtCore.Qt.ItemIsEnabled)
            self.detail.setItem(cnt, 0, newitem)
            newitem = QTableWidgetItem(str(tmp[1]))
            newitem.setFlags(QtCore.Qt.ItemIsEnabled)
            self.detail.setItem(cnt, 1, newitem)
        elif (self.type == 4):
            self.cur.execute("select max(m_mid) from manager;")
            i = self.cur.fetchall()[0][0]
            tmp = [int(i) + 1, 'manager0' + str(int(i)+1), '0']
            print("insert into manager(m_mname, m_mpassword) values ('" + str(tmp[1]) + "' , '0');")
            self.cur.execute("insert into manager(m_mname, m_mpassword) values ('" + str(tmp[1]) + "' , '0');")
            print("create user " + tmp[1] + " with password '" + tmp[2] + "';")
            self.cur.execute("create user " + tmp[1] + " with password '" + tmp[2] + "';")
            print("grant " + "manager to " + tmp[1] + ";")
            self.cur.execute("grant " + "manager to " + tmp[1] + ";")
            self.tablelist.append(tmp)
            cnt = self.detail.rowCount()
            self.detail.setRowCount(cnt + 1)
            newitem = QTableWidgetItem(str(tmp[0]))
            newitem.setFlags(QtCore.Qt.ItemIsEnabled)
            self.detail.setItem(cnt, 0, newitem)
            newitem = QTableWidgetItem(str(tmp[1]))
            newitem.setFlags(QtCore.Qt.ItemIsEnabled)
            self.detail.setItem(cnt, 1, newitem)

    def tabledelete(self):
        row = self.detail.selectedItems()[0].row()
        item = self.detail.item(row, 0).text()
        print(item)
        print("delete from "+self.tablename+" where "+self.pk+" = '"+str(item)+"';")
        self.cur.execute("delete from " + self.tablename + " where " + self.pk + " = '" + str(item) + "';")
        if (self.type == 3 or self.type == 4):
            self.cur.execute("drop user " + self.detail.item(row, 1).text() + ";")
        self.detail.removeRow(row)
        self.tablelist.remove(self.tablelist[row])


    def accept(self):
        self.conn.commit()
        self.close()

    def exit(self):
        self.conn.rollback()
        self.close()

class Statics(QtWidgets.QDialog, Ui_Statics):
    def __init__(self, conn):
        super(Statics, self).__init__()
        self.setupUi(self)
        self.conn = conn
        self.cur = conn.cursor()
        self.cur.execute("select * from c_tc;")
        tmp = self.cur.fetchall()
        tmp = set(tmp)
        self.detail.setRowCount(len(tmp))
        for i, item in enumerate(tmp):
            for j, jtem in enumerate(item):
                if jtem == None:
                    break;
                newitem = QTableWidgetItem(jtem)
                self.detail.setItem(i, j, newitem)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    conductorui = Conductor()
    managerui = Manager()
    loginui = Login(conductorui, managerui)
    loginui.show()
    sys.exit(app.exec())