import sys
from importlib.machinery import SourceFileLoader
from daemon.Configuration.Modele import *

#############################################################
#
#                   INITIALISATION
#############################################################


# CHARGEMENT DU FICHIER de configuration des modules
with open("daemon/Configuration/json/module.json", "r") as fichier:
    JSON = fichier.read()
config.load(JSON)



#import des classes et objet
for item in config.getlitem():
    temp = getattr(SourceFileLoader(item,sys.path[0]+ "/daemon/Module/"+item+".py").load_module(), item)
    lobjet[item] = temp()

#import des regles
for rule in config.getlrules():
    temp = SourceFileLoader(rule,sys.path[0]+ "/daemon/Rules/"+rule+".py").load_module()
    lrules.append(temp)






