import speech_recognition as sr # recognise speech        
from gtts import gTTS # google text to speech    
from time import ctime # get time details    
import webbrowser # open browser    
import ssl    
import certifi    
import time    
import os # to remove created audio files 

def speak(audio_string):    
tts = gTTS(text=audio_string, lang='en') # text to speech(voice)    
r = random.randint(1,20000000)    
audio_file = 'audio' + str(r) + '.mp3'    
tts.save(audio_file) # save as mp3    
playsound.playsound(audio_file) # play the audio file    
print(f"May Day: {audio_string}") # print what app said    
os.remove(audio_file) # remove audio file     


r = sr.Recognizer() # initialise a recogniser    
# listen for audio and convert it to text:    
def record_audio(ask=False):    
    with sr.Microphone() as source: # microphone as source    
        if ask:    
            speak(ask)    
        audio = r.listen(source)  # listen for the audio via source    
        voice_data = ''    
        try:    
            voice_data = r.recognize_google(audio)  # convert audio to text    
        except sr.UnknownValueError: # error: recognizer does not understand    
            speak('I did not get that')    
        except sr.RequestError:    
            speak('Sorry, the service is down') # error: recognizer is not connected    
        print(f">> {voice_data.lower()}") # print what user said    
        return voice_data.lower()   