from daemon.Module.Abstract.Hardware import Hardware
from daemon.Configuration.Modele import *
from importlib.machinery import SourceFileLoader


class HP(Hardware):





    def __init__(self):
        super().__init__()

        temp = getattr(SourceFileLoader("driver_HP",Moduledirectory + self.getname() + "/Driver/driver_HP.py").load_module(), "driver_HP")
        self.driver = temp()


    #####################
    #
    # RUN
    #
    ########################

    def run(self):
        super().run()


        #print(self.getparamvalue("Mode"))
        if self.getparamvalue("Mode") == "ALLUMER":
            self.driver.alarme()
        if self.getparamvalue("Mode") == "ETEINTE":
            self.driver.stop()



