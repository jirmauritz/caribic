import time   #importing time library to make Rpi wait because its too impatient
import pigpio

escPIN = 17  #Connect the ESC in this GPIO pin
max_value = 2000
min_value = 700

pi = pigpio.pi()
pi.set_servo_pulsewidth(escPIN, 0)


def speed(throttle):
    # 1100 - 1900
    pwm = (throttle * 4) + 1500
    pi.set_servo_pulsewidth(escPIN, pwm)


def calibrate():   #This is the auto calibration procedure of a normal escPIN
    pi.set_servo_pulsewidth(escPIN, 0)
    print("Disconnect the battery and press Enter")
    inp = input()
    if inp == '':
        pi.set_servo_pulsewidth(escPIN, max_value)
        print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = input()
        if inp == '':            
            pi.set_servo_pulsewidth(escPIN, min_value)
            print("Wierd eh! Special tone")
            time.sleep(7)
            print("Wait for it ....")
            time.sleep (5)
            print("Im working on it, DONT WORRY JUST WAIT.....")
            pi.set_servo_pulsewidth(escPIN, 0)
            time.sleep(2)
            print("Arming escPIN now...")
            pi.set_servo_pulsewidth(escPIN, min_value)
            time.sleep(1)
            print("See.... uhhhhh")

