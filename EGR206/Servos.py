import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)


kit.servo[1].set_pulse_width_range(1100, 1800)
kit.servo[1].actuation_range = 180
while True:
    kit.servo[1].angle = 180
    time.sleep(0.5)
    kit.servo[1].angle = 0
    time.sleep(0.5)


