from daemon.Module.Abstract.Attribut import Attribut


class Opacity(Attribut):

    def __init__(self, objectname):
        self.objectname = objectname
        super().__init__()


