
import threading,time

class Allumer(threading.Thread):

    def __init__(self, object):
        threading.Thread.__init__(self)
        self.object = object
        self.attribut = ["Time"]


    def run(self):
        self.object.setparamvalue("Mode", "ALLUMER")
        time.sleep(self.object.getparamvalue("Time"))
        self.object.setparamvalue("Mode", "ETEINTE")

        #if self.object.getparamvalue("Mode") == "ETEINTE":
        #    self.object.setparamvalue("Mode", "ALLUMER")


    def getAttribut(self):
        return self.attribut