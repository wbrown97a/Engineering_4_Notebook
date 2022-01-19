import time
import picamera
with picamera.PiCamera() as camera:
	camera.resolution = (640, 480)
	camera.start_preview()
	print("running")
	time.sleep(2)
	camera.capture('Pictures/camera_test.jpg')
	print("done")
