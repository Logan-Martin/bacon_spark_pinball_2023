# type: ignore

import board
import digitalio
import time
import pwmio
from adafruit_motor import servo

button_left = digitalio.DigitalInOut(board.GP13)  # Button stuff
button_left.direction = digitalio.Direction.INPUT
button_left.pull = digitalio.Pull.UP
debounce_ButtonLeft = False

button_right = digitalio.DigitalInOut(board.GP16)  # Button stuff
button_right.direction = digitalio.Direction.INPUT
button_right.pull = digitalio.Pull.UP
debounce_ButtonRight = False

pwm_servo_left = pwmio.PWMOut(board.GP1, duty_cycle=2 ** 15, frequency=50)
servo_left = servo.Servo(pwm_servo_left, min_pulse=1000, max_pulse=2000)

pwm_servo_right = pwmio.PWMOut(board.GP15, duty_cycle=2 ** 15, frequency=50)
servo_right = servo.Servo(pwm_servo_right, min_pulse=1000, max_pulse=2000)

servo_left.angle = 0
servo_right.angle = 0

while True:

    if button_left.value == False:
        if debounce_ButtonLeft == False:
            debounce_ButtonLeft = True
            servo_left.angle = 180

    elif button_left.value == True:
        if debounce_ButtonLeft == True:
            debounce_ButtonLeft = False
            servo_left.angle = 0


    
    if button_right.value == False:
        if debounce_ButtonRight == False:
            debounce_ButtonRight = True
            servo_right.angle = 180

    elif button_right.value == True:
        if debounce_ButtonRight == True:
            debounce_ButtonRight = False
            servo_right.angle = 0

    time.sleep(0.1)
