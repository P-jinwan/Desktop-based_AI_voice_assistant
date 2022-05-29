#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 마이크에서 음성을 수집하는 함수입니다.
def GetSpeech() :
    
    # 필요한 패키지를 임포트 합니다.
    import speech_recognition as sr

    r = sr.Recognizer() # 마이크에서 음성을 수집하는 객체를 생성합니다.

    microphone = sr.Microphone(sample_rate=16000) # 마이크 객체를 생성하고 Khz를 16000으로 설정합니다.

    with microphone as source :            # 마이크 객체 source를 선언합니다.
        r.adjust_for_ambient_noise(source) # 음성 수집 시 소음 수치를 반영하여 음성을 명확하게 받게 합니다.
        print('음성을 청취 중입니다.')
        try :
            result = r.listen(source)      # 마이크에서 입력되는 음성을 수집하여 result 변수에 저장합니다.
            return result
        except Exception as e :            # 음성이 제대로 수집 되지 않았을 경우
            print('Exception: ' + str(e))  # 에러 메세지를 출력합니다.
            return ('입력된 음성이 없습니다. 계속 청취합니다.')

