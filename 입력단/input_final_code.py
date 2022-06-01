#!/usr/bin/env python
# coding: utf-8

# In[5]:


def VoiceCollect() :
    ########## 패키지 임포트(임포트 경로는 메인 코드 기준으로 작성할 것) ##########
    from 입력단.Voice_Input import get_speech as gs
    from 입력단.Voice_Input import kakao_stt as stt
    from 입력단.Noise_Reduction import noise_cancellation as nc
    from 입력단.Biomatic_Voice_Recognization import biomatric_voice_recognization as bvr
    from 입력단.Speech_Similarty import Speech_Similarity as ss
    import scipy
    import time
    ########## 패키지 임포트(임포트 경로는 메인 코드 기준으로 작성할 것) ##########
    
    ########## 함수 선언 ##########
    # Numpy array를 Bytes로 변환하는 함수입니다.
    def NumpyToBytes(numpy_array) :
        # numpy array to bytes
        ntb = numpy_array.tobytes()
        
        return ntb
    ########## 함수 선언 ##########
    
    # 음성을 수집합니다.
    voice = gs.GetSpeech()
    
    start = time.time()
    # 노이즈 필터를 거쳐 선명한 음성을 받습니다.
    nf_voice = nc.NoiseCancellation(voice, 1)
    print('노이즈 필터 소요시간:', time.time() - start)
    
    start = time.time()
    # 생체 인식 GMM 모델을 사용하여 목소리의 주인을 찾습니다.
    identity = bvr.recognize_file(nf_voice)
    print('GMM 소요시간:', time.time() - start)
    
    start = time.time()
    # 비교용 녹음 파일을 읽어 들입니다.(추후에 데이타 베이스로 경로 변경 할 것)
    sample_rate, data = scipy.io.wavfile.read('입력단/Speech_Similarty/ref_Javise.wav')
    
    # 녹음 파일과 실시간 수집된 음성의 유사도를 확인합니다.
    ss.speech_similarity(nf_voice, data, 20)
    print('유사도 소요시간:', time.time() - start)
    
    start = time.time()
    # 노이즈를 제거한 데이터의 요소값을 bytes로 변환합니다.
    bytes_voice = NumpyToBytes(nf_voice)

    # 텍스트로 변환합니다.
    text = stt.KakaoSTT(bytes_voice)
    print('STT 소요시간:', time.time() - start)

    return text