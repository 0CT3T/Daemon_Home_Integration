import json
from daemon.Configuration.Modele import *


class Frequency():

    def __init__(self, objectname):
        self.value = 100
        self.objectname = objectname
        self.JSONfilename = self.getname() + ".json"


    def saveJSON(self):
        with open(JSONdirectory + self.objectname + "/" + self.JSONfilename, "w") as fichier:
            fichier.write(self.getJSON())
        return JSONdirectory + self.objectname + "/" + self.JSONfilename

    def getJSON(self):
        dic = {'value':self.value}
        return json.dumps(dic)

    def autoloadJSON(self):
        try:
            with open(JSONdirectory + self.objectname + "/" + self.JSONfilename, "r") as fichier:
                JSON = fichier.read()
            self.loadJSON(JSON)
        except FileNotFoundError:
            self.saveJSON()
        except ValueError:
            pass

    def loadJSON(self,JSON):
        dic = json.loads(JSON)
        self.value = dic['value']

    def getvalue(self):
        return self.value

    def getname(self):
        return self.__class__.__name__

    def setvalue(self, value):
        self.value = value
        self.saveJSON()

    def getJSONfilename(self):
        return self.JSONfilename
