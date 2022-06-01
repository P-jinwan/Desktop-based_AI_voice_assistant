#!/usr/bin/env python
# coding: utf-8

# In[1]:


def GoogleTTS(text) :
    
    # 필요한 패키지를 임포트 합니다.
    import playsound as ps          # 음향 파일을 읽어주는 패키지입니다.
    import os
    from gtts import gTTS           # google TTS(Text to Speech) API 입니다.
    from IPython.display import Audio 

    tts = gTTS(text=text, lang='ko')         # 입력 받은 텍스트를 음성으로 변환합니다.
    tts.save('kor.wav')                      # 변환된 음성 데이터를 kor.wav 파일로 저장합니다.
    display(Audio('kor.wav', autoplay=True)) # 저장된 파일을 출력합니다.

