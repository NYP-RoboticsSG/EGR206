import time
from adafruit_crickit import crickit
 
print("1 Servo demo!")
crickit.servo_1.min_pulse = 1190
crickit.servo_1.max_pulse = 2000

while True:
    print("Moving servo #1")
    crickit.servo_1.angle = 0      # right
    time.sleep(1)
    crickit.servo_1.angle = 90     # middle
    time.sleep(1)
    crickit.servo_1.angle = 180    # left
    time.sleep(1)
    crickit.servo_1.angle = 90     # middle
    time.sleep(1)
    # and repeat!
