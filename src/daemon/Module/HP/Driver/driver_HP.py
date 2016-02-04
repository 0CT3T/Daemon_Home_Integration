
import os

class driver_HP():

    def __init__(self):
        os.system('./daemon/Module/HP/Driver/testcode &')
        with open('test','w') as fichier:
            fichier.write('2')

    def alarme(self):
        with open('test','w') as fichier:
            fichier.write('1')

    def stop(self):
        with open('test','w') as fichier:
            fichier.write('2')

