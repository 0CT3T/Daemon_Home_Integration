from daemon.initialisation import *

#################################
#
#   DAEMON du projet
#
######################################

print(lobjet["LED"].getJSON())

lobjet["LED"].saveJSON()
lobjet["LED"].autoloadJSON()



for param in lobjet['LED'].getAllparam():
    print(lobjet["LED"].getparamvalue(param))

#test des objets
#for objet in lobjet.values():
#    objet.loadJSON()
#    objet.run()
#    print(objet.getmode())
#    objet.setmode(2)
#    print(objet.getmode())
#    objet.saveJSON()




