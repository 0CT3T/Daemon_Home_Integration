import RPi.GPIO as GPIO


class driver_LED():

    def __init__(self):

        pwmPin = 12 # pin 18 pwm


        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pwmPin, GPIO.OUT)
        self.pwm = GPIO.PWM(pwmPin, 100)



    def allumer(self,opacite):
        self.pwm.ChangeFrequency(100)
        self.pwm.start(opacite)
    
    def stop(self):
        self.pwm.stop()

    def blink(self,frequency,opacity):
        self.pwm.ChangeFrequency(frequency)
        self.pwm.start(opacity)

