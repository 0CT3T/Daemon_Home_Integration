import json
from configuration import configuration

#JSON parser
def jdefault(o):
    if isinstance(o, set):
        return list(o)
    return o.__dict__

#import a Class
def my_import(name):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

################### PARSER JSON ############
#j = configuration()
#obj = json.dumps(j,default=jdefault,indent=4)
#with open("module.conf", "w") as fichier:
#    fichier.write(obj)

######### CHARGEMENT DU FICHIER ###
with open("module.conf", "r") as fichier:
    JSON = fichier.read()
config = configuration(JSON)




#variable
lmodule = []
lobjet = []

for item in config.getlitem():
    lmodule.append(my_import('Module.' + item))

#lmodule.append(my_import('Module.PIR'))
#lmodule.append(my_import('Module.LED'))

for module in lmodule:
    lobjet.append(module())

for objet in lobjet:
    objet.run()

