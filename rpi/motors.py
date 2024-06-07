import pigpio
import RPi.GPIO as GPIO
from ser_read import Read
import math
from time import sleep



def NumCheck(num):
    if float(nums[num]) < 500:
        return 500
    elif float(nums[num]) > 2500:
        return 2500
    else:
        result = math.ceil(nums[num] / 100) * 100
        return result


m1 = 23
m2 = 25
pwm = pigpio.pi() 
pwm2 = pigpio.pi() 
pwm.set_mode(m1, pigpio.OUTPUT)
pwm2.set_mode(m2, pigpio.OUTPUT)

pwm.set_PWM_frequency(m1, 50)
pwm.set_PWM_range(m1, 20000) # 1,000,000 / 50 = 20,000us for 100% duty cycle
pwm2.set_PWM_frequency(m2, 50)
pwm2.set_PWM_range(m2, 20000) # 1,000,000 / 50 = 20,000us for 100% duty cycle

sleep(5)

oldx = 0
oldy = 0
oldz = 0

while True:
    nums = Read()

    x = NumCheck(0)
    y = NumCheck(1)
    z = NumCheck(2)

    print(x, y, z)
    if x == oldx:
        continue
    else:
        pwm.set_servo_pulsewidth(m1, x)

    if y == oldy:
        continue
    else:
        pwm.set_servo_pulsewidth(m2, y)
    #sleep(0.5)
    oldx = x
    oldy = y
    oldz = z
