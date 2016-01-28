
import threading,time

class Allumer(threading.Thread):

    def __init__(self, object):
        threading.Thread.__init__(self)
        self.object = object
        self.attribut = ["Time"]
        self._stop = threading.Event()
        self.starttime = time.time()


    def run(self):
        self.object.setparamvalue("Mode", "ALLUMER")
        while not self._stop.isSet():
            if (time.time() - self.starttime)  > self.object.getparamvalue("Time"):
                break
        self.object.setparamvalue("Mode", "ETEINTE")




    def stop(self):
        self._stop.set()

    def getAttribut(self):
        return self.attribut