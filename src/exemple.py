from initialisation import *

#test des objets
for objet in lobjet.values():
    objet.loadJSON()
    objet.run()
    print(objet.getmode())
    objet.setmode(2)
    print(objet.getmode())
    objet.saveJSON()