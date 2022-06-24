# 데스크탑 기반 인공지능 음성 비서</br>(Desktop-based AI voice assistant)
- 수행 기간(period): 22.05.01 ~ 22.05.30 (30일)

---

## 팀 구성 및 역할(Teaming and Roles)
- `프로젝트 매니저(PM)` - 민경태(min-moon-sick)
- `생체 음성 인식 모델 구현, 서버 환경 구축` - 민경태(min-moon-sick)
- `호출어 인식 구현, 분류기 설계, 멀티프로세싱 구현` - 강성현(Ckichen)
- `모니터 컨트롤 알고리즘 구현, 제스처 프로그램 제어 시스템 구현, TTS 구현` - 박의찬(uichan96)
- `Optimization, Decoder 개발, 날씨 리뷰 알고리즘 구현, 프로그램 자동화 알고리즘 설계, 전반적인 프로그램 관리 및 연계` - 박진완(P-jinwan)

---

## 구현 기능별 시연 영상(Demonstration video by implementation function)
1. 프로그램 실행 및 종료

https://user-images.githubusercontent.com/96413630/171378947-a0e85f20-0b37-4fb6-b2f0-f2cf82863b72.mp4

2. 날씨 리뷰

https://user-images.githubusercontent.com/96413630/171571220-14546b8f-46d6-4be0-8d75-eef4df32f8bb.mp4

---

## 목차(Contents)
1. [프로젝트 개요](https://github.com/P-jinwan/Desktop-based_AI_voice_assistant#%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B0%9C%EC%9A%94project-summary)
2. [프로젝트 수행 절차](https://github.com/P-jinwan/Desktop-based_AI_voice_assistant#%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%88%98%ED%96%89-%EC%A0%88%EC%B0%A8execution-procedure)
3. [출처 및 참고 사이트](https://github.com/P-jinwan/Desktop-based_AI_voice_assistant#%EC%B6%9C%EC%B2%98-%EB%B0%8F-%EC%B0%B8%EA%B3%A0-%EC%82%AC%EC%9D%B4%ED%8A%B8reference)
4. [개선 사항 및 후기](https://github.com/P-jinwan/Desktop-based_AI_voice_assistant#%EA%B0%9C%EC%84%A0-%EC%82%AC%ED%95%AD-%EB%B0%8F-%ED%9B%84%EA%B8%B0improvements-and-reviews)

---

## 프로젝트 개요(Project Summary)

### 1. 프로젝트 선정 배경
- 시중에 상용화된 AI 비서는 스피커를 매개체로 voice by voice의 형태로 음성에 의존하여 수행되는데, 이를 voice by graphics 형태로 청각에 모든 걸 의지하지 않고 시각적으로 나타낼 수 있게 하고 싶었습니다. 또한 많은 AI 비서가 스마트폰과 스마트티브이 등 IoT 제품에 맞춰져 있고 Microsoft 사에서 제공하는 Cortana 같은 AI 비서는 한국에서는 서비스되지 않는 점을 고려하였을 때 한국형 데스크톱 기반의 인공지능 음성 비서는 개발할 만한 가치가 있다고 판단하였고 프로젝트에 착수하게 되었습니다.

### 2. 프로젝트 기대 효과
- 시각적인 효과를 사용자에게 제공하여 편의와 함께 업무를 보조하는 비서 기능을 구현함으로써, 능률을 향상시킬 수 있습니다.

### 3. 구현 기능
- 일상 음성 대화 속 호출어 인식
- 날씨 리뷰
- 프로그램 실행 및 종료
- 사용자와 모니터간 거리를 측정하여 웹 페이지 확대
- 제스처 PPT 제어
- TTS 목소리 커스터마이징

### 4. 개발 환경
- 사용 언어 - Python 3.7 ~ 3.8
- 코드 편집기 - Jupyter notebook, Colab
- 운영 체제 - Window

---

## 프로젝트 수행 절차(Execution Procedure)
1. [블록 다이어그램](https://github.com/P-jinwan/Desktop-based_AI_voice_assistant/blob/master/README.md#1-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%88%98%ED%96%89-%EC%A0%88%EC%B0%A8---%EB%B8%94%EB%A1%9D-%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8)
2. [음성 수집](https://github.com/P-jinwan/Desktop-based_AI_voice_assistant/blob/master/README.md#2-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%88%98%ED%96%89-%EC%A0%88%EC%B0%A8---%EC%9D%8C%EC%84%B1-%EC%88%98%EC%A7%91get-voice)
3. [소음 감소 필터](https://github.com/P-jinwan/Desktop-based_AI_voice_assistant/blob/master/README.md#3-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%88%98%ED%96%89-%EC%A0%88%EC%B0%A8---%EC%86%8C%EC%9D%8C-%EA%B0%90%EC%86%8C-%ED%95%84%ED%84%B0noise-reduction-filter)
4. [생체 인식](https://github.com/P-jinwan/Desktop-based_AI_voice_assistant/blob/master/README.md#4-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%88%98%ED%96%89-%EC%A0%88%EC%B0%A8---%EC%83%9D%EC%B2%B4-%EC%9D%B8%EC%8B%9Dbiometrics)
5. [음성 유사도 비교](https://github.com/P-jinwan/Desktop-based_AI_voice_assistant/edit/master/README.md#5-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%88%98%ED%96%89-%EC%A0%88%EC%B0%A8---%EC%9D%8C%EC%84%B1-%EC%9C%A0%EC%82%AC%EB%8F%84-%EB%B9%84%EA%B5%90comparison-of-speech-similarities)
6. [호출어 인식](https://github.com/P-jinwan/Desktop-based_AI_voice_assistant/edit/master/README.md#6-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%88%98%ED%96%89-%EC%A0%88%EC%B0%A8---%ED%98%B8%EC%B6%9C%EC%96%B4-%EC%9D%B8%EC%8B%9Dwake-up-word)
7. [STT](https://github.com/P-jinwan/Desktop-based_AI_voice_assistant/edit/master/README.md#7-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%88%98%ED%96%89-%EC%A0%88%EC%B0%A8---sttspeech-to-text)
8. [분류기](https://github.com/P-jinwan/Desktop-based_AI_voice_assistant/edit/master/README.md#8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%88%98%ED%96%89-%EC%A0%88%EC%B0%A8---%EB%B6%84%EB%A5%98%EA%B8%B0classification-model)
9. [디코더](https://github.com/P-jinwan/Desktop-based_AI_voice_assistant/edit/master/README.md#9-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%88%98%ED%96%89-%EC%A0%88%EC%B0%A8---%EB%94%94%EC%BD%94%EB%8D%94decoder)
10. [① 프로그램 제어](https://github.com/P-jinwan/Desktop-based_AI_voice_assistant/edit/master/README.md#10-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%88%98%ED%96%89-%EC%A0%88%EC%B0%A8----%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-%EC%A0%9C%EC%96%B4)
11. [② 제스처 제어](https://github.com/P-jinwan/Desktop-based_AI_voice_assistant/edit/master/README.md#11-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%88%98%ED%96%89-%EC%A0%88%EC%B0%A8----%EC%A0%9C%EC%8A%A4%EC%B2%98-%EC%A0%9C%EC%96%B4)
12. [③ 모니터 축소 및 확대 제어](https://github.com/P-jinwan/Desktop-based_AI_voice_assistant/edit/master/README.md#12-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%88%98%ED%96%89-%EC%A0%88%EC%B0%A8----%EB%AA%A8%EB%8B%88%ED%84%B0-%EC%B6%95%EC%86%8C-%EB%B0%8F-%ED%99%95%EB%8C%80-%EC%A0%9C%EC%96%B4)
13. [④ 날씨 리뷰](https://github.com/P-jinwan/Desktop-based_AI_voice_assistant/edit/master/README.md#13-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%88%98%ED%96%89-%EC%A0%88%EC%B0%A8----%EB%82%A0%EC%94%A8-%EB%A6%AC%EB%B7%B0)
14. [TTS](https://github.com/P-jinwan/Desktop-based_AI_voice_assistant#14-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%88%98%ED%96%89-%EC%A0%88%EC%B0%A8---ttstext-to-speech)

### 1. 프로젝트 수행 절차 - 블록 다이어그램
![블록 다이어그램](https://user-images.githubusercontent.com/96413630/171382906-3aabcea5-41a6-4426-bc2c-8fb78b325e6b.png)

### 2. 프로젝트 수행 절차 - 음성 수집(Get voice)
![20220601_193425](https://user-images.githubusercontent.com/96413630/171385336-e9105f8e-659c-4a85-a19e-3941fbbab6ae.png)

#### (1) Info & Effect
- SpeechRecognition 라이브러리 사용
- 마이크 객체를 지정한 후 아날로그 음성 데이터를 수집
- 음성 수집시 필요에 따라 주파수(khz)를 sample rate로 설정함

#### (2) Procedure
![그림2](https://user-images.githubusercontent.com/96413630/171385759-3d66ad49-fe41-4f34-aa3b-2cf6b95b566d.png)

### 3. 프로젝트 수행 절차 - 소음 감소 필터(Noise Reduction Filter)
![20220601_193334](https://user-images.githubusercontent.com/96413630/171385200-65e121cb-14fa-4e87-b706-f52ab4970b34.png)

#### (1) Info & Effect
- None Stationary Noise Reduction 기법은 시간이 지남에 따라 잡음 게이트가 변경될 수 있음
- 신호가 발생하는 타임스케일을 알고 있는 경우 더 긴 타임스케일에서 발생하는 이벤트가 노이즈라는 가정을 기반으로 노이즈 임계값을 설정할 수 있음
- 이 알고리즘은 채널당 에너지 정규화(Per-Channel Energy Normalization)라고 하는 생체 음향학의 최근 방법에 의해 동기가 부여되었음

#### (2) Procedure
- 신호를 통해 스펙트로그램을 계산 → IIR 필터를 사용하여 시간 평활화된 스펙트럼 계산 → 스펙트로그램을 기반으로 마스크 생성 → 마스크가 신호의 스펙트로그램에 적용되고 변환

### 4. 프로젝트 수행 절차 - 생체 인식(biometrics)
![image](https://user-images.githubusercontent.com/96413630/171386559-12e83927-8ae5-4c82-bc92-70b628afe7a5.png)

#### (1) Info & Effect
- 생체 패턴을 파악하여 수집된 음성의 출처를 찾을 수 있음
- 사용자로 등록된 음성만 데스크탑을 제어할 수 있음

#### (2) Procedure
- 사용자 음성 3차례 입력 → 수집된 음성에 소음 감소 필터 적용 → 필터를 거친 음성 Stacking → 음성에 대해 Gaussian Mixture Model을 사용하여 학습 및 평가

### 5. 프로젝트 수행 절차 - 음성 유사도 비교(Comparison of speech similarities)
![image](https://user-images.githubusercontent.com/96413630/171390678-16e5deb2-1202-48d7-a76d-acfbb130f154.png)

#### (1) Info & Effect
- FastDTW 사용
- 음성 발생 시 유사도를 파악하여 생체 정보가 등록된  사용자의 음성만 수집하도록 함

#### (2) Procedure
- 사용자 음성 3차례 입력 → 수집된 음성에 소음 감소 필터 적용 → 필터를 거친 음성 Stacking → 음성에 대해 Gaussian Mixture Model을 사용하여 학습 및 평가

### 6. 프로젝트 수행 절차 - 호출어 인식(Wake up word)
![image](https://user-images.githubusercontent.com/96413630/171557516-379a5f66-276a-4390-97e7-5041afd13756.png)

#### (1) Info & Effect
- 호출어(Wake-up Word)의 식별 및 정확도 개선
- 소음(Noise)을 감안한 예측 모델 사용
- STT의 데이터 병목현상(Bottleneck) 방지

#### (2) Procedure
![image](https://user-images.githubusercontent.com/96413630/171557723-be4cdbda-6536-4293-941e-0389f93b23ce.png)

### 7. 프로젝트 수행 절차 - STT(Speech to Text)
![image](https://user-images.githubusercontent.com/96413630/171557904-8f93682c-bc6a-42f4-a6a6-df271ccbc935.png)

#### (1) Info & Effect
- Kakao STT API 사용
- Google STT, IBM Watson STT API 등 다른 API보다 긴 무료 시간과 사용이 쉽기 때문에 개발 및 테스트에 용이하다고 판단되어 채택
- 키보드 대신 음성 문자를 입력으로 사용하여 위치의 한계를 벗어나 자유롭게 입력할 수 있음
- 음성 데이터는 Mono channel(1), 16000 Hz sample rate, 16 bit depth PAW PCM 포맷만 지원함

#### (2) Procedure
![image](https://user-images.githubusercontent.com/96413630/171558194-0091f83f-730d-4381-aeb8-8ca5d9395a38.png)

### 8. 프로젝트 수행 절차 - 분류기(Classification Model)
![image](https://user-images.githubusercontent.com/96413630/171558347-f59b41b8-04ae-4cf0-bf43-8a8cc2fb451b.png)

#### (1) Info & Effect
- STT로부터 받은 텍스트를 프로세스 처리의 인자로 보내기 위해서는 각 단어의 태그가 필요
- 문장 내 단어들이 가지는 의미를 파악하는 임베딩 예측 모델
- LSTM, BERT 모델의 성능 (정확도 및 처리 속도) 비교 후 BERT 모델 채택

#### (2) Procedure
- Mecab 형태소 분석기를 사용하여 텍스트를 나눔 → word_to_index로 정수화 → Padding 부분에 대한 mask_zero 처리 → LSTM 레이어의 각 시퀀스에서 다대다(Many to many) 출력 → 모델 구축(손실 함수: sparse_categorical_crossentropy, 옵티마이저: adam) → 학습 및 예측

### 9. 프로젝트 수행 절차 - 디코더(Decoder)
![image](https://user-images.githubusercontent.com/96413630/171559364-84e9ccfb-ea8f-449c-954f-7306b4630ad8.png)

#### (1) Info & Effect
- 분류기에서는 하나의 단어를 어절 별로 끊기 때문에 정확한 기능 수행이 어려워짐
- 디코더는 이를 보완하여 가령 [‘파워’, ‘포인트’]라는 입력을 받게 되면 [‘파워 포인트’]라는 하나의 단어로 묶어 정확한 기능 수행이 가능하게 됨
- 다중 비교가 용이한 인덱스 번호로 변환하여 토큰 별로 여러 개의 단어가 들어와도 처리가 가능함
- 한 문장 속 명령이 여러 개일 경우 순차적으로 처리할 수 있음

#### (2) Procedure
![image](https://user-images.githubusercontent.com/96413630/171560174-f1d5bea0-609c-4442-8a61-a9f88a8b22f1.png)

### 10. 프로젝트 수행 절차 - ① 프로그램 제어
![image](https://user-images.githubusercontent.com/96413630/171560232-799221a7-6e63-42e1-9964-3168d803d602.png)

#### (1) Info & Effect
- 음성으로 프로그램을 호출하는 기능
- 마우스로 직접 클릭을 하지 않아도 음성으로 프로그램을 제어할 수 있음

#### (2) Procedure
- Decoder의 결괏값에 맞는 명령 실행 (Python - Windows 자동화 모듈 : PyWinAuto)
- 활성화(작업표시줄에 열린 상태)를 기준으로 프로세스에 명령을 할당하며, 활성화되어 있지 않을 경우 새로 프로세스를 실행시킴
- 프로세스 ID, 이름, 핸들 값 등의 정보로 프로세스를 찾아 윈도우 객체로 연결시키면 해당 객체의 속성에 따라 다양한 명령 제어가 가능

### 11 프로젝트 수행 절차 - ② 제스처 제어
![image](https://user-images.githubusercontent.com/96413630/171560232-799221a7-6e63-42e1-9964-3168d803d602.png)

#### (1) Info & Effect
- Power Point 등의 프로그램을 손동작으로 제어하는 기능  
- MediaPipe 프레임워크를 사용한 Open CV 프로그램
- 손의 동작을 파악하여 지정된 기능을 수행

#### (2) Procedure
![image](https://user-images.githubusercontent.com/96413630/171561614-a8bd1d1a-d046-4d21-9332-ea2df8926db9.png)

### 12. 프로젝트 수행 절차 - ③ 모니터 축소 및 확대 제어
![image](https://user-images.githubusercontent.com/96413630/171560232-799221a7-6e63-42e1-9964-3168d803d602.png)

#### (1) Info & Effect
- 모니터와 얼굴의 거리를 파악하여 자동으로 화면을 확대, 축소하는 기능 
- dlib 라이브러리를 사용한 Open CV 프로그램
- 모니터와의 거리를 통해 화면을 제어함으로써 눈의 피로도 감소

#### (2) Procedure
- dlib를 통해 얼굴의 좌표를 받음
- 두 눈의 좌표를 통해 두 눈 사이의 거리를 계산하여 반환
- 두 눈 사이의 거리를 기준으로 짧아지면 화면 축소 기능, 길어지면 화면 확대 기능을 수행 

### 13. 프로젝트 수행 절차 - ④ 날씨 리뷰
![image](https://user-images.githubusercontent.com/96413630/171560232-799221a7-6e63-42e1-9964-3168d803d602.png)

#### (1) Info & Effect
- 오늘 날씨를 읽어주는 기능
- BeautifulSoup와 requests 라이브러리를 사용한 웹 크롤링
- 현재 위치한 지명과 대략적인 날씨, 최저온도, 최고온도를 브리핑함

#### (2) Procedure
![image](https://user-images.githubusercontent.com/96413630/171562022-cf916f89-0b81-41ff-92fb-5eb8bd91f409.png)

### 14. 프로젝트 수행 절차 - TTS(Text to Speech)
![image](https://user-images.githubusercontent.com/96413630/171562087-34224aab-f9e2-4696-90b8-3c2fd7029d9c.png)

#### (1) Info & Effect
- 결과를 음성으로 알려줌으로써 시각의 의존에서 벗어남 
- 사람과 프로그램이 대화가 가능하게 할 수 있음
- 스피커만으로 서비스를 제공할 수 있음
- Tacotron2와 Multi-band Melgen 모델 사용
- 목소리 커스터마이징 가능(1 ~ 2초 사이의 짧은 문장으로 이루어진 녹음 음성 약 500개 필요)

#### (2) Procedure
![image](https://user-images.githubusercontent.com/96413630/171562304-ab9cbb4c-7cad-454b-b007-c1da7b37c79c.png)

## 출처 및 참고 사이트(Reference)
- 단어장 데이터 → [한국해양대학교 자연언어처리연구실](https://github.com/kmounlp/NER)
- 멀티프로세싱 → [파이썬 멀티프로세싱 document](https://docs.python.org/ko/3/library/multiprocessing.html)
- 음성 전처리 → [bytes to numpy and numpy to bytes](https://d-tail.tistory.com/32), [bytes to numpy](https://stackoverflow.com/questions/53376786/convert-byte-array-back-to-numpy-array), [BytesIO document](https://docs.python.org/ko/3/library/io.html)
- 크롤링 → [BeautifulSoup](https://library.gabia.com/contents/9239/)
- STT → [Kakao STT API](https://park-duck.tistory.com/entry/python-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9D%8C%EC%84%B1API-STT-feat-postman), [Kakao STT API 공식 문서](https://developers.kakao.com/docs/latest/ko/reference/rest-api-reference)
- 호출어 → [호출어 관련](https://www.youtube.com/watch?v=jYgMMy8KAc0)
- 분류기 → [LSTM + CRF](https://wikidocs.net/34156/), [NER](https://www.letr.ai/explore/tech-20210723)
- 생체 인식 → [GMM Model](https://ratsgo.github.io/speechbook/docs/am/gmm#gaussian-mixture-model-1)

## 개선 사항 및 후기(Improvements and reviews)

### 1. 개선 사항
- 멀티프로세싱을 이용한 병렬 연산 처리
- 제스처 인식 기능 향상
- 음성 인식 기능 향상
- 기능 추가

### 2. 후기
- 배워본 적 없는 음성의 세계에 첫 발을 내디딘 프로젝트로써 의미가 있었습니다. 또 API를 처음 사용해 보았고 처음 프로젝트와 달리 체계적으로 진행하여 블록을 맞추듯 하나 둘 조립되어 가는 과정을 보며 매우 즐거웠습니다. 개발 과정에서 어려운 점이나 문제를 겪고 해결해 나갈 때 짜릿함과 쾌감은 말로 이룰 수 없을 정도로 좋았습니다. 팀원들이 너무나도 좋은 사람들이고 실력이 다들 출중하셔서 당초 계획했던 것보다는 몸집이 커졌습니다. 그럼에도 시니어 개발자들이 보기엔 초라한 결과물이지만 즐겁고 나름 좋은 결과를 도출할 수 있어서 매우 좋았습니다. 앞으로도 음성 관련해서 공부를 더 하고 싶네요.
