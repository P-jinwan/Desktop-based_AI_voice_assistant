#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fastdtw import fastdtw


# In[2]:


def record_javise():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 3
    
#     file_name = 'ref_Javise'
    file_name = 'test'
    num = 3
    path = '입력단/Speech_Similarity/'
    
    if not '입력단/Speech_Similarity' in os.listdir('입력단/'):
        os.mkdir(path)
    else:
        pass

    audio = pyaudio.PyAudio()

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
    waveFile = wave.open(path + '/' + file_name + "_"+ str(num) + '.wav', 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    print("Done")


# In[3]:


def sampling_function(ref_data, test_data, step):
    sample_idx_ref = [i for i in range(0, len(ref_data), step) ]
    sample_idx_test = [i for i in range(0, len(test_data), step) ]
    return ref_data[sample_idx_ref], test_data[sample_idx_test]


# In[4]:


def speech_similarity(data_1, data_2, step):
    x, y = sampling_function(data_1, data_2, step)
    d, _ = fastdtw(x, y)
    
    print('distance : {}'.format(d))


# In[1]:


def scaling_data(data, test):
    
    mms = MinMaxScaler()
    convert_data = mms.fit_transform(data.reshape(-1, 1))

    mms_1 = MinMaxScaler()
    convert_test = mms.fit_transform(test.reshape(-1, 1))
    
    return convert_data, convert_test


# In[5]:


if __name__ == "__main__":
    print("this file is Speech_Similarity")


# In[ ]:




