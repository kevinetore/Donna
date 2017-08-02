from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
from oauth2client.tools import argparser

from gtts import gTTS
import os
import pyaudio

default_path = '/home/pi/projects/speech_recognition/pocketsphinx/model/en-us/en-us'

# Language model is an important component of the configuration which tells the Decoder which sequence of words are possible to recognzie
config = Decoder.default_config()
config.set_string('-hmm', default_path)
config.set_string('-lm', default_path + '/7864.lm')
# dictionary provides system the data to map vocabulary words to sequence of phonemes
config.set_string('-dict', default_path + '/7864.dic')
config.set_string('-logfn', '/dev/null')
decoder = Decoder(config)

# Default settings for youtube search api request
argparser.add_argument("--q", help="Search term", default="Google")
argparser.add_argument("--max-results", help="Max results", default=1)
args = argparser.parse_args()

p = pyaudio.PyAudio()
stream = p.open(
        format=pyaudio.paInt16, # size of each sample, calc size by: pyaudio.get_sample_size(pyaudio.paInt16)
        channels=1, # mono
        rate=16000, # amount of samples that are taken per second to represent the event digitally
        input=True, # specifies whether this is an input stream. Defaults to False.
        frames_per_buffer=1024 # number of frames the signals are split into
    )
stream.start_stream() # delivering real-time audio through a network

def requested_donna_audio():
    response_donna = "Hello Kevin, sure give me a moment!"
    tts = gTTS(text= response_donna, lang='en')
    # Google text to speech requires MP3 file
    tts.save('response_donna.mp3')
    # We are using Alsa as output to play the MP3
    os.system('mpg321 -o alsa response_donna.mp3')
    os.remove('response_donna.mp3')

in_speech_bf = False
# Start listening
decoder.start_utt()

while True:
    # The sound buffer is a portion of computer memory that temporarily holds sound files on their way to audio speakers.
    sound_buffer = stream.read(1024, exception_on_overflow = False)
    if sound_buffer:
        # Pass the Chunk to the decoder
        decoder.process_raw(sound_buffer, False, False)
        # checks if the last audio buffer contained speech
        if decoder.get_in_speech() != in_speech_bf:
            in_speech_bf = decoder.get_in_speech() # will be set to True now?
            # When the speech ends:
            if not in_speech_bf:
                decoder.end_utt()
                # Since the speech is ended, we can assume that we have final results, then display them
                result = decoder.hyp().hypstr
                print result

                # we could also do something like if "DONNA ADD SONG" in result:
                if result == "DONNA ADD SONG":
                    requested_donna_audio()
                    import search_song
                    search_song.youtube_search(args)
                decoder.start_utt()
    else:
        break
decoder.end_utt()
