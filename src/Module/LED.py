from Module.Hardware import Hardware
import json
from Configuration.Modele import *

class LED(Hardware):

    def __init__(self):
        super().__init__()
        self.allmode = ["ALLUMER","ETEINTE","BLINKER"]
        self.mode = 1
        self.JSONurl = "Configuration/json/LED.json"

    def saveJSON(self):
        obj = json.dumps(self,default=jdefault,indent=4)
        with open(self.JSONurl, "w") as fichier:
            fichier.write(obj)
        return self.JSONurl

    def loadJSON(self):
        with open(self.JSONurl, "r") as fichier:
            JSON = fichier.read()
        self.__dict__= json.loads(JSON)

    #run pour utiliser le driver
    #à implementer
    def run(self):
        print("LED")

    def getname(self):
        return self.__name__

    def getallmode(self):
        return self.allmode

    def getmode(self):
        return self.allmode[self.mode]

    def setmode(self,value):
        self.mode = value