from daemon.Module.Abstract.Attribut import Attribut


class Time(Attribut):

    def __init__(self, objectname):
        self.objectname = objectname
        super().__init__()