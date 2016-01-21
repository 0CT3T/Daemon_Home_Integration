from daemon.initialisation import *

#################################
#
#   DAEMON du projet
#
######################################



lobjet["PIR"].saveJSON()
lobjet["PIR"].autoloadJSON()



for param in lobjet['PIR'].getAllparam():
    print(lobjet["PIR"].getparamvalue(param))
    print(lobjet["PIR"].getparamJSONfilename(param))

#test des objets
#for objet in lobjet.values():
#    objet.loadJSON()
#    objet.run()
#    print(objet.getmode())
#    objet.setmode(2)
#    print(objet.getmode())
#    objet.saveJSON()




