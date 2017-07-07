try:
    import RPi.GPIO as GPIO
    import time as time
except RuntimeError:
    print("Error importing RPi.GPIO!")

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.OUT)
for i in range(0, 50):
	GPIO.output(16, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(16, GPIO.LOW)
	time.sleep(1)
GPIO.cleanup()
