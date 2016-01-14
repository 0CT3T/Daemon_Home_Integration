
from Configuration.Modele import *

def test():
    if lobjet["LED"].getmode() == "ALLUMER":
        lobjet["LED"].setmode("ETEINTE")


