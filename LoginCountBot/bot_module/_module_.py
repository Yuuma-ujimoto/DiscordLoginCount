import mysql.connector
import datetime
import codecs
import bot_module._utility_ as ut
import config._config_ as config

sqlconnect = mysql.connector.connect(user=config.user, password=config.password, host=config.host,
                                          database=config.database)


#Botのメインになる関数
class DiscordList:
    def __init__(self):
        global sqlconnect

        #mysqlサーバー接続
        self.cur = sqlconnect.cursor()
        #cursor設定
    def login_menber(self):
        l = []
        self.cur.execute("select user_id,server_id from discord")
        for x in self.cur.fetchall():
            l.append(x[0]+x[1])
        return l

    def today_login_menber(self):
        l = []
        dt = ut.Utillity().time_list()

        self.cur.execute("select user_id,server_id from discord where month ={0} and day = {1}".format(dt[0],dt[1]))
        for x in self.cur.fetchall():
            l.append(x[0] + x[1])
        return l
class DiscordCmd:
    def __init__(self):
        #self.sqlconnect = mysql.connector.connect(user=config.user, password=config.password, host=config.host,database=config.database)
        #mysqlサーバー接続
        global sqlconnect
        self.cur = sqlconnect.cursor()
    def new_menber(self,user_name,user_id,server_id,len):
        dt = ut.Utillity().time_list()
        sql_execute("insert into discord Value("
                             "'{0}','{1}','{2}',1,{3},{4},{5},1)"
                             .format(user_id,user_name,server_id,len,dt[0],dt[1]))

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
    def update(self,user_name,user_id):
        sql_execute("update discord set user_name = '{0}' where user_id = '{1}'".format(user_name,user_id))
        m = "```ユーザー名を更新しました```"
        return m
    def help(self):
        m = "```.mc\t発言回数と発言文字数とそれらの平均を表示します。\n" \
               ".lc\t今いるサーバーで何日発言したかを表示します。\n" \
               ".md\t一日当たりの平均発言回数を表示します。\n" \
               ".github\tこのbotのソースコードを表示します。\n" \
               ".update\t登録名を更新します。```"
        return m
class DiscordLog:
    def __init__(self):
        pass
    def user_log(self,log):
        _lof_("user_log",log)
    def cmd_log(self,log):
        _lof_("cmd_log",log)
    def tlogin_log(self,log):
        _lof_("login_log",log)
class DiscrdCount:
    def __init__(self):
        pass

    def word_count(self,user_id,server_id,len):
        sql_execute("update discord set message_count = message_count+1,word_count = word_count+{0} where user_id ='{1}' and server_id = '{2}'".format(len,user_id,server_id))
    def login_count(self,user_id,server_id):
        dt = ut.Utillity().time_list()
        sql_execute("update discord set login_count = login_count+1,month = {0},day = {1} where user_id ='{2}' and server_id = '{3}'".format(dt[0],dt[1],user_id,server_id))
def sql_execute(sql_):
    global sqlconnect
    cur = sqlconnect.cursor()
    try:
        cur.execute(sql_)
        sqlconnect.commit()
    except:
        sqlconnect.rollback()
        raise
def _lof_(file_name,log_message):
    path = "../log"+file_name+".txt"
    f = codecs.open(path, "a", 'utf-8')
    f.write(log_message)
    f.close()
