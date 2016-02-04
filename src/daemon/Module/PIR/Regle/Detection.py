from daemon.Module.Abstract.Rules import Rules

class Detection(Rules):

    def __init__(self, object):
        self.object = object
        super().__init__()

    def test(self):
        if self.object.getparamvalue("Detect") == "SOMETHING":
            self.object.getobjet("LED").setparamvalue("Mode", "BLINKER")
            self.object.getobjet("HP").setparamvalue("Mode","ALLUMER")
        else:
            self.object.getobjet("LED").setparamvalue("Mode", "ETEINTE")
            self.object.getobjet("HP").setparamvalue("Mode", "ETEINTE")
