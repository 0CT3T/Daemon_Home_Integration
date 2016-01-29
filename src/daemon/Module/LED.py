from daemon.Module.Hardware import Hardware

from importlib.machinery import SourceFileLoader


class LED(Hardware):





    def __init__(self):
        super().__init__()

        #temp = getattr(SourceFileLoader("driver_LED",Moduledirectory + self.getname() + "/Driver/driver_LED.py").load_module(), "driver_LED")
        #self.driver = temp()


    #####################
    #
    # RUN
    #
    ########################

    def run(self):



        print(self.getparamvalue("Mode"))
        #if self.getparamvalue("Mode") == "ALLUMER":
        #    self.driver.allumer(100)
        #if self.getparamvalue("Mode") == "ETEINTE":
        #    self.driver.stop()
        #if self.getparamvalue("Mode") == "BLINKER":
        #    self.driver.blink(20,20)



