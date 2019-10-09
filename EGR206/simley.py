
from sense_hat import SenseHat 
sense = SenseHat() 
sense.clear() 
r = (255,0,0) 
g = (0, 255, 0) 
b = (0, 0,255) 
O = (0,0,0) 
X = (255,255,255) 
smileLeft = [ 
  O,X,X,X,X,X,X,O, 
  X,O,O,O,O,O,O,X, 
  X,O,X,O,X,O,O,X, 
  X,O,O,O,O,O,O,X, 
  X,X,O,O,O,X,O,X, 
  X,O,X,X,X,O,O,X, 
  X,O,O,O,O,O,O,X, 
  O,X,X,X,X,X,X,O 
  ] 
smileRight = [ 
  O,X,X,X,X,X,X,O, 
  X,O,O,O,O,O,O,X, 
  X,O,O,X,O,X,O,X, 
  X,O,O,O,O,O,O,X, 
  X,O,X,O,O,O,X,X,
  X,O,O,X,X,X,O,X, 
  X,O,O,O,O,O,O,X, 
  O,X,X,X,X,X,X,O 
  ] 

def left(): 
    sense.set_pixels(smileLeft) 

def right(): 
    sense.set_pixels(smileRight) 

def clear():
   sense.clear()

sense.stick.direction_left = left 
sense.stick.direction_right = right 

while True: 
   try: 
     pass
   except (KeyboardInterrupt,SystemExit):
    clear()
    raise
