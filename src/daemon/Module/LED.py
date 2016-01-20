from daemon.Module.Hardware import Hardware
import json
from daemon.Configuration.Modele import *
from importlib.machinery import SourceFileLoader

class LED(Hardware):



    def __init__(self):
        super().__init__()
        self.allmode = ["ALLUMER","ETEINTE","BLINKER"]
        self.mode = "ETEINTE"
        self.JSONname = "LED.json"
        self.parametre = {}
        self.attribute = ["Frequency"]
        #import des classes et objet
        for item in self.attribute:
            temp = getattr(SourceFileLoader(item,Moduledirectory + self.getname() + "/" + item+".py").load_module(), item)
            self.parametre[item] = temp(self.getname())


    def saveJSON(self):
        with open(JSONdirectory + self.getname() + "/" + self.JSONname, "w") as fichier:
            fichier.write(self.getJSON())
        return JSONdirectory + self.getname() + '/' + self.JSONname

    def getJSON(self):
        return json.dumps(self.mode,default=jdefault)


    def autoloadJSON(self):
        with open(JSONdirectory + self.getname() + "/" + self.JSONname, "r") as fichier:
            JSON = fichier.read()
        self.loadJSON(JSON)

    def loadJSON(self,JSON):
        self.mode = json.loads(JSON)

    #run pour utiliser le driver
    #à implementer
    def run(self):
        print(self.mode)

    def getname(self):
        return self.__class__.__name__

    def getfilename(self):
        return self.JSONname

    def getallmode(self):
        return self.allmode

    def getmode(self):
        return self.mode

    def setmode(self,value):
        self.mode = value
        self.saveJSON()

    def getAllparam(self):
        return self.attribute

    def getparamvalue(self, name):
        return self.parametre[name].getvalue()

    def setparamvalue(self, name, value):
        self.parametre[name].setvalue(value)