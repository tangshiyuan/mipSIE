#!/usr/bin/python

from datetime import datetime
from time import sleep

from altimu import AltIMU

imu = AltIMU()
imu.enable()

imu.calibrateGyroAngles()

#for x in range(1000):
#    startTime = datetime.now()
#    angles = imu.trackGyroAngles(deltaT = 0.0002)

#print angles

start = datetime.now()

while True:
    stop = datetime.now() - start
    deltaT = stop.microseconds/1000000.0
    print " "
    print "Interval(s):", stop.total_seconds()
    #print "Interval(s):", deltaT
    print "Accel Angles:", imu.getAccelerometerAngles()
    #print "Gyro Angles:", imu.trackGyroAngles(deltaT = deltaT)
    #print "Rotation Rate: ", imu.getGyroRotationRates() # ok 
    #print "Complimentary:", imu.getComplementaryAngles(deltaT = deltaT) # fixed
    #print "Karman:", imu.getKalmanAngles(deltaT = deltaT) # kinda fixed...
    start = datetime.now()
    #sleep(0.02)
    sleep(1)
