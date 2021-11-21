print("hello")
import pyttsx3
import os
import sys
import io
import speech_recognition as sr
import datetime
engine = pyttsx3.init( 'sapi5')
voices=engine.getProperty('voices')
def speech(audio):
    engine.say(audio)
    engine.runAndWait()
print(voices[0].id)

def good():
    hour=int(datetime.datetime.now().hour)
    print(hour)
    if(hour>=0 and hour<12):
        speech("Good Morning Baby")
    elif(hour>=12 and hour<18):
        speech("Good Afternoon Baby")
    else:
        speech("Good Evening Baby")
def listen2():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            print('Recognizing')
            query=r.recognize_google(audio,language='en-in')
            print(query)
        except Exception as e:
            print(e)
            return "None"
if __name__ == "__main__":
    speech("welcome in voices enjoy ")
    good()
    speech('How can i help you')
    listen2()

# engine.say("I will speak this ")
# engine.runAndWait()