from Configuration.configuration import configuration

config = configuration()


#methode globale

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