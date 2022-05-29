#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Kakao의 Open API를 사용하여 STT 기능을 함수로 구현합니다.
def KakaoSTT(data) :
    
    # 필요한 패키지를 임포트 합니다.
    import requests
    import json

    # API의 전달할 내용을 작성합니다.
    headers = {"Content-Type": "application/octet-stream", "Authorization": "KakaoAK " + '419b7a94f1afa5d4e729cbefb11338f6'}

    # Request의 POST와 HOST를 참조하여 카카오 음성 url을 설정합니다.
    kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"

    # Kakao API의 음성 인식을 요청합니다.
    voice_re = requests.post(kakao_speech_url, headers=headers, data=data)

    # 요청에 실패했을 경우 예외 처리를 합니다.
    if voice_re.status_code != 200 : 
        text=""
        print("error! because",  voice_re.json())
    else :
        result = voice_re.text[voice_re.text.index('{"type":"finalResult"'):voice_re.text.rindex('}')+1]
        text = json.loads(result).get('value')

    return text

