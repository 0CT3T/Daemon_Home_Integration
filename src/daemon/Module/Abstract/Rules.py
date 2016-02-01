import json
from daemon.Configuration.Modele import *

class Rules():

    def __init__(self):
        if self.__class__ is Rules:
            raise Exception("ERREUR 01 : Rules is abstract")
        else:
            self.active = False
            self.JSONfilename = self.object.getname() + "/Regle/"+ self.getname() + ".json"

    def set(self):
        self.active = True
        self.saveJSON()

    def clear(self):
        self.active = False
        self.saveJSON()

    def isset(self):
        return self.active

    def exec(self):
        try:
            if self.active == True:
                self.test()
        except:
            pass

    def saveJSON(self):
        with open(JSONdirectory + self.JSONfilename, "w") as fichier:
            fichier.write(self.getJSON())
        return JSONdirectory + self.JSONfilename

    def getJSON(self):
        dic = {'active':self.active}
        return json.dumps(dic)

    def autoloadJSON(self):
        try:
            with open(JSONdirectory + self.JSONfilename, "r") as fichier:
                JSON = fichier.read()
            self.loadJSON(JSON)
        except FileNotFoundError:
            self.saveJSON()
        except ValueError:
            pass

    def loadJSON(self,JSON):
        dic = json.loads(JSON)
        self.active = dic['active']

    def getname(self):
        return self.__class__.__name__

    def getJSONfilename(self):
        return self.JSONfilename