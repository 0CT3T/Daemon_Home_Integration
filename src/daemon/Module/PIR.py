from daemon.Module.Abstract.Hardware import Hardware

from importlib.machinery import SourceFileLoader


class PIR(Hardware):





    def __init__(self):
        super().__init__()




    #####################
    #
    # RUN
    #
    ########################

    def run(self):
        print(self.getparamvalue("Mode"))



