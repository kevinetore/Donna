from gtts import gTTS
import os

def addedSong(title):
    donna = "Hello, I just added the song: {} to your favorites on Youtube! Have a nice day".format(title)
    tts = gTTS(text= donna, lang='en')
    tts.save('added_default.mp3')
    os.system('mpg321 -o alsa added_default.mp3')
    os.remove('added_default.mp3')