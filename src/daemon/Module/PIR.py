from daemon.Module.Hardware import Hardware
import json
from daemon.Configuration.Modele import *
from importlib.machinery import SourceFileLoader

import os, re

class PIR(Hardware):



    def __init__(self):
        super().__init__()
        self.allmode = ["ALLUMER","ETEINTE"]
        self.JSONname = self.getname()+".json"
        self.parametre = {}
        self.attribute = []

        #Chercher tous les attributs dans le dossier LED
        for path, dirs, files in os.walk(Moduledirectory + self.getname() + "/Attribut/"):
            for file in files:
                if re.match(r"(.)+.py$", file) != None:
                    self.attribute.append(file[:-3])

        #import des Attributs
        for item in self.attribute:
            temp = getattr(SourceFileLoader(item,Moduledirectory + self.getname() + "/Attribut/" + item+".py").load_module(), item)
            self.parametre[item] = temp(self.getname())


    def saveJSON(self):
        with open(JSONdirectory + self.getname() + "/" + self.JSONname, "w") as fichier:
            fichier.write(self.getJSON())
        return JSONdirectory + self.getname() + '/' + self.JSONname

    def getJSON(self):
        dic = {'allmode':self.allmode}
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
        self.allmode = dic['allmode']

    #run pour utiliser le driver
    #à implementer
    #def run(self):
        #print(self.getparamvalue("Mode"))


    def getname(self):
        return self.__class__.__name__

    def getfilename(self):
        return self.JSONname

    def getallmode(self):
        return self.allmode

    #####################
    #
    # Parametre
    #
    ########################

    def getallparam(self):
        return self.attribute

    def getparamvalue(self, name):
        return self.parametre[name].getvalue()

    def setparamvalue(self, name, value):
        self.parametre[name].setvalue(value)

    def getparamJSON(self, name):
        return self.parametre[name].getJSON()

    def getparamJSONfilename(self,name):
        return self.parametre[name].getJSONfilename()