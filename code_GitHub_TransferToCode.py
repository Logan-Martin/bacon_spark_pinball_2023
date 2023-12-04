# type: ignore

import board
import digitalio
import time
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

def testFun():
   print("LED should be on!")

time.sleep(1)

while True:
   led.value = True
   testFun()
   time.sleep(1)
   led.value = False
   time.sleep(1)




