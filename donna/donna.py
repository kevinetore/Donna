import warnings
import json
import RPi.GPIO as GPIO
import time as time
import threading
from threading import Thread
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

GPIO.setmode(GPIO.BOARD)
pins = [3,5,8,15,16] # In correct order of GPIO on Raspberry Pi
second_pins = [7,11,13,10,12]

board_pins = zip(pins, second_pins)
print(board_pins)

GPIO.setup(pins+second_pins, GPIO.OUT)

# load config from a JSON file (or anything outputting a python dictionary)
with open("database.cnf") as f:
    config = json.load(f)
    
def piBoard():
    for pin in board_pins * 15:
        GPIO.output(
            pin[0], GPIO.HIGH
        )
        GPIO.output(
            pin[1], GPIO.HIGH
        )
        time.sleep(0.15)
        GPIO.output(
            pin[0], GPIO.LOW
        )
        GPIO.output(
            pin[1], GPIO.LOW
        )
        
def recognizeSong():
    # create a Dejavu instance
    djv = Dejavu(config)

    # Fingerprint mp3's in mp3 directory
    djv.fingerprint_directory("mp3", [".mp3"])
    secs = 5
    song = djv.recognize(MicrophoneRecognizer, seconds=secs)
    
    if song is None:
        print "Nothing recognized -- did you play the song out loud so your mic could hear it? :)"
    else:
	print "From mic with %d seconds we recognized: %s\n" % (secs, song)

if __name__ == '__main__':

    Thread(target = piBoard).start()
    Thread(target = recognizeSong).start()    