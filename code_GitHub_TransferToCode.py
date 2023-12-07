# type: ignore

import board
import digitalio
import time
import pwmio
from adafruit_motor import servo

button_left = digitalio.DigitalInOut(board.GP4)
button_left.direction = digitalio.Direction.OUTPUT
debounce_ButtonLeft = False

button_right = digitalio.DigitalInOut(board.GP15)
button_right.direction = digitalio.Direction.OUTPUT
debounce_ButtonRight = False

pwm_servo_left = pwmio.PWMOut(board.GP11, duty_cycle=2 ** 15, frequency=50)
servo_left = servo.Servo(pwm_servo_left, min_pulse=500, max_pulse=2500)

pwm_servo_right = pwmio.PWMOut(board.GP7, duty_cycle=2 ** 15, frequency=50)
servo_right = servo.Servo(pwm_servo_right, min_pulse=500, max_pulse=2500)


time.sleep(1)

while True:

   if button_left.value == True:

      if debounce_ButtonLeft == False:
         debounce_ButtonLeft = True
         print("True, left!")
         servo_left.angle = 90

   else:

      if debounce_ButtonLeft == True:
         debounce_ButtonLeft = False
         print("False, left!")
         servo_left.angle = 0



   if button_right.value == True:

      if debounce_ButtonRight == False:
         debounce_ButtonRight = True
         print("True, right!")
         servo_right.angle = 90

   else:

      if debounce_ButtonRight == True:
         debounce_ButtonRight = False
         print("False, right!")
         servo_right.angle = 0


      

