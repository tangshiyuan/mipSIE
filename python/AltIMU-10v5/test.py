#!/usr/bin/python

from datetime import datetime
from time import sleep

from lsm6ds33 import LSM6DS33
from lis3mdl import LIS3MDL
from lps25h import LPS25H

imu = LSM6DS33()
imu.enableLSM()

magnet = LIS3MDL()
magnet.enableLIS()

baro = LPS25H()
baro.enableLPS()

start = datetime.now()

while True:
    stop = datetime.now() - start
    start = datetime.now()
    deltaT = stop.microseconds/1000000.0
    print " "
    print "Interval(s):", deltaT
    print "Gyro:", imu.getGyroscopeRaw()
    print "Accelerometer:", imu.getAccelerometerRaw()
    print "Magnet:", magnet.getMagnetometerRaw()
    print "hPa:", baro.getBarometerMillibars()
    print "Altitude:", baro.getAltitude()
    #sleep(0.2)
    print "Gyro Temperature:", imu.getLSMTemperatureCelsius()
    print "Magnet Temperature:", magnet.getLISTemperatureCelsius()
    print "Baro Temperature:", baro.getLPSTemperatureCelsius()
    #sleep(0.1)
    sleep(1)
