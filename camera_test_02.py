import time
import picamera
with picamera.PiCamera() as camera:
	camera.resolution = (640, 480)
	camera.start_preview()
	print("running")
	camera.image_effect = 'film'
	time.sleep(2)
	camera.capture('Pictures/film.jpg')
	camera.resolution = (640, 480)
	camera.start_preview()
	print("cartoon")
	camera.image_effect = 'cartoon'
	time.sleep(2)
	camera.capture('Pictures/cartoon.jpg')
	camera.resolution = (640, 480)
	camera.start_preview()
	print("watercolor")
	camera.image_effect = 'watercolor'
	time.sleep(2)
	camera.capture('Pictures/watercolor.jpg')
	camera.resolution = (640, 480)
	camera.start_preview()
	print("blur")
	camera.image_effect = 'blur'
	time.sleep(2)
	camera.capture('Pictures/blur.jpg')
	camera.resolution = (640, 480)
	camera.start_preview()
	print("colorswap picture")
	camera.image_effect = 'colorswap'
	time.sleep(2)
	camera.capture('Pictures/colorswap.jpg')
	camera.resolution = (640, 480)
	camera.start_preview()
	print("negative")
	camera.image_effect = 'negative'
	time.sleep(2)
	camera.capture('Pictures/negative.jpg')
	print("done")
