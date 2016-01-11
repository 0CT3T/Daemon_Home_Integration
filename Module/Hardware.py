#import section


class Hardware:

    #constructeur
    def __init__(self):
        if self.__class__ is Hardware:
            raise Exception("ERREUR 01 : Hardware is abstract")
        else:
            pass

    def run(self):
        pass