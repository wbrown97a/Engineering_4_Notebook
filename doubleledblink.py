import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
while True:
	GPIO.output(21,GPIO.HIGH)
	print("LED 1 is on")	
	time.sleep(1)
	GPIO.output(21,GPIO.LOW)
	print("LED 1 is off")
	print("LED 2 is on")
	GPIO.output(26,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(26,GPIO.LOW)
	print("LED 2 is off")
