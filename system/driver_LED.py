import RPi.GPIO as GPIO
import time
import threading

pwmPin = 18 # pin 18 pwm


GPIO.setmode(GPIO.BCM)
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 100)

def function():
	while 1:
		pass	


def allumer(opacite):
    pwm.ChangeFrequency(100)
    pwm.start(opacite)
    
def stop():
    pwm.stop()

def blink(frequency,opacity):
    pwm.ChangeFrequency(frequency)
    pwm.start(opacity)

t1 = threading.Thread(target=function)
t1.start()
#t1.join()
    

    


#GPIO.cleanup()
#ALLUMER LA LED
#GPIO.OUTPUT(pwmPin, GPIO.HIGH)

#ETEINDRE LA LED
#GPIO.OUTPUT(pwmPin, GPIO.LOW)

#BLINKER LA LED
#GPIO.OUTPUT(pwmPin, GPIO.HIGH)
#time.sleep(1)
#GPIO.OUTPUT(pwmPin, GPIO.LOW)
#time.sleep(1)





