from daemon.Module.Abstract.Hardware import Hardware
from daemon.Configuration.Modele import *
from importlib.machinery import SourceFileLoader


class LED(Hardware):





    def __init__(self):
        super().__init__()

        temp = getattr(SourceFileLoader("driver_LED",Moduledirectory + self.getname() + "/Driver/driver_LED.py").load_module(), "driver_LED")
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
            self.driver.allumer(self.getparamvalue("Opacity"))
        if self.getparamvalue("Mode") == "ETEINTE":
            self.driver.stop()
        if self.getparamvalue("Mode") == "BLINKER":
            self.driver.blink(self.getparamvalue("Frequency"),self.getparamvalue("Opacity"))



