from daemon.Module.Hardware import Hardware
from daemon.Configuration.Modele import *
from importlib.machinery import SourceFileLoader
import os, re, json, threading

class LED(Hardware):

    threading


    def __init__(self):
        super().__init__()
        self.allmode = ["ALLUMER","ETEINTE","BLINKER"]
        self.JSONname = self.getname() + ".json"
        self.parametre = {}
        self.attribute = []
        self.functionname = []
        self.function = {}



        #Chercher tous les attributs dans le dossier LED
        for path, dirs, files in os.walk(Moduledirectory + self.getname() + "/Attribut/"):
            for file in files:
                if re.match(r"(.)+.py$", file) != None:
                    self.attribute.append(file[:-3])

        #import des Attributs
        for item in self.attribute:
            temp = getattr(SourceFileLoader(item,Moduledirectory + self.getname() + "/Attribut/" + item+".py").load_module(), item)
            self.parametre[item] = temp(self.getname())

        #Chercher toutes les fonctions dans le dossier LED
        for path, dirs, files in os.walk(Moduledirectory + self.getname() + "/Function/"):
            for file in files:
                if re.match(r"(.)+.py$", file) != None:
                    self.functionname.append(file[:-3])

        #import des fonctions
        for item in self.functionname:
            temp = getattr(SourceFileLoader(item,Moduledirectory + self.getname() + "/Function/" + item+".py").load_module(), item)
            self.function[item] = temp(self)

        #temp = getattr(SourceFileLoader("driver_LED",Moduledirectory + self.getname() + "/Driver/driver_LED.py").load_module(), "driver_LED")
        #self.driver = temp()

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

    #####################
    #
    # RUN
    #
    ########################

    def run(self):

        if self.threading.is_alive():
            print(self.getparamvalue("Mode"))
        else:
            print(self.getparamvalue("Mode"))
            #if self.getparamvalue("Mode") == "ALLUMER":
            #    self.driver.allumer(100)
            #if self.getparamvalue("Mode") == "ETEINTE":
            #    self.driver.stop()
            #if self.getparamvalue("Mode") == "BLINKER":
            #    self.driver.blink(20,20)

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

    #####################
    #
    # FUNCTION
    #
    ########################

    def getallfunction(self):
        return self.functionname

    def execfunction(self, functionname, *args, **kwargs):
        #mettre les parametre
        try:
            if len(args) == 0:
                pass
            else:
                print(args)
                for dic in args:
                    for key in dic.keys():
                        self.setparamvalue(key,dic[key])
        except:
            pass

        self.threading = self.function[functionname]
        self.threading.setDaemon(True)
        self.threading.start()