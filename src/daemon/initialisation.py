
from importlib.machinery import SourceFileLoader
from daemon.Configuration.Modele import *
from daemon.Configuration.configuration import configuration

#############################################################
#
#                   INITIALISATION
#############################################################

lobjet = {}  #liste des classes
lmodrules = [] #liste des modules de regle
config = configuration()


# CHARGEMENT DU FICHIER de configuration des modules
with open(JSONdirectory + "module.json", "r") as fichier:
    JSON = fichier.read()
config.load(JSON)



#import des classes et objet
for item in config.getlitem():
    temp = getattr(SourceFileLoader(item,Moduledirectory +item+".py").load_module(), item)
    lobjet[item] = temp()








