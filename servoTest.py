"""
Rob Ryan

testing pre-built Adafruit servo gimbals
"""

from gpiozero import Servo
from time import sleep

print("hello world, let's try to move a servo")

servo_1 = Servo(8)     # Servo 1 connected to GPIO port #8
servo_2 = Servo(10)    # Servo 2 connected to GPIO port #10

try:
    while True:
        servo_1.min()
        servo_2.min()
        sleep(0.5)
        servo_1.mid()
        servo_2.mid()
        sleep(0.5)
        servo_1.max()
        servo_2.max()
        sleep(0.5)
except KeyboardInterrupt:
	print("Program stopped")