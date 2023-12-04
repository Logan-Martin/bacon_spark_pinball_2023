# type: ignore

import board
import digitalio
import time
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

function testFun() {
   print("LED should be on!")
}


time.sleep(2)
testFun()

led.value = True
time.sleep(2)
led.value = False



