import os
import pyttsx3
import winsound
from gtts import gTTS
import speech_recognition as sr


def stt(verbose=1):
    # obtain audio from the microphone
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # listen for 2 seconds and create the ambient noise energy level
        print("Please wait, calibrating microphone...")
        print('respond after the beep.')
        r.adjust_for_ambient_noise(source, duration=3)
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        audio = r.listen(source)
        if(verbose == 1):
            print('Processing...')

    try:
        i_said = r.recognize_google(audio)
        if(verbose == 1):
            print("You said: " + i_said)
        return i_said
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        # SRS = Speech Recognition Service
        print("Could not request results from Google SRS; {0}".format(e))


def tts(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def gtts(text, lang, save_file=False):
    file = gTTS(text=text, lang=lang)
    filename = 'temp.mp3'
    file.save(filename)
    os.system(filename)
    if(not (save_file)):
        os.remove(filename)
