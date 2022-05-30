#!/usr/bin/env python
# coding: utf-8

# # Biomatric Voice Recognization
# 
# - 참고 링크 
# https://github.com/MohamadMerchant/Voice-Authentication-and-Face-Recognition

# In[4]:


import os
import sys

import numpy as np
import pandas as pd

import pyaudio
import time

from IPython.display import Audio, display, clear_output
import wave
import sklearn
from sklearn.mixture import GaussianMixture as GMM
import pickle
from scipy.io.wavfile import read
import matplotlib.pyplot as plt


# In[12]:


def add_voice(name):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 3

    path = '입력단/Biomatic_Voice_Recognization/Speech_Database/'

    
    print("음성 등록을 위해 3회 녹음을 진행합니다.\n")
    
    
    for i in range(3):
        print('{}번째 녹음을 진행합니다.\n '.format(i+1))
        
        audio = pyaudio.PyAudio()

        if i == 0:
            j = 5
            while j>=0:
                time.sleep(1.0)
                print("Speak your name in {} seconds".format(j))
                clear_output(wait=True)

                j-=1

        elif i ==1:
            print("Speak your name one more time")
            time.sleep(0.5)

        else:
            print("Speak your name one last time")
            time.sleep(0.5)

        # start Recording
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                  rate=RATE, input=True,
                  frames_per_buffer=CHUNK)

        print("recording...")

        frames = []

        for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        # stop Recording
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # saving wav file of speaker
        waveFile = wave.open(path + '/' + name + "_"+ str((i+1)) + '.wav', 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
        print("Done")
    
    dest =  "입력단/Biomatic_Voice_Recognization/GMM_Model/"


# In[17]:


def BVR_train():
    voice_file_list = os.listdir('Biomatic_Voice_Recognization/Speech_Database/')

    voice_file_list = sorted(voice_file_list)

    dest =  "입력단/Biomatic_Voice_Recognization/GMM_Model/"
    count = 0

    for i in voice_file_list:

        path = os.path.join('입력단/Biomatic_Voice_Recognization/Speech_Database/' + i)

        features = np.array([])

        (sr, audio) = read(path)

        vector = audio

        if features.size == 0:
            features = vector
        else:
            features = np.vstack((features, vector))

        if count == 2:  
            features_2dim = np.concatenate([features, features]).reshape(-1, 2)
            
            gmm = GMM(n_components = 2, covariance_type='diag',n_init = 3)
            gmm.fit(features_2dim)

            # saving the trained gaussian model
            pickle.dump(gmm, open(dest + i[:3] + '.gmm', 'wb'))

            features = np.asarray(())
            count = 0
        count = count + 1


# In[ ]:


def recognize_file(file):
    
    modelpath = "입력단/Biomatic_Voice_Recognization/GMM_Model/"
    
    gmm_files = [os.path.join(modelpath,fname) for fname in 
           os.listdir(modelpath) if fname.endswith('.gmm')]

    models    = [pickle.load(open(fname,'rb')) for fname in gmm_files]

    speakers   = [fname.split("/")[-1].split(".gmm")[0] for fname 
           in gmm_files]
    
    #read test file
#     sr,audio = read(file)
    audio = file

    # extract mfcc features
#     vector = extract_features(audio,sr)
    log_likelihood = np.zeros(len(models)) 

    #checking with each model one by one
    for i in range(len(models)):
        gmm = models[i]   
        audio_2dim = np.concatenate([audio, audio]).reshape(-1, 2)
        scores = np.array(gmm.score(audio_2dim))
        log_likelihood[i] = scores.sum()

    pred = np.argmax(log_likelihood)
    identity = speakers[pred]

    # if voice not recognized than terminate the process
    if identity == 'unknown':
        print("Not Recognized! Try again...")
        return

    print('pred : ', pred)
    print('log_likelihood : ', log_likelihood)
    print( "Recognized as - ", identity)
    
    return identity


# In[8]:


def recognize():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 3
    
    testname ='입력단/Biomatic_Voice_Recognization//test.wav'
    
    audio = pyaudio.PyAudio()
    
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
               rate=RATE, input=True,
               frames_per_buffer=CHUNK)
    print("recoding.....")
    
    frames = []
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("finished recording")
    
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    # saving wav file 
    waveFile = wave.open(testname, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    
    modelpath = "입력단/Biomatic_Voice_Recognization/GMM_Model/"
    
    gmm_files = [os.path.join(modelpath,fname) for fname in 
           os.listdir(modelpath) if fname.endswith('.gmm')]

    models    = [pickle.load(open(fname,'rb')) for fname in gmm_files]

    speakers   = [fname.split("/")[-1].split(".gmm")[0] for fname 
           in gmm_files]
    
    #read test file
    sr,audio = read(testname)

    # extract mfcc features
#     vector = extract_features(audio,sr)
    log_likelihood = np.zeros(len(models)) 

    #checking with each model one by one
    for i in range(len(models)):
        gmm = models[i]   
        audio_2dim = np.concatenate([audio, audio]).reshape(-1, 2)
        scores = np.array(gmm.score(audio_2dim))
        log_likelihood[i] = scores.sum()

    pred = np.argmax(log_likelihood)
    identity = speakers[pred]

    # if voice not recognized than terminate the process
    if identity == 'unknown':
        print("Not Recognized! Try again...")
        return

#     print('pred : ', pred)
#     print('log_likelihood : ', log_likelihood)
    print( "Recognized as - ", identity)
    
    return identity


# In[22]:


if __name__ == "__main__":

    identity = recognize()
    
    # 저장된 인원 list
    identity_list = set([i[:3] for i in os.listdir('입력단/Biomatic_Voice_Recognization/Speech_Database/')])

    # 등록된 사용자인지 확인
    if identity in list(identity_list):
        print(identity)

    else:
        print("등록되지 않은 사용자 입니다.")


# In[14]:


# add_voice('민경태')


# In[18]:


# BVR_train()


# In[ ]:




