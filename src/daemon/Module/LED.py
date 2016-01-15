from daemon.Module.Hardware import Hardware
import json
from daemon.Configuration.Modele import *

class LED(Hardware):

    def __init__(self):
        super().__init__()
        self.allmode = ["ALLUMER","ETEINTE","BLINKER"]
        self.mode = "ETEINTE"
        self.JSONname = "LED.json"

    def saveJSON(self):
        with open(JSONdirectory + self.JSONname, "w") as fichier:
            fichier.write(self.getJSON())
        return JSONdirectory + self.JSONname

    def getJSON(self):
        return json.dumps(self,default=jdefault, indent=4)


    def autoloadJSON(self):
        with open(JSONdirectory + self.JSONname, "r") as fichier:
            JSON = fichier.read()
        self.loadJSON(JSON)

    def loadJSON(self,JSON):
        self.__dict__= json.loads(JSON)

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