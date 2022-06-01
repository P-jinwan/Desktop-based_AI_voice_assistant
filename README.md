# 데스크탑 기반 인공지능 음성 비서</br>(Desktop-based AI voice assistant)
- 수행 기간(period): 22.05.01 ~ 22.05.30 (30일)

---

## 팀 구성 및 역할(Teaming and Roles)
- `프로젝트 매니저(PM)` - 민경태(min-moon-sick)
- `생체 음성 인식 모델 구현, 서버 환경 구축` - 민경태(min-moon-sick)
- `호출어 인식 구현, 분류기 설계, 멀티프로세싱 구현` - 강성현(Ckichen)
- `모니터 컨트롤 알고리즘 구현, 제스처 프로그램 제어 시스템 구현, TTS 구현` - 박의찬
- `Optimization, Decoder 개발, 날씨 리뷰 알고리즘 구현, 프로그램 자동화 알고리즘 설계, 전반적인 프로그램 관리 및 연계` - 박진완(P-jinwan)

---

## 구현 기능별 시연 영상(Demonstration video by implementation function)
1. 날씨 리뷰

https://user-images.githubusercontent.com/96413630/171378947-a0e85f20-0b37-4fb6-b2f0-f2cf82863b72.mp4

---

## 목차(Contents)
1. [프로젝트 개요]
2. [프로젝트 수행 절차]
3. [출처 및 참고 사이트]
4. [개선 사항 및 어려웠던 점과 느낀 점]

---

## 프로젝트 개요(Project Summary)

### 1. 프로젝트 선정 배경
- 시중에 상용화된 AI 비서는 스피커를 매개체로 voice by voice의 형태로 음성에 의존하여 수행되는데, 이를 voice by graphics 형태로 청각에 모든 걸 의지하지 않고 시각적으로 나타낼 수 있게 하고 싶었습니다. 또한 많은 AI 비서가 스마트폰과 스마트티브이 등 IoT 제품에 맞춰져 있고 Microsoft 사에서 제공하는 Cortana 같은 AI 비서는 한국에서는 서비스되지 않는 점을 고려하였을 때 한국형 데스크톱 기반의 인공지능 음성 비서는 개발할 만한 가치가 있다고 판단하였고 프로젝트에 착수하게 되었습니다.

### 2. 프로젝트 기대 효과
- 시각적인 효과를 사용자에게 제공하여 편의와 함께 업무를 보조하는 비서 기능을 구현함으로써, 능률을 향상시킬 수 있습니다.

### 3. 구현 기능
- 일상 음성 대화 속 호출어 인식
- 날씨 리뷰
- 음성 프로그램 제어
- 사용자와 모니터간 거리를 측정하여 웹 페이지 확대
- 제스처 PPT 제어
- TTS 목소리 커스터마이징

### 4. 개발 환경
- 사용 언어 - Python 3.7 ~ 3.8
- 코드 편집기 - Jupyter notebook, Colab
- 운영 체제 - Window

---

## 프로젝트 수행 절차(Execution Procedure)
1. [블록 다이어그램]
2. [음성 수집]
3. [소음 감소 필터]
4. [생체 인식]

### 1. 프로젝트 수행 절차 - 블록 다이어그램
![블록 다이어그램](https://user-images.githubusercontent.com/96413630/171382906-3aabcea5-41a6-4426-bc2c-8fb78b325e6b.png)

### 2. 프로젝트 수행 절차 - 음성 수집
![20220601_193425](https://user-images.githubusercontent.com/96413630/171385336-e9105f8e-659c-4a85-a19e-3941fbbab6ae.png)

#### (1) Info & Effect
- SpeechRecognition 라이브러리 사용
- 마이크 객체를 지정한 후 아날로그 음성 데이터를 수집
- 음성 수집시 필요에 따라 주파수(khz)를 sample rate로 설정함

#### (2) Procedure
![그림2](https://user-images.githubusercontent.com/96413630/171385759-3d66ad49-fe41-4f34-aa3b-2cf6b95b566d.png)

### 3. 프로젝트 수행 절차 - 소음 감소 필터
![20220601_193334](https://user-images.githubusercontent.com/96413630/171385200-65e121cb-14fa-4e87-b706-f52ab4970b34.png)

#### (1) Info & Effect
- None Stationary Noise Reduction 기법은 시간이 지남에 따라 잡음 게이트가 변경될 수 있음
- 신호가 발생하는 타임스케일을 알고 있는 경우 더 긴 타임스케일에서 발생하는 이벤트가 노이즈라는 가정을 기반으로 노이즈 임계값을 설정할 수 있음
- 이 알고리즘은 채널당 에너지 정규화(Per-Channel Energy Normalization)라고 하는 생체 음향학의 최근 방법에 의해 동기가 부여되었음

#### (2) Procedure
- 신호를 통해 스펙트로그램을 계산 → IIR 필터를 사용하여 시간 평활화된 스펙트럼 계산 → 스펙트로그램을 기반으로 마스크 생성 → 마스크가 신호의 스펙트로그램에 적용되고 변환

### 4. 프로젝트 수행 절차 - 생체 인식
![image](https://user-images.githubusercontent.com/96413630/171386559-12e83927-8ae5-4c82-bc92-70b628afe7a5.png)

#### (1) Info & Effect
- 생체 패턴을 파악하여 수집된 음성의 출처를 찾을 수 있음
- 사용자로 등록된 음성만 데스크탑을 제어할 수 있음

#### (2) Procedure
- 사용자 음성 3차례 입력 → 수집된 음성에 소음 감소 필터 적용 → 필터를 거친 음성 Stacking → 음성에 대해 Gaussian Mixture Model을 사용하여 학습 및 평가

### 5. 프로젝트 수행 절차 - 음성 유사도 비교
![image](https://user-images.githubusercontent.com/96413630/171390678-16e5deb2-1202-48d7-a76d-acfbb130f154.png)

#### (1) Info & Effect
- FastDTW 사용
- 음성 발생 시 유사도를 파악하여 생체 정보가 등록된  사용자의 음성만 수집하도록 함

#### (2) Procedure
- 사용자 음성 3차례 입력 → 수집된 음성에 소음 감소 필터 적용 → 필터를 거친 음성 Stacking → 음성에 대해 Gaussian Mixture Model을 사용하여 학습 및 평가
