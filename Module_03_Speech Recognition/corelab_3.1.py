# -*- coding: utf-8 -*-

import speech_recognition as sr


def transcribe(wav_path):
    '''
    Speech to Text by Google free API
    language: en-US, zh-TW
    '''
    
    r = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio = r.record(source)
    try:
        return r.recognize_google(audio, language="zh-TW")
        # Write your code here
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return None
    

'''
作業
設定音檔 record.wav
選擇中文，進行辨識
'''

wav_path = "../Module_02_PyAudio/ENG_M.wav"  # Write your code here
text = transcribe(wav_path)
print(text)



 