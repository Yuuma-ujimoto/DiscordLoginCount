import datetime
import codecs
#Botのメインにはならないが便利な関数はここで
class Utillity:
    def __init__(self):
        self.n = datetime.datetime.now()
        self.m = self.n.month
        self.d = self.n.day

    def time_list(self):
        l = [self.m, self.d]
        return l
    def _log_(self,file_name, log_message):
        path = "../log/" + file_name + ".txt"
        f = codecs.open(path, "a", 'utf-8')
        f.write(log_message)
        f.close()
