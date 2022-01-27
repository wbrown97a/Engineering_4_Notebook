import time
from picamera import PiCamera
from gpiozero import Button

button = Button(20)
camera = PiCamera()
camera.start_preview()
frame = 1

while True:
	try:
	   button.wait_for_press()
	   camera.capture('Pictures/animation/frames%03d.jpg' % frame)
	   frame += 1
	except KeyboardInterrupt:
	   camera.stop_preview()
	   break
