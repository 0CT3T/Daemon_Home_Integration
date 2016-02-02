import RPi.GPIO as io


class driver_PIR():

    def __init__(self):

        pir_pin = 23 # pin 23

        io.setup(pir_pin, io.IN)         # activate input



    def get(self):
        return io.input(self.pir_pin)

