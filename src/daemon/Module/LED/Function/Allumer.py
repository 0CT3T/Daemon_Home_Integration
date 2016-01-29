
from daemon.Module.Abstract.Function import Function
import time

class Allumer(Function):

    def __init__(self, object):
        super().__init__()
        self.object = object
        self.attribut = ["Time"]
        self.starttime = time.time()

    def setup(self):
        self.object.setparamvalue("Mode", "ALLUMER")

    def loop(self):
        if (time.time() - self.starttime)  > self.object.getparamvalue("Time"):
                self.stop()

    def finish(self):
        self.object.setparamvalue("Mode", "ETEINTE")



