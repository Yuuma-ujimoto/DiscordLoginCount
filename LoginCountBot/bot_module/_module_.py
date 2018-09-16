import mysql.connector
import datetime
import codecs
import bot_module._utility_ as ut
#Botのメインになる関数
class discord_list:
    def __init__(self):
        #create databse discord(user_id varchar(500),user_name varchar(500),server_id varchar(500),message_count int,word_count int,month int,day int,login_count int)
        #上記コマンドをmysqlで打ち込めば使えます
        self.sqlconnect = mysql.connector.connect(user='user', password='password', host='host', database='database')#自分が使うデーターベースの情報を入力しておいてください
        #mysqlサーバー接続
        self.cur = self.sqlconnect.cursor()
        #cursor設定
    def login_menber(self):
        l = []
        self.cur.execute("select user_id,server_id from discord")
        for x in self.cur.fetchall():
            l.append(x[0]+x[1])
        return l

    def today_login_menber(self):
        l = []
        dt = ut._utillity_().time_list()

        self.cur.execute("select user_id,server_id from discord where month ={0} and day = {1}".format(dt[0],dt[1]))
        for x in self.cur.fetchall():
            l.append(x[0] + x[1])
        return l
class discord_cmd:
    def __init__(self):
        self.sqlconnect = mysql.connector.connect(user='user', password='password', host='host', database='database')#自分が使うデーターベースの情報を入力しておいてください
        #mysqlサーバー接続
        self.cur = self.sqlconnect.cursor()
    def new_menber(self,user_name,user_id,server_id,len):
        dt = ut._utillity_().time_list()

        try:
            self.cur.execute("insert into discord Value("
                             "'{0}','{1}','{2}',1,{3},{4},{5},1)"
                             .format(user_id,user_name,server_id,len,dt[0],dt[1]))
            self.sqlconnect.commit()
        except:
            self.sqlconnect.rollback()
            raise
    def mc(self,user_id,server_id):
        self.cur.execute("select user_name,message_count,word_count from discord where user_id = '{0}' and server_id = '{1}'".format(user_id,server_id))
        x = self.cur.fetchall()
        m = "```"+str(x[0][0])+"さんは"+str(x[0][1])+"回発言し\n総発言文字数は"+str(x[0][2])+"回\n一回の発言当たりの平均使用文字数は"+str(x[0][2]//x[0][1])+"です。```"
        return m
    def lc(self,user_id,server_id):
        self.cur.execute("select user_name,login_count from discord where user_id = '{0}' and server_id = '{1}'".format(user_id,server_id))
        x = self.cur.fetchall()
        m = "```"+str(x[0][0])+"さんはこのサーバーで"+str(x[0][1])+"日発言しています。```"
        return m
    def md(self,user_id,server_id):

        self.cur.execute("select user_name,login_count,message_count from discord where user_id = '{0}' and server_id = '{1}'".format(user_id,server_id))
        x = self.cur.fetchall()
        m = "```"+str(x[0][0])+"さんの一日当たりの平均発言回数は"+str(x[0][2]//x[0][1])+"です。```"
        return m
    def help(self):
        m = "```.mc\t発言回数と発言文字数とそれらの平均を表示します。\n" \
               ".lc\t今いるサーバーで何日発言したかを表示します。\n" \
               ".md\t一日当たりの平均発言回数を表示します。```"
        return m
class discord_log:
    def __init__(self):
        pass
    def user_log(self,log):
        f = codecs.open("../log/user_log.txt", "a", 'utf-8')
        f.write(log)
        f.close()
    def cmd_log(self,log):
        f = codecs.open("../log/cmd_log.txt", "a", 'utf-8')
        f.write(log)
        f.close()
    def tlogin_log(self,log):
        f = codecs.open("../log/login_log.txt", "a", 'utf-8')
        f.write(log)
        f.close()
class discrd_count:
    def __init__(self):
        self.sqlconnect = mysql.connector.connect(user='user', password='password', host='host', database='database')#自分が使うデーターベースの情報を入力しておいてください
        #mysqlサーバー接続
        self.cur = self.sqlconnect.cursor()

    def word_count(self,user_id,server_id,len):
        try:
            self.cur.execute("update discord set message_count = message_count+1,word_count = word_count+{0} where user_id ='{1}' and server_id = '{2}'".format(len,user_id,server_id))
            self.sqlconnect.commit()
        except:
            self.sqlconnect.rollback()
            raise

    def login_count(self,user_id,server_id):
        dt = ut._utillity_().time_list()
        try:
            self.cur.execute("update discord set login_count = login_count+1,month = {0},day = {1} where user_id ='{2}' and server_id = '{3}'".format(dt[0],dt[1],user_id,server_id))
            self.sqlconnect.commit()
        except:
            self.sqlconnect.rollback()
            raise
