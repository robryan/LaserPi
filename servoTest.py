"""
Rob Ryan

testing pre-built Adafruit servo gimbals
"""

from gpiozero import Servo
from time import sleep

print("hello world, let's try to move a servo")

servo_1 = Servo(14)    # Adafruit Servo 1 connected to GPIO port #8
servo_2 = Servo(15)    # Adafruit Servo 2 connected to GPIO port #10

"""
Flex the servos by rotating each to its minimum, midpoint, and max
"""
def min_med_max(interval_seconds, num_iterations):
    try:
        for iteration in range(0, 4):
            # this is first
            servo_1.min()
            sleep(interval_seconds)
            servo_2.min()
            sleep(interval_seconds)
            servo_1.mid()
            sleep(interval_seconds)
            servo_2.mid()
            sleep(interval_seconds)
            servo_1.max()
            sleep(interval_seconds)
            servo_2.max()
            sleep(interval_seconds)
    except KeyboardInterrupt:
        print("Program stopped")

    exit


min_med_max(0.75, 10)   # 10 cycles, each every 0.75s

