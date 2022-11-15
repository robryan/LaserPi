"""
Rob Ryan

testing pre-built Adafruit servo gimbals
"""

import numpy as np
from gpiozero import AngularServo
from time import sleep


print("hello world, let's try to move a servo")

vertical_yaw = AngularServo(pin=14, min_angle=-90, max_angle=90)    # GPIO port #14 controls vertical axis
lateral_pitch = AngularServo(pin=15, min_angle=-75, max_angle=75)   # GPIO port #15 controls lateral axis

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
Flex the servos by rotating each to its minimum, midpoint, and max
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

            y_bottom = -75
            y_top = 75
            y_step = 0.1          # size in degrees of smallest servo motion
            y_sleep = 0.001     # pause between movements

            # tilt up/down
            for y in np.arange(y_bottom, y_top, y_step):
                lateral_pitch.angle = x
                sleep(y_sleep)

            # pause for a sec before going again    
            sleep(interval_seconds)

    except KeyboardInterrupt:
        print("Program stopped")

    exit


# min_med_max(0.75, 4)   # 4 cycles, each every 0.75s

draw_box(2, 4)   # 4 boxes, rest between