import warnings
import json
import RPi.GPIO as GPIO
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

GPIO.setmode(GPIO.BOARD)

pins = 8, 10
GPIO.setup(pins, GPIO.OUT)

# load config from a JSON file (or anything outputting a python dictionary)
with open("database.cnf") as f:
    config = json.load(f)

if __name__ == '__main__':

	# create a Dejavu instance
	djv = Dejavu(config)

	# Fingerprint all the mp3's in the directory we give it
	djv.fingerprint_directory("mp3", [".mp3"])
        
	# Recognize audio from a file
	# song = djv.recognize(FileRecognizer, "mp3/SampleAudio_0.4mb.mp3")
	# print "From file we recognized: %s\n" % song

	# Or recognize audio from your microphone for `secs` seconds
	GPIO.output(pins, GPIO.HIGH)
	secs = 5
	song = djv.recognize(MicrophoneRecognizer, seconds=secs)
	
	if song is None:
		print "Nothing recognized -- did you play the song out loud so your mic could hear it? :)"
		GPIO.output(pins, GPIO.LOW)
	else:
		print "From mic with %d seconds we recognized: %s\n" % (secs, song)
		GPIO.output(pins, GPIO.LOW)
        GPIO.cleanup()

	# Or use a recognizer without the shortcut, in anyway you would like
	# recognizer = FileRecognizer(djv)
	# song = recognizer.recognize_file("mp3/SampleAudio_0.4mb.mp3")
	# print "No shortcut, we recognized: %s\n" % song