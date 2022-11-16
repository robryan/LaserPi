"""
Rob Ryan

testing pre-built Adafruit servo gimbals
"""

from time import sleep

from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
import numpy as np
from tween import *



print("hello world, let's try to move a servo")

# smooth jitter with PigPIO
# https://gpiozero.readthedocs.io/en/stable/api_output.html#servo fo
pigpio_factory = PiGPIOFactory()

vertical_yaw = AngularServo(pin=14, min_angle=-90, max_angle=90, pin_factory=pigpio_factory)    # GPIO port #14 controls vertical axis
lateral_pitch = AngularServo(pin=15, min_angle=0, max_angle=90, pin_factory=pigpio_factory)   # GPIO port #15 controls lateral axis

"""
Flex the servos by rotating each to its minimum, midpoint, and max
"""
def min_med_max(interval_seconds, num_iterations):
    try:
        for iteration in range(0, num_iterations):
            vertical_yaw.min()
            sleep(interval_seconds)
            
            lateral_pitch.min()
            sleep(interval_seconds)
            
            lateral_pitch.mid()
            sleep(interval_seconds)
            
            lateral_pitch.max()
            sleep(interval_seconds)
            
            vertical_yaw.mid()
            sleep(interval_seconds)

            vertical_yaw.max()
            sleep(interval_seconds)

            lateral_pitch.mid()
            sleep(interval_seconds)

            lateral_pitch.min()
            sleep(interval_seconds)

            vertical_yaw.mid()
            sleep(interval_seconds)

            lateral_pitch.mid()
            sleep(interval_seconds)

    except KeyboardInterrupt:
        print("Program stopped")

    exit



"""
Flex the servos by drawing a rectagle on the wall
"""
def draw_box(interval_seconds, num_iterations):
    try:
        vertical_yaw.min()
        lateral_pitch.min()

        for iteration in range(0, num_iterations):
            # rotate left/right in tiny steps

            x_left = -90
            x_right = 90
            x_step = 0.1          # size in degrees of smallest servo motion
            x_sleep = 0.001     # pause between movements
            
            # pan left to right
            for x in np.arange(x_left, x_right, x_step):
                vertical_yaw.angle = x
                sleep(x_sleep)

            y_bottom = 0
            y_top = 90
            y_step = 0.1          # size in degrees of smallest servo motion
            y_sleep = 0.001     # pause between movements

            # tilt up/down
            for y in np.arange(y_bottom, y_top, y_step):
                lateral_pitch.angle = y
                sleep(y_step)

            # pause for a sec before going again    
            sleep(interval_seconds)

    except KeyboardInterrupt:
        print("Program stopped")

    exit


"""
Flex the servos by rotating each to its minimum, midpoint, and max
"""
def left_right_w_easing(interval_seconds, num_iterations):
    try:
        vertical_yaw.min()
        lateral_pitch.min()

        for iteration in range(0, num_iterations):
            # rotate left/right in ease function'd steps
            x_left = -90
            x_right = 90
            x_step = 0.1          # size in degrees of smallest servo motion
            x_sleep = 0.001     # pause between movements

            for x in cycleTween(easeInOutCubic, easeInOutCubic, x_left, x_right, 32, True):
                print(x)
                vertical_yaw.angle = x
                sleep(x_step)

            
            # # pan left to right
            # for x in np.arange(x_left, x_right, x_step):
            #     vertical_yaw.angle = x
            #     sleep(x_sleep)

            # y_bottom = 0
            # y_top = 90
            # y_step = 0.1          # size in degrees of smallest servo motion
            # y_sleep = 0.001     # pause between movements

            # # tilt up/down
            # for y in np.arange(y_bottom, y_top, y_step):
            #     lateral_pitch.angle = y
            #     sleep(y_step)

            # pause for a sec before going again    
            sleep(interval_seconds)

    except KeyboardInterrupt:
        print("Program stopped")

    exit



# min_med_max(0.75, 4)   # 4 cycles, each every 0.75s

# draw_box(2, 4)   # 4 boxes, rest between

left_right_w_easing(2, 4)  