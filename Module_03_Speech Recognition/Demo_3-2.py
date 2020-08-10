# -*- coding: utf-8 -*-

import speech_recognition as sr

def transcribe(wav_path):
    '''
    Speech to Text by Google free API
    language: en-US, zh-TW
    '''
    language_choose = 'zh-TW'
    # language_choose = 'en-US'
    # language_choose = 'en-GB'
    # language_choose = 'ja-JP'
    # language_choose = 'ko-KR'
    # language_choose = 'de-DE'
    # language_choose = 'es-ES'
    # language_choose = 'fr-FR'
    

    r = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio = r.record(source)
    try:
        # return r.recognize_google(audio, language="zh-TW")
        return r.recognize_google(audio, language=language_choose)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return None
    

# 欲辨識的音檔位置
wav_path = "ENG_M.wav"
text = transcribe(wav_path)
print(text)



