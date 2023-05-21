
#import pyttsx3

'''
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 125)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
'''

import os

#os.system("say -r 100 [[volm 0.9]] hello world")

# speak out 'text' with rate as 'rate' and volume as 'volm' 
'''
def speak(text, rate=125, volm=1):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  
    engine.setProperty('rate', rate)  
    engine.setProperty('volume', volm) 
    engine.say(text)
    engine.runAndWait()
'''

def speak(text, rate=125, volm=1):
    command = "say -r " + str(rate) + " [[volm " + str(volm) + "]] " + text
    os.system(command)

#speak("hello world")
#speak("hello world", 200, 1)
