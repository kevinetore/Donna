import time as time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pins = 8, 10
GPIO.setup(pins, GPIO.OUT)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
	input_state = GPIO.input(40)
	if input_state == False:
		GPIO.output(pins, GPIO.HIGH)
	GPIO.output(pins, GPIO.LOW)
GPIO.cleanup()


