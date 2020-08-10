# -*- coding: utf-8 -*-

import pyaudio
import wave
import matplotlib.pyplot as plt
import numpy as np


def record(duration_sec, fs):
    ''' Record duration_sec with sampling rate fs '''
    
    chunk = 2048
    p = pyaudio.PyAudio()
    stream = p.open( format=pyaudio.paFloat32, channels=1, rate=fs, input=True, frames_per_buffer=chunk)
    speech = []
    print('Start recording...')
    for i in range(int(duration_sec*fs/chunk)):
        reading_samples = np.frombuffer(stream.read(chunk), dtype = np.float32).tolist()
        speech.extend(reading_samples)
    print('Finished!')
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    return np.asarray(speech).astype(np.float32)


def play_raw(speech, fs):
    ''' Play audio raw data '''

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
    stream.write(speech.tostring())
    stream.stop_stream()
    stream.close()
    p.terminate()


def save_wav(speech, fs):
    ''' Save as wav file '''
    
    wf = wave.open('sample.wav', 'sm')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(fs)
    wf.writeframes(b''.join((speech*32768).astype(np.int16)))
    wf.close()
    print('Done: record.wav')
    
    
'''
作業：
設定取樣率為 16000
錄音 5 秒鐘
說「我要預約」
'''

fs =   16000         # Write your code here
duration_sec =  5# Write your code here
speech = record(duration_sec, fs)     # Write your code here

# 輸出音檔，存至 record.wav
save_wav(speech, fs)