import RPi.GPIO as GPIO
import time
import threading

class driver_LED():

    def __init__(self):

        pwmPin = 18 # pin 18 pwm


        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pwmPin, GPIO.OUT)
        self.pwm = GPIO.PWM(pwmPin, 100)

        #t1 = threading.Thread(target=self.function)
        #t1.start()


    def function():
        while 1:
            pass


    def allumer(opacite):
        self.pwm.ChangeFrequency(100)
        self.pwm.start(opacite)
    
    def stop():
        self.pwm.stop()

    def blink(frequency,opacity):
        self.pwm.ChangeFrequency(frequency)
        self.pwm.start(opacity)

