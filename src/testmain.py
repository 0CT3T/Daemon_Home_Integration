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


#TEST DES FUNCTION AVEC PARAMETRE
print(lobjet["LED"].getattributfunction("Allumer"))
lobjet["LED"].setfunction("Allumer",{"Time":10})
lobjet["LED"].setfunction("Allumer",{"Time":200})


#GESTION DE LA ROUTE
lobjet["LED"].addobjet(lobjet["PIR"])
#lobjet["LED"].removeobjet('PIR')




for objet in lobjet.values():
    objetname = objet.getname()
    print("********" + objetname + "**********")
    print(objet.getallobjet())
    print(objet.getallrules())
    print("-------------------")
    for param in lobjet[objetname].getallparam():
        print(param)
        print(lobjet[objetname].getparamvalue(param))
        print(lobjet[objetname].getparamJSONfilename(param))
    print("--------------------")
    for rule in lobjet[objetname].getallrules():
        print(rule)
        print(lobjet[objetname].isSetRule(rule))




#test des objets
#for objet in lobjet.values():
#    objet.loadJSON()
#    objet.run()
#    print(objet.getmode())
#    objet.setmode(2)
#    print(objet.getmode())
#    objet.saveJSON()




