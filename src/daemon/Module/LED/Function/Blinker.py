
from daemon.Module.Abstract.Function import Function


class Blinker(Function):

    def __init__(self, object):
        super().__init__()
        self.object = object
        self.attribut = ["Frequency","Opacity"]

    def setup(self):
        self.object.setparamvalue("Mode", "BLINKER")

    def loop(self):
        pass

    def finish(self):
        pass



