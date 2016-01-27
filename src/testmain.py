from daemon.initialisation import *

#################################
#
#   DAEMON du projet
#
######################################


print(lobjet["LED"].getallfunction())

lobjet["PIR"].saveJSON()
lobjet["PIR"].autoloadJSON()

lobjet["LED"].setparamvalue("Mode",lobjet["LED"].getallmode()[0])
lobjet["LED"].execfunction("Allumer")

print("test")
for objet in lobjet.values():
    objetname = objet.getname()
    print("********" + objetname + "**********")
    for param in lobjet[objetname].getallparam():
        print(lobjet[objetname].getparamvalue(param))
        print(lobjet[objetname].getparamJSONfilename(param))



#test des objets
#for objet in lobjet.values():
#    objet.loadJSON()
#    objet.run()
#    print(objet.getmode())
#    objet.setmode(2)
#    print(objet.getmode())
#    objet.saveJSON()




