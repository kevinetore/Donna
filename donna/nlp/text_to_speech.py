def speak(arg):
	import pyttsx
	engine = pyttsx.init()
	engine.setProperty('voice', 'english+f4')
	rate = engine.getProperty('rate')
    	engine.setProperty('rate', rate-5)
    	engine.say(arg)
    	engine.say("   ")
    	engine.runAndWait()
speak('Hello, I\'m, Donna, and, I, just, added, the, song, Freak, to, your, favorites, on, youtube!')
