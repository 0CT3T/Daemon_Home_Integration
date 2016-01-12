
from Configuration.configuration import configuration
from Configuration.Modele import *



######### CHARGEMENT DU FICHIER ###
with open("Configuration/module.conf", "r") as fichier:
    JSON = fichier.read()
config.load(JSON)




#variable
lmodule = []
lobjet = []

#import des modules
for item in config.getlitem():
    lmodule.append(my_import('Module.' + item))

#Creation des objets
for module in lmodule:
    lobjet.append(module())

#test des objets
for objet in lobjet:
    objet.run()
    print(objet.getmode())
    objet.setmode(2)
    print(objet.getmode())
    objet.saveJSON()

