import time   #importing time library to make Rpi wait because its too impatient
import RPi.GPIO as GPIO

escPIN = 17  #Connect the ESC in this GPIO pin
max_value = 2000
mid_value = 1500
min_value = 700

GPIO.setmode(GPIO.BCM)
GPIO.setup(escPIN, GPIO.OUT)
esc_pwm = GPIO.PWM(escPIN, 0)


def speed(throttle):
    # 1100 - 1900
    pwm = (throttle * 4) + 1500
    esc_pwm.start(pwm)

def calibrate():   #This is the auto calibration procedure of a normal ESC
    print("Disconnect the battery and press Enter")
    inp = input()
    if inp == '':
        esc_pwm.start(max_value)
        print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = input()
        if inp == '':            
            esc_pwm.start(min_value)
            print("Wierd eh! Special tone")
            time.sleep(7)
            print("Wait for it ....")
            time.sleep (5)
            print("Im working on it, DONT WORRY JUST WAIT.....")
            esc_pwm.start(0)
            time.sleep(2)
            print("Arming ESC now...")
            esc_pwm.start(min_value)
            time.sleep(1)
            print("See.... uhhhhh")

