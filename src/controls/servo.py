import RPi.GPIO as GPIO
from time import sleep


servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
servo = GPIO.PWM(servoPIN, 50)
servo.start(4.2)


def steer(direction):
    # map < -100, 100 > into < 2.5, 5.9 >
    pwm = (direction / 58.8) + 4.2
    servo.start(pwm)
