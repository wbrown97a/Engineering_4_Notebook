
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

lsm303 = Adafruit_LSM303.LSM303()
x = 0
RST = 24
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height

padding = 3
top = padding
bottom = height-padding

image = Image.new('1', (width, height))
font = ImageFont.load_default()
draw = ImageDraw.Draw(image)

while True:
  #clears the display to update the accelerators
  draw.rectangle((0,0,width,height), outline=0, fill=0)

  accel, mag = lsm303.read()
#prints the x, y, and z accelerators and makes them a short decimal
  accel_x, accel_y, accel_z = accel
  draw.text((x, top),    "x accel: " + (str(round(accel_x/107, 3))), fill=255)
  draw.text((x, top+20), "y accel: " + (str(round(accel_y/107, 3))), fill=255)
  draw.text((x, top+40), "z accel: "  + (str(round(accel_z/107, 3))), fill=255)

  disp.image(image)
  disp.display()
