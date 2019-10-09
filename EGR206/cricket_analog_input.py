import time
from adafruit_crickit import crickit
 
# For signal control, we'll chat directly with seesaw, use 'ss' to shorted typing!
ss = crickit.seesaw
# potentiometer connected to signal #3
pot = crickit.SIGNAL3
 
while True:
    print((ss.analog_read(pot),))
    time.sleep(0.25)
