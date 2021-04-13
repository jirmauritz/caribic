import FaBo9Axis_MPU9250
import time
import sys
from math import atan2, pi, sqrt

LSB = 0.48828125
R2D = 180.0 / pi

minx = 100
maxx = -100


# hx = 0 - 90
# hy = -16 - 43
# hz = -107 - -35

while True:
    try:
        mpu9250 = FaBo9Axis_MPU9250.MPU9250()
        accel = mpu9250.readAccel()
        mag = mpu9250.readMagnet()
        D = None
        hx = mag['x'] - 45
        hy = mag['y'] - 29.5
        hz = mag['z'] + 71
 #       h = sqrt(hx * hx + hy * hy + hz * hz)
 #       hx /= h
 #       hy /= h
 #       hz /= h
        yaw_rad = atan2(hy, hx)
        heading_rad = yaw_rad *R2D
        D = heading_rad % 360
        print(D)
        time.sleep(0.2)
    except OSError:
        print('Error')
        time.sleep(0.5)
        pass

