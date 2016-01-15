import sys
from importlib.machinery import SourceFileLoader
from daemon.Configuration.Modele import *

#############################################################
#
#                   INITIALISATION
#############################################################


# CHARGEMENT DU FICHIER de configuration des modules
with open(JSONdirectory + "module.json", "r") as fichier:
    JSON = fichier.read()
config.load(JSON)



#import des classes et objet
for item in config.getlitem():
    temp = getattr(SourceFileLoader(item,Moduledirectory +item+".py").load_module(), item)
    lobjet[item] = temp()

#import des regles
for rule in config.getlrules():
    temp = SourceFileLoader(rule,Ruledirectory + rule+".py").load_module()
    lrules.append(temp)






