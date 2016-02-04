import RPi.GPIO as io


class driver_PIR():

    def __init__(self):

        self.pir_pin = 18 # pin 23
        io.setmode(io.BCM)
        io.setup(self.pir_pin, io.IN)         # activate input



    def get(self):
        #print (io.input(self.pir_pin))
        if io.input(self.pir_pin):
            return True
        else:
            return False

