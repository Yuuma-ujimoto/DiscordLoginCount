import datetime

#Botのメインにはならないが便利な関数はここで
class _utillity_:
    def __init__(self):
        self.n = datetime.datetime.now()
        self.m = self.n.month
        self.d = self.n.day

    def time_list(self):
        l = [self.m, self.d]
        return l
    '''def write_log(self,log,l):
        f = codecs.open("../log/"+l,"a", 'utf-8')
        f.write(log)
        f.close()
       '''