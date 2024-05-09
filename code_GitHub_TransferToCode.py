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

pwm_servo_left = pwmio.PWMOut(board.GP1, duty_cycle=2 ** 15, frequency=50)
servo_left = servo.ContinuousServo(pwm_servo_left, min_pulse=1000, max_pulse=2000)

servo_left.throttle = 0

while True:

    ##print(debounce_ButtonLeft)
    ##print(button_left.value)

    if button_left.value == False:
        if debounce_ButtonLeft == False:
            debounce_ButtonLeft = True
            print("turn a")
            servo_left.throttle = 0.5
            time.sleep(0.2)
            servo_left.throttle = 0

    elif button_left.value == True:
        if debounce_ButtonLeft == True:
            debounce_ButtonLeft = False
            servo_left.throttle = -0.5
            time.sleep(0.2)
            servo_left.throttle = 0

    time.sleep(0.1)
