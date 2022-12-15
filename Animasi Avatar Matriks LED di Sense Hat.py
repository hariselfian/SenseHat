from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

Y = (255, 255, 39)
R = (255, 0, 0)
W = (255,255,255)
B = (0,0,0)
O = (255, 163, 0)

avatar_smile = [
    B, B, Y, Y, Y, O, B, B,
    B, Y, Y, Y, Y, Y, O, B,
    Y, Y, B, Y, Y, B, Y, O,
    Y, Y, B, Y, Y, B, Y, O,
    Y, Y, Y, Y, Y, Y, Y, O,
    Y, B, W, W, W, W, B, O,
    B, Y, B, B, B, B, O, B,
    B, B, Y, Y, Y, O, B, B,
    ]

avatar_left = [
    B, B, Y, Y, Y, O, B, B,
    B, Y, Y, Y, Y, Y, O, B,
    Y, R, Y, Y, R, Y, O, O,
    Y, R, Y, Y, R, Y, O, O,
    Y, Y, Y, Y, Y, Y, O, O,
    Y, Y, W, W, W, R, O, O,
    B, Y, R, R, R, O, O, B,
    B, B, Y, Y, Y, O, B, B,
    ]

avatar_right = [
    B, B, O, Y, Y, Y, B, B,
    B, O, Y, Y, Y, Y, Y, B,
    O, O, Y, R, Y, Y, R, Y,
    O, O, Y, R, Y, Y, R, Y,
    O, O, Y, Y, Y, Y, Y, Y,
    O, O, R, W, W, W, Y, Y,
    B, O, O, B, B, B, Y, B,
    B, B, O, Y, Y, Y, B, B,
    ]

avatar_top = [
    B, B, Y, Y, Y, O, B, B,
    B, Y, B, Y, Y, B, O, B,
    Y, Y, B, Y, Y, B, Y, O,
    Y, Y, Y, Y, Y, Y, Y, O,
    Y, B, W, W, W, W, B, O,
    Y, Y, B, B, B, B, Y, O,
    B, Y, Y, Y, Y, Y, O, B,
    B, B, Y, Y, Y, O, B, B,
    ]

avatar_bottom = [
    B, B, Y, Y, Y, O, B, B,
    B, Y, Y, Y, Y, Y, O, B,
    Y, Y, Y, Y, Y, Y, Y, O,
    Y, Y, B, Y, Y, B, Y, O,
    Y, Y, B, Y, Y, B, Y, O,
    Y, Y, Y, Y, Y, Y, Y, O,
    B, Y, B, W, W, B, Y, B,
    B, B, Y, Y, Y, Y, B, B,
    ]

def walking():
  for i in range(3):  
    sense.set_pixels(avatar_smile)
    sleep(1)
    sense.set_pixels(avatar_left)
    sleep(1)
    sense.set_pixels(avatar_right)
    sleep(1)
    sense.set_pixels(avatar_top)
    sleep(1)
    sense.set_pixels(avatar_bottom)
    sleep(1)
while True:
    walking()
#code by Haris Elfian