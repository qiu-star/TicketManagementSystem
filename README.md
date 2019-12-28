# 售票管理系统 - TicketManagementSystem
概述：数据库大作业
# 实验要求
考察本市的长途汽车站或者火车站的售票业务，设计车站售票管理系统。要求可以完成下列功能：
* 具有方便，快速的售票功能，包括车票的预定和退票功能，支持团体的预定和退票。
* 可以方便的查询时刻表或者是车次，票价等信息。
* 可以更改系统中存储的各种信息。
# 实验环境
* 编程语言：python3
* 数据库管理系统：PostgreSQL
# 系统配置
* 在PostgreSQL创建名为TicketManagementSystem数据库，选择tms1228.backup进行restore，创建角色组conductor和manager，然后再运行main.py
# 系统运行截图
* 登录界面
![](https://wx1.sinaimg.cn/mw690/005uWzWaly1gacvfebbvgj30gy0cd74b.jpg)
* 售票员界面
![](https://wx1.sinaimg.cn/mw690/005uWzWaly1gacvficue3j30pk0evq3n.jpg)
    * 售票员选择目标站和发车时间后可以看到车次信息
    ![](https://wx4.sinaimg.cn/mw690/005uWzWaly1gacvflikltj30pn0ezwfn.jpg)
    * 选中想要查看的行，即可看到票价和剩余车票数
    ![](https://wx1.sinaimg.cn/mw690/005uWzWaly1gacvfp66j3j30po0f03zv.jpg)
    * 点击销售，即可进行卖票
    ![](https://wx4.sinaimg.cn/mw690/005uWzWaly1gacvfscuqzj30ew0a3jrp.jpg)
    * 输入乘客身份证，选择票数，系统会自动计算乘客应付的钱数
    ![](https://wx2.sinaimg.cn/mw690/005uWzWaly1gacvgf5wuhj30ez09yt93.jpg)
    * 点击退票，并输入乘客身份证，可以查看该乘客订的所有未退的票的信息
    ![](https://wx1.sinaimg.cn/mw690/005uWzWaly1gacvgi8hb0j30kf0gvq3x.jpg)
    * 选择相应车次，可以看到应返还的钱数
    ![](https://wx1.sinaimg.cn/mw690/005uWzWaly1gacvglvg8gj30kt0h43zk.jpg)
    * 售票员把钱返还给乘客后，点击退订，即退订完毕。可以看到再次查询，该顾客订票信息中只剩余了一张票。
    ![](https://wx1.sinaimg.cn/mw690/005uWzWaly1gacvgp3dw1j30ks0h4754.jpg)
* 管理员界面
![](https://wx3.sinaimg.cn/mw690/005uWzWaly1gacvgs4xecj30li0bmmxs.jpg)
    * 调度功能（以车辆修改为例）
        * 双击需要修改的栏即可进行修改
        ![](https://wx4.sinaimg.cn/mw690/005uWzWaly1gacvh7f71xj30lq0fpmyb.jpg)
        * 然后点击取消，即取消修改（rollback），再进入该界面时发现座位数仍是未修改的值（400）
        ![](https://wx4.sinaimg.cn/mw690/005uWzWaly1gacvheu580j30aw00wweb.jpg)
        * 若点击确定，会提交修改（commit），再进入该界面时发现座位数已经变为修改后的值（600）
        ![](https://wx4.sinaimg.cn/mw690/005uWzWaly1gacvhi3znlj308q00z3yc.jpg)
        * 点击增加，即可增加一行
        ![](https://wx2.sinaimg.cn/mw690/005uWzWaly1gacvhlglkdj30bg03u3yk.jpg)
        * 点击删除即可把这一行删掉
        ![](https://wx1.sinaimg.cn/mw690/005uWzWaly1gacvi0ihmoj30c807g0t7.jpg)
    * 维护功能
        * 在维护功能中可以进行管理员/售票员的增删和修改密码等操作。
        ![](https://wx2.sinaimg.cn/mw690/005uWzWaly1gacvi519nfj30ln0fmjs8.jpg)
        * 增添一位售票员，可以看到添加成功
        ![](https://wx1.sinaimg.cn/mw690/005uWzWaly1gacvi8jicij30kd081jrx.jpg)
        <br>![](https://wx2.sinaimg.cn/mw690/005uWzWaly1gacviclun4j30km06jaau.jpg)</br>
        * 删除该售票员，可以看到删除成功
        ![](https://wx3.sinaimg.cn/mw690/005uWzWaly1gacvigbjpnj30kh04m0t8.jpg)
    * 统计功能
        * 可以看到每个员工卖出的票数
        ![](https://wx4.sinaimg.cn/mw690/005uWzWaly1gacviu4rfnj30gn0du0t4.jpg)
