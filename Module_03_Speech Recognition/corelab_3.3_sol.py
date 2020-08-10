# -*- coding: utf-8 -*-

import speech_recognition as sr


r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)


'''
作業
設定英文，並開起麥克風辨識
隨意說一句話
'''

try:
    '''
    language: en-US, zh-TW
    '''
    print('You said:', r.recognize_google(audio, language="en-US"))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))



