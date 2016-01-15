import json


class configuration():

    def __init__(self,*args, **kwargs):
        self.litem = []
        self.lrules = []
        if len(args) == 0:
            pass
        else:
            self.__dict__ = json.loads(args[0])

    def load(self,JSON):
        self.__dict__ = json.loads(JSON)

    def getlitem(self):
        return self.litem

    def getlrules(self):
        return self.lrules


