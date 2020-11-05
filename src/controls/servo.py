import RPi.GPIO as GPIO
from time import sleep

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
servo = GPIO.PWM(servoPIN, 50)

# Init to center
servo.start(7)

def steer(direction):
    # map < -100, 100 > into < 5, 9 >
    pwm = (direction / 50) + 7
    servo.start(pwm)
    sleep(0.5)
    servo.start(0)
