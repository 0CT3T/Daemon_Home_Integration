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


    def getallmode(self):
        pass



    #####################
    #
    # Parametre
    #
    ########################

    def getallparam(self):
        pass

    def getparamvalue(self, name):
        pass

    def setparamvalue(self, name, value):
        pass

    def getparamJSON(self, name):
        pass

    def getparamJSONfilename(self,name):
        pass

    #####################
    #
    # FUNCTION
    #
    ########################

    def getallfunction(self):
        pass

    def execfunction(self, functionname, *args, **kwargs):
        pass