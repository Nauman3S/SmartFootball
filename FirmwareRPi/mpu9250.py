import os
import sys
import time
import smbus

from imusensor.MPU9250 import MPU9250

address = 0x68
bus = smbus.SMBus(1)
imu = MPU9250.MPU9250(bus, address)
imu.begin()

def getData():

    imu.readSensor()
    imu.computeOrientation()
    acc=[imu.AccelVals[0], imu.AccelVals[1], imu.AccelVals[2]]
    gyro=[imu.GyroVals[0], imu.GyroVals[1], imu.GyroVals[2]]
    mag=[imu.MagVals[0], imu.MagVals[1], imu.MagVals[2]]
    ypr=[imu.roll, imu.pitch, imu.yaw]
	
    return [acc,gyro,mag,ypr]