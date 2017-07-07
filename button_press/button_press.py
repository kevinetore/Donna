import time as time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.OUT)

while True:
	input_state = GPIO.input(18)
	if input_state == False:
		GPIO.output(16, GPIO.HIGH)
	GPIO.output(16, GPIO.LOW)
GPIO.cleanup()
