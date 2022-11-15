"""
Rob Ryan

testing pre-built Adafruit servo gimbals
"""

from gpiozero import Servo
from time import sleep

print("hello world, let's try to move a servo")

servo_vertical_yaw = Servo(14)    # GPIO port #8 controls vertical axis
servo_lateral_pitch = Servo(15)   # GPIO port #10 controls lateral axis

"""
Flex the servos by rotating each to its minimum, midpoint, and max
"""
def min_med_max(interval_seconds, num_iterations):
    try:
        for iteration in range(0, num_iterations):
            servo_vertical_yaw.min()
            sleep(interval_seconds)
            
            servo_lateral_pitch.min()
            sleep(interval_seconds)
            
            servo_lateral_pitch.mid()
            sleep(interval_seconds)
            
            servo_lateral_pitch.max()
            sleep(interval_seconds)
            
            servo_vertical_yaw.mid()
            sleep(interval_seconds)

            servo_vertical_yaw.max()
            sleep(interval_seconds)

            servo_lateral_pitch.mid()
            sleep(interval_seconds)

            servo_lateral_pitch.min()
            sleep(interval_seconds)

            servo_vertical_yaw.mid()
            sleep(interval_seconds)

            servo_lateral_pitch.mid()
            sleep(interval_seconds)

    except KeyboardInterrupt:
        print("Program stopped")

    exit


min_med_max(0.75, 10)   # 10 cycles, each every 0.75s

