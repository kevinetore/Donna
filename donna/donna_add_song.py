from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
from oauth2client.tools import argparser

from gtts import gTTS
import os

default_path = '/home/pi/projects/speech_recognition/pocketsphinx/model/en-us/en-us'

config = Decoder.default_config()
config.set_string('-hmm', default_path)
config.set_string('-lm', default_path + '/7864.lm')
config.set_string('-dict', default_path + '/7864.dic')
config.set_string('-logfn', '/dev/null')
decoder = Decoder(config)

# Default settings for youtube search api request
argparser.add_argument("--q", help="Search term", default="Google")
argparser.add_argument("--max-results", help="Max results", default=1)
args = argparser.parse_args()

import pyaudio
p = pyaudio.PyAudio()
stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=1024
    )
stream.start_stream()

in_speech_bf = False
decoder.start_utt()
while True:
    buf = stream.read(1024, exception_on_overflow = False) # Ik heb exception on overflow nodig omdat de CPU van de Pi het anders niet trekt
    if buf:
        decoder.process_raw(buf, False, False)
        if decoder.get_in_speech() != in_speech_bf:
            in_speech_bf = decoder.get_in_speech()
            if not in_speech_bf:
                decoder.end_utt()
                result = decoder.hyp().hypstr
                if result == 'DONNA ADD SONG':
                    print result
                    donna = "Hello master Kevin, sure give me a moment!"
                    tts = gTTS(text= donna, lang='en')
                    tts.save('initial_state.mp3')
                    os.system('mpg321 -o alsa initial_state.mp3')
                    os.remove('initial_state.mp3')
                    
                    import search_song
                    search_song.youtube_search(args)
                decoder.start_utt()
    else:
        break
decoder.end_utt()
