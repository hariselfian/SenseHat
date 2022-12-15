from sense_hat import SenseHat

sense = SenseHat()

sense.clear()

r = (255,0,0)
g = (0, 255, 0)
b = (0, 0,255)
w = (255,255,255)

o = (0,0,0)

Kiri = [
  o,o,o,o,o,o,o,o,
  o,o,r,o,o,o,o,o,
  o,r,r,o,o,o,o,o,
  r,r,r,r,r,r,r,r,
  r,r,r,r,r,r,r,r,
  o,r,r,o,o,o,o,o,
  o,o,r,o,o,o,o,o,
  o,o,o,o,o,o,o,o
  ]
  
Kanan = [
  o,o,o,o,o,o,o,o,
  o,o,o,o,o,g,o,o,
  o,o,o,o,o,g,g,o,
  g,g,g,g,g,g,g,g,
  g,g,g,g,g,g,g,g,
  o,o,o,o,o,g,g,o,
  o,o,o,o,o,g,o,o,
  o,o,o,o,o,o,o,o
  ]

Atas = [
  o,o,o,b,b,o,o,o,
  o,o,b,b,b,b,o,o,
  o,b,b,b,b,b,b,o,
  o,o,o,b,b,o,o,o,
  o,o,o,b,b,o,o,o,
  o,o,o,b,b,o,o,o,
  o,o,o,b,b,o,o,o,
  o,o,o,b,b,o,o,o
  ]
  
Bawah = [
  o,o,o,w,w,o,o,o,
  o,o,o,w,w,o,o,o,
  o,o,o,w,w,o,o,o,
  o,o,o,w,w,o,o,o,
  o,o,o,w,w,o,o,o,
  o,w,w,w,w,w,w,o,
  o,o,w,w,w,w,o,o,
  o,o,o,w,w,o,o,o
  ]


def left():
  sense.set_pixels(Kiri)

def right():
  sense.set_pixels(Kanan)

def up():
  sense.set_pixels(Atas)

def down():
  sense.set_pixels(Bawah)
  
sense.stick.direction_left = left
sense.stick.direction_right = right
sense.stick.direction_up = up
sense.stick.direction_down = down

while True:
  pass
#Code By Haris Elfian