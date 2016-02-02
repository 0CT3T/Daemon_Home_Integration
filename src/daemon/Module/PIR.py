from daemon.Module.Abstract.Hardware import Hardware

from importlib.machinery import SourceFileLoader


class PIR(Hardware):





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
        if self.driver.get():
            self.setparamvalue("Detect","SOMETHING")
        else
            self.setparamvalue("Detect","NOTHING")



