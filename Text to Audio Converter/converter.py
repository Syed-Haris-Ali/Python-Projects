#By Codred Tech

# pip install gtts
from typing import Text
from gtts import gTTS

# pip install playsound
from playsound import playsound


audio = 'speech.mp3'     #The file name you want to create
language = 'ur'        #The language you want to convert
sp = gTTS(text="Enter Your Text Here",
          lang=language, slow=False) 
sp.save(audio)
playsound(audio)
