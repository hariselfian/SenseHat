from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

lightblue = (192, 222, 255)

new_sense = SenseHat()
sense = SenseHat()

temp = sense.get_temperature()
temp = (int(temp))

pressure = sense.get_pressure()
pressure = (int(pressure))

humidity = sense.get_humidity()
humidity = (int(humidity))

def left():
  print ("Suhu: %s °C" %temp)
  new_sense.show_message("Suhu: %s °C" % temp, text_colour=lightblue, scroll_speed=0.07)
  sense.clear()

def up():
  print ("Tekanan: %s Pa" %pressure)
  new_sense.show_message("Tekanan: %s Pa" % pressure, text_colour=lightblue, scroll_speed=0.07)
  sense.clear()
  
def right():
  print ("Kelembatan: %s %" %humidity)
  new_sense.show_message("Kelembatan: %s %" % humidity, text_colour=lightblue, scroll_speed=0.07)
  sense.clear()
  
sense.stick.direction_left = left
sense.stick.direction_up = up
sense.stick.direction_right = right

while True:
  pass

#Code By Haris Elfian