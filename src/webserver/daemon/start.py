from initialisation import *

#################################
#
#   DAEMON du projet
#
######################################

print(lobjet["LED"].getJSON())

#test des objets
#for objet in lobjet.values():
#    objet.loadJSON()
#    objet.run()
#    print(objet.getmode())
#    objet.setmode(2)
#    print(objet.getmode())
#    objet.saveJSON()

while True:
    #tester toutes les regles
    for rule in lrules:
        rule.test()

    #tester tous les objets
    for objet in lobjet.values():
        objet.loadJSON()
        objet.run()
    print(lobjet["LED"].getJSON())

