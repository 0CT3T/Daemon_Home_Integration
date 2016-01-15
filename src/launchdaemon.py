from daemon.initialisation import *

#################################
#
#   DAEMON du projet
#
######################################

print(lobjet["LED"].getname())

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
        try:
            objet.autoloadJSON()
        except FileNotFoundError:
            pass
        objet.run()
