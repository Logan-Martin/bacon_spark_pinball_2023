# type: ignore

import board
import digitalio
import time
import pwmio
from adafruit_motor import servo

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT\

pwm_servo = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

def testFun():
   print("LED should be on!")
   servo1.angle = 0


time.sleep(1)

while True:
   led.value = True
   testFun()
   time.sleep(1)
   led.value = False
   servo1.angle = 90
   time.sleep(1)




