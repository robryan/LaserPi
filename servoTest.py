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
def min_med_max(interval_seconds):
    try:
        while True:
            servo_1.min()
            servo_2.min()
            sleep(interval_seconds)
            servo_1.mid()
            servo_2.mid()
            sleep(interval_seconds)
            servo_1.max()
            servo_2.max()
            sleep(interval_seconds)
    except KeyboardInterrupt:
        print("Program stopped")



min_med_max(0.25)