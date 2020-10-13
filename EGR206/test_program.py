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
    
    print("Touch sensor demo!")
    
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
 
    print("Buzzer Drive demo!")

    crickit.drive_1.frequency = 1000

    crickit.drive_1.fraction = 1.0  # all the way on
    time.sleep(0.5)
    crickit.drive_1.fraction = 0.0  # all the way off
    time.sleep(0.5)
    crickit.drive_1.fraction = 0.5  # half on/off
    time.sleep(0.5)

    print("Reading Analog sensor !")
    print((ss.analog_read(pot),))
    time.sleep(0.25)

