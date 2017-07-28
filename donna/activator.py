#import speech_recognition as sr
import RPi.GPIO as GPIO
import time
import start as start

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(40)
    if input_state == False:
        print('Button pressed')
        start.youtube_search(args)
        time.sleep(0.2)
# met gsr bedoel ik Google Speech Recognition
#gsr = sr.Recognizer()
#with sr.Microphone() as source:
#    print("speak now, or be silence forever")
#    while True:
#        audio = gsr.listen(source)

#gsr.recognize_google(audio)

#try:
#    print(gsr.recognize_google(audio))
#except sr.UnknownValueError:
#    print("Could not understand audio")
#except sr.RequestError as e:
#    print("gsr service error {}".format(e))