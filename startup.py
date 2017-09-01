import time
import threading
import os

def server():
	path = '/home/pi/projects/webapp'
	os.chdir(path)
	os.system("python3 manage.py runserver")

def donna():
	path = '/home/pi/projects'
	os.chdir(path)
	os.system("python donna_add_song.py")

s = threading.Thread(name='server', target=server)
d = threading.Thread(name='donna', target=donna)

s.start()
d.start()
