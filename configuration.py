import json


class configuration():

    def __init__(self,*args, **kwargs):
        self.litem = []
        if len(args) == 0:
            self.litem.append('PIR')
            self.litem.append('LED')
        else:
            self.__dict__ = json.loads(args[0])

    def getlitem(self):
        return self.litem


