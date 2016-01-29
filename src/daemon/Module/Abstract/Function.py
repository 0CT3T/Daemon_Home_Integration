import threading

class Function(threading.Thread):

    def __init__(self):
        if self.__class__ is Function:
            raise Exception("ERREUR 01 : Function is abstract")
        else:
            threading.Thread.__init__(self)
            self.stopthread = threading.Event()

    def run(self):
        self.setup()
        while not self.stopthread.isSet():
            self.loop()
        self.finish()

    def stop(self):
        self.stopthread.set()

    def getAttribut(self):
        return self.attribut