from daemon.Module.Abstract.Hardware import Hardware
from daemon.Configuration.Modele import *
from importlib.machinery import SourceFileLoader


class PIR(Hardware):





    def __init__(self):
        super().__init__()

        temp = getattr(SourceFileLoader("driver_PIR",Moduledirectory + self.getname() + "/Driver/driver_PIR.py").load_module(), "driver_PIR")
        self.driver = temp()




    #####################
    #
    # RUN
    #
    ########################

    def run(self):
        super().run()
        #print(self.getparamvalue("Detect"))
        if self.driver.get():
            self.setparamvalue("Detect","SOMETHING")
        else:
            self.setparamvalue("Detect","NOTHING")



