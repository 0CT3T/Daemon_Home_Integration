#import section
from daemon.Configuration.Modele import *
from importlib.machinery import SourceFileLoader
import os, re, json, threading




class Hardware:


    #############################
    #
    # CONSTRUCTEUR
    #
    ############################
    def __init__(self):
        if self.__class__ is Hardware:
            raise Exception("ERREUR 01 : Hardware is abstract")
        else:
            self.allmode = []
            self.JSONname = self.getname() + ".json"
            self.parametre = {}
            self.attribute = []
            self.functionname = []
            self.function = {}
            self.startfunc = ""
            self.funcattribut = {}
            self.route = {}
            self.reglename = []
            self.regle = {}


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

            #Chercher toutes les regles dans le dossier LED
            for path, dirs, files in os.walk(Moduledirectory + self.getname() + "/Regle/"):
                for file in files:
                    if re.match(r"(.)+.py$", file) != None:
                        self.reglename.append(file[:-3])

            #import des regles
            for item in self.reglename:
                temp = getattr(SourceFileLoader(item,Moduledirectory + self.getname() + "/Regle/" + item+".py").load_module(), item)
                self.regle[item] = temp(self)

            self.autoloadJSON()


    def saveJSON(self):
        with open(JSONdirectory + self.getname() + "/" + self.JSONname, "w") as fichier:
            fichier.write(self.getJSON())
        return JSONdirectory + self.getname() + '/' + self.JSONname

    def getJSON(self):
        dic = {'allmode':self.allmode,'startfunction':self.startfunc,'funcattribut':self.funcattribut}
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

        #autoload all rules
        for item in self.reglename:
            self.regle[item].autoloadJSON()


    def loadJSON(self,JSON):
        dic = json.loads(JSON)
        self.allmode = dic['allmode']
        self.startfunc = dic['startfunction']
        self.funcattribut = dic['funcattribut']

    def run(self):
        if self.startfunc != "":
            self.execfunction(self.startfunc,self.funcattribut)
            #resetfunction
            self.setfunction("",{})

        #stop les regles si fonction active
        try:
            if not self.threading.isAlive():
                for rule in self.regle.values():
                    rule.exec()
        except:
            for rule in self.regle.values():
                    rule.exec()

    #####################
    #
    # ACCESSEURS
    #
    ########################



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

    def setfunction(self, name, attribut):
        self.startfunc = name
        self.funcattribut = attribut
        self.saveJSON()

    def getfunction(self):
        return self.startfunc

    def getattributfunction(self, functionname):
        return self.function[functionname].getAttribut()


    def execfunction(self, functionname, funcattribut):
        #mettre les parametre
        try:
            if len(funcattribut) == 0:
                pass
            else:
                for key in funcattribut.keys():
                    self.setparamvalue(key,funcattribut[key])

            #set le thread
            if self.threading.isAlive():
                self.threading.stop()
            while self.threading.isAlive():
                pass


                #self.threading.close()
        except AttributeError:
            pass
        except:
             pass

        #Demarrer thread de la function
        temp = getattr(SourceFileLoader(functionname,Moduledirectory + self.getname() + "/Function/" + functionname+".py").load_module(), functionname)


        self.threading = temp(self)
        self.threading.setName(functionname)
        self.threading.setDaemon(True)
        self.threading.start()

    #####################
    #
    # OBJET CONNECTEE
    #
    ########################


    def addobjet(self,objet):
        self.route[objet.getname()] = objet

    def getobjet(self,name):
        return self.route[name]

    def getallobjet(self):
        return list(self.route.keys())

    def removeobjet(self,name):
        self.route.pop(name, None)

    #####################
    #
    # REGLE
    #
    ########################

    def setRule(self,name):
        self.regle[name].set()

    def clearRule(self,name):
        self.regle[name].clear()

    def isSetRule(self,name):
        return self.regle[name].isset()

    def getallrules(self):
        return self.reglename

    def getruleJSON(self, name):
        return self.regle[name].getJSON()

    def getruleJSONfilename(self,name):
        return self.regle[name].getJSONfilename()