from Module import Hardware


class LED(Hardware):

    def __init__(self):
        super().__init__()

    #run
    def run(self):
        print("LED")