from daemon.Module.Abstract.Attribut import Attribut


class Frequency(Attribut):

    def __init__(self, objectname):
        self.objectname = objectname
        super().__init__()


