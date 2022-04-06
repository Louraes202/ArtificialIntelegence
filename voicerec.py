# libraries: speech_recognition | 
import os
import speech_recognition as Sr

r = Sr.Recognizer()

sampleaudio1 = Sr.AudioFile("interviewtips.wav")

with sampleaudio1 as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)

print(r.recognize_google(audio))