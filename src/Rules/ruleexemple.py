
from Configuration.Modele import *

def test():
    if lobjet["LED"].getmode() == 0:
        lobjet["LED"].setmode(1)
        print('test')

