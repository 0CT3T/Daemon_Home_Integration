import sys
from importlib.machinery import SourceFileLoader
from Configuration.Modele import *

#############################################################
#
#                   INITIALISATION
#############################################################


# CHARGEMENT DU FICHIER de configuration des modules
with open("Configuration/json/module.json", "r") as fichier:
    JSON = fichier.read()
config.load(JSON)

# variable global
lmodule = [] #liste des modules
lobjet = []  #liste des classes

#import des classes
for item in config.getlitem():
    lmodule.append(getattr(SourceFileLoader(item,sys.path[0]+ "/Module/"+item+".py").load_module(), item))


#Creation des classes
for module in lmodule:
    lobjet.append(module())



#test des objets
for objet in lobjet:
    objet.loadJSON()
    objet.run()
    print(objet.getmode())
    objet.setmode(2)
    print(objet.getmode())
    objet.saveJSON()

