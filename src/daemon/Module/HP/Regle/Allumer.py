
from daemon.Module.Abstract.Rules import Rules

class Allumer(Rules):

    def __init__(self, object):
        self.object = object
        super().__init__()


    def test(self):
        if self.object.getparamvalue("Mode") == "ALLUMER":
            self.object.getobjet("LED").setparamvalue("Mode", "BLINKER")