#!/usr/bin/env python
# coding: utf-8

# In[1]:


def NoiseCancellation(voice , mode):
    ############################## ▼패키지 임포트▼ ##############################
    import numpy as np
    import soundfile as sf
    import sounddevice as sd
    import scipy.io.wavfile
    import noisereduce as nr
    ############################## ▲패키지 임포트▲ ##############################
    
    ############################## ▼함수 선언▼ ##############################
    def SNRFilter(data, sample_rate) :
        # 음성 파일에서 추출한 데이터의 소음을 줄입니다.
        audio_snrf = nr.reduce_noise(
            y=data,                    # 입력 신호를 지정합니다
            sr=sample_rate,                # 입력 신호/노이즈 신호의 샘플링 속도를 정의합니다.
            n_std_thresh_stationary=1.5,   # 고정 노이즈 제거 강도를 지정합니다.
            stationary=True)               # 고정 또는 비고정 노이즈 감소를 수행할지 여부를 지정합니다.
        
        return audio_snrf

    def NSNRFilter(data, sample_rate) :
        # 음성 파일에서 추출한 데이터의 소음을 줄입니다.
        audio_nsnrf = nr.reduce_noise(
            y=data,                    # 입력 신호를 지정합니다
            sr=sample_rate,                # 입력 신호/노이즈 신호의 샘플링 속도를 정의합니다.
            thresh_n_mult_nonstationary=2, # 노이즈 제거 강도를 지정합니다.
            stationary=False)              # 고정 또는 비고정 노이즈 감소를 수행할지 여부를 지정합니다.
        
        return audio_nsnrf
    ############################## ▲함수 선언▲ ##############################
    
    ############################## ▼노이즈 제거 실행▼ ##############################
    with open("입력단/Noise_Reduction/audio.wav", "wb") as f :
        f.write(voice.get_wav_data())

    # 음성 파일에서 데이터와 레이트를 추출합니다.
    sample_rate, data = scipy.io.wavfile.read('입력단/Noise_Reduction/audio.wav')

    # 노이즈 필터를 거쳐 선명한 음성을 받습니다.
    if mode == 0:
        nf_voice = SNRFilter(data, sample_rate)
    else:
        nf_voice = NSNRFilter(data, sample_rate)
    
    return nf_voice
    ############################## ▲노이즈 제거 실행▲ ##############################

