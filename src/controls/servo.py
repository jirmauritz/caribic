import RPi.GPIO as GPIO
from time import sleep


servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
servo = GPIO.PWM(servoPIN, 50)
servo.start(5.75)


def steer(direction):
    # map < -100, 100 > into < 3, 8.5 > with 6 as center
    pwm = (direction / 36.4) + 5.75
    servo.start(pwm)
