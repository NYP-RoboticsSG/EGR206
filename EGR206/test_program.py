from sense_hat import SenseHat
import time
from random import randint
from time import sleep
from adafruit_crickit import crickit

sense = SenseHat()
ss = crickit.seesaw
# make a list of all the servos
servos = (crickit.servo_1, crickit.servo_2, crickit.servo_3, crickit.servo_4)
pot = crickit.SIGNAL3
sense.clear()
while True:
    
    x = randint(0, 7)
    y = randint(0, 7)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    
    sense.set_pixel(x, y, r, g, b)

    if crickit.touch_1.value:
        print("Touched Cap Touch Pad 1")
    if crickit.touch_2.value:
        print("Touched Cap Touch Pad 2")
    if crickit.touch_3.value:
        print("Touched Cap Touch Pad 3")
    if crickit.touch_4.value:
        print("Touched Cap Touch Pad 4")

    for my_servo in servos:
        # Do the wave!
        print("Moving servo #", servos.index(my_servo)+1)
        my_servo.angle = 0      # right
        time.sleep(0.25)
        my_servo.angle = 90     # middle
        time.sleep(0.25)
        my_servo.angle = 180    # left
        time.sleep(0.25)
        my_servo.angle = 90     # middle
        time.sleep(0.25)
        my_servo.angle = 0      # right

    print((ss.analog_read(pot),))
    time.sleep(0.25)
    
sleep(0.01)
