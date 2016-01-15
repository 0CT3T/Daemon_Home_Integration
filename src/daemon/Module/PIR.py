from daemon.Module.Hardware import Hardware


class PIR(Hardware):

    def __init__(self):
        super().__init__()

    #run
    def run(self):
        print("PIR")