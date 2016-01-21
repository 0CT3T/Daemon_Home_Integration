from daemon.Module.Hardware import Hardware
import json
from daemon.Configuration.Modele import *
from importlib.machinery import SourceFileLoader

import os, re

class LED(Hardware):



    def __init__(self):
        super().__init__()
        self.allmode = ["ALLUMER","ETEINTE","BLINKER"]
        self.mode = "ETEINTE"
        self.JSONname = "LED.json"
        self.parametre = {}
        self.attribute = []

        #Chercher tous les attributs dans le dossier LED
        for path, dirs, files in os.walk(Moduledirectory + self.getname() + "/"):
            for file in files:
                if re.match(r"(.)+.py$", file) != None:
                    self.attribute.append(file[:-3])

        #import des Attributs
        for item in self.attribute:
            temp = getattr(SourceFileLoader(item,Moduledirectory + self.getname() + "/" + item+".py").load_module(), item)
            self.parametre[item] = temp(self.getname())


    def saveJSON(self):
        with open(JSONdirectory + self.getname() + "/" + self.JSONname, "w") as fichier:
            fichier.write(self.getJSON())
        return JSONdirectory + self.getname() + '/' + self.JSONname

    def getJSON(self):
        dic = {'mode':self.mode}
        return json.dumps(dic)


    def autoloadJSON(self):
        #load himself
        try:
            with open(JSONdirectory + self.getname() + "/" + self.JSONname, "r") as fichier:
                JSON = fichier.read()
            self.loadJSON(JSON)
        except FileNotFoundError:
            self.saveJSON()
        except ValueError:
            pass
        #autoload all attribute
        for item in self.attribute:
            self.parametre[item].autoloadJSON()

    def loadJSON(self,JSON):
        dic = json.loads(JSON)
        self.mode = dic['mode']

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

    def getparamJSON(self, name):
        return self.parametre[name].getJSON()

    def getparamJSONfilename(self,name):
        return self.parametre[name].getJSONfilename()