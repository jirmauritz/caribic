import time
import pigpio

escPIN = 27
max_value = 1900
min_value = 1100

pi = pigpio.pi()

# calibrate
pi.set_servo_pulsewidth(escPIN, max_value)
time.sleep(1)
pi.set_servo_pulsewidth(escPIN, min_value)
time.sleep(1)
pi.set_servo_pulsewidth(escPIN, (max_value - min_value)/2 + min_value)


def speed(rate):
    # 1100 - 1900
    pwm = (rate * 4) + 1500
    pi.set_servo_pulsewidth(escPIN, pwm)
