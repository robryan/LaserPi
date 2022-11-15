"""
Rob Ryan

testing pre-built Adafruit servo gimbals
"""

import numpy as np
from gpiozero import Servo
from time import sleep


print("hello world, let's try to move a servo")

vertical_yaw = Servo(14)    # GPIO port #8 controls vertical axis
lateral_pitch = Servo(15)   # GPIO port #10 controls lateral axis

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
            for x in np.arange(-1, 1, 0.01):
                print("x is currently ... ", x)
                vertical_yaw.value = x
                sleep(0.01)
            sleep(interval_seconds)

    except KeyboardInterrupt:
        print("Program stopped")

    exit


# min_med_max(0.75, 4)   # 4 cycles, each every 0.75s

draw_box(2, 4)   # 4 boxes, rest 0.75s between