# Example code for (GY-521) MPU6050 Accelerometer/Gyro Module
# Write in MicroPython by Warayut Poomiwatracanont JAN 2023

from MPU6050 import MPU6050
import time
from machine import Pin
from time import sleep_ms


VCC = Pin(13, Pin.OUT)
GND = Pin(12, Pin.OUT)
VCC.value(1)
GND.value(0)
time.sleep(.2)


mpu = MPU6050()


while True:
        # Accelerometer Data
    accel = mpu.read_accel_data() # read the accelerometer [ms^-2]
    aX = accel["x"]
    aY = accel["y"]
    aZ = accel["z"]
    #print(aZ)
    print("x: " + str(aX) + " y: " + str(aY) + " z: " + str(aZ))
    
        # Gyroscope Data
    gyro = mpu.read_gyro_data()   # read the gyro [deg/s]
    gX = gyro["x"]
    gY = gyro["y"]
    gZ = gyro["z"]
   
#     print("x:" + str(gX) + " y:" + str(gY) + " z:" + str(gZ))

    
    sleep_ms(500)

