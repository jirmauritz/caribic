import pigpio

servoPIN = 17

pi = pigpio.pi()
pi.set_servo_pulsewidth(servoPIN, 1200)


def steer(direction):
    # map < -100, 100 > into < 600, 1800 > with 1200 as center
    pwm = (6 * direction) + 1200
    pi.set_servo_pulsewidth(servoPIN, pwm)
