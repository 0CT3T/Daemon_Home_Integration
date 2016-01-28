from daemon.initialisation import *

#################################
#
#   DAEMON du projet
#
######################################


try:
    while True:


        #tester tous les objets
        for objet in lobjet.values():
            try:
                objet.autoloadJSON()
            except FileNotFoundError:
                pass
            except ValueError:
                pass
            objet.run()

except KeyboardInterrupt:
    pass


