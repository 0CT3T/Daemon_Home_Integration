from Module.Hardware import Hardware
import json
from Configuration.Modele import *

class LED(Hardware):

    def __init__(self):
        super().__init__()
        self.allmode = ["ALLUMER","ETEINTE","BLINKER"]
        self.mode = "ETEINTE"
        self.JSONurl = "Configuration/json/LED.json"

    def saveJSON(self):
        bj = json.dumps(self,default=jdefault,indent=4)
        with open(self.JSONurl, "w") as fichier:
            fichier.write(self.getJSON())
        return self.JSONurl

    def getJSON(self):
        obj = json.dumps(self,default=jdefault)
        return obj

    def loadJSON(self):
        with open(self.JSONurl, "r") as fichier:
            JSON = fichier.read()
        self.loadJSON(JSON)

    def loadJSON(self,JSON):
        self.__dict__= json.loads(JSON)

    #run pour utiliser le driver
    #à implementer
    def run(self):
        print(self.mode)

    def getname(self):
        return self.__name__

    def getfilename(self):
        return 'LED.JSON'

    def getallmode(self):
        return self.allmode

    def getmode(self):
        return self.mode

    def setmode(self,value):
        self.mode = value
        self.saveJSON()