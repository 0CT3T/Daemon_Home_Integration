

class Allumer():

    def __init__(self, object):
        self.object = object

    def test(self):
        if self.object.getparamvalue("Mode") == "ETEINTE":
            self.object.setparamvalue("Mode", "ALLUMER")