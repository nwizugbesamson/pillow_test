import speech_recognition as sr
from os import path
from pydub import AudioSegment

# convert mp3 file to wav                                                       
sound = AudioSegment.from_file('data/Audio/Recording.m4a',  format= 'm4a')
sound.export("data/Audio/transcript.wav", format="wav")


# transcribe audio file                                                         
AUDIO_FILE = "data/Audio/transcript.wav"

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        print("Transcription: " + r.recognize_google(audio))



## https://pythonbasics.org/transcribe-audio/