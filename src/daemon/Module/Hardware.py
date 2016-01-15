#import section




class Hardware:

    #constructeur
    def __init__(self):
        if self.__class__ is Hardware:
            raise Exception("ERREUR 01 : Hardware is abstract")
        else:
            pass

    def getname(self):
        pass

    def saveJSON(self):
        pass

    def getJSON(self):
        pass

    def getfilename(self):
        pass

    def autoloadJSON(self):
        pass

    def loadJSON(self,JSON):
        pass

    def run(self):
        pass

    def getdata(self):
        pass

    def getallmode(self):
        pass

    def getmode(self):
        pass

    def setmode(self,value):
        pass