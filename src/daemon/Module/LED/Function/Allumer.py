from daemon.Module.LED import LED

class Allumer:

    def __init__(self, object):
        self.object = object


    def exe(self):
        if self.object.getparamvalue("Mode") == "ALLUMER":
            d.Allumer()
