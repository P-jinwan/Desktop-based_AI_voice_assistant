#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 화면에서 얼굴까지의 거리를 측정하는 함수입니다.
def MonitorControl() :
    #################### ▼패키지 임포트▼ ####################
    import pyautogui as pag
    import dlib, cv2, math, time, os
    #################### ▲패키지 임포트▲ ####################
    
    ######################### ▼함수▼ ##########################
    # 거리에 따라 화면의 페이지의 배율을 확대/축소하는 함수입니다.
    def Zoom(num, last_num) :
        # 모니터와 얼굴의 거리를 계산합니다.
        dist_m_f = num - last_num # 현재 거리에서 이전 거리 값을 빼 모니터와 얼굴의 거리를 계산합니다.

        # 계산된 거리를 기반으로 화면 확대/축소를 진행합니다.
        if dist_m_f > 0 :
            for i in range(last_num, num + 1) : 
                pag.hotkey('ctrl', '+') # ctrl+-        
        elif dist_m_f < 0 :
            for i in range(num, last_num + 1) :
                pag.hotkey('ctrl', '-') # ctrl++
    ######################### ▲함수▲ ##########################
    
    # 얼굴의 랜드마크 정보를 가져옵니다. (무조건 메인 코드와 같은 경로에 위치해야함)
    sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    
    # 객체를 생성하고 영상을 수집합니다.
    detector = dlib.get_frontal_face_detector() # dlib의 얼굴 검출기 객체 detector를 생성합니다.
    cam = cv2.VideoCapture(0)                   # 카메라로 실시간 영상을 받습니다.

    count = 0 
    last_num = 0
    num = 0
    
    while True :
        img, frame = cam.read()
        face = detector(frame)

        for f in face :
            #dlib으로 얼굴 검출
            cv2.rectangle(frame, (f.left(), f.top()), (f.right(), f.bottom()), (0, 0, 255), 2)

            land = sp(frame, f)
            land_list = []

            for l in land.parts() :
                land_list.append([l.x, l.y])
                cv2.circle(frame, (l.x, l.y), 3, (255, 0, 0), -1)
            result = math.sqrt(math.pow(land_list[36][0] - land_list[45][0], 2) + math.pow(land_list[36][1] - land_list[45][1], 2))
            result = int((result / 220) * 100)

            if 70 < result :   #3
                num = 3
            elif 60 < result < 67 : #2
                num = 2
            elif 50 < result < 57 : #1
                num = 1
            elif 40 < result < 48 : #0
                num = 0
            elif 30 < result < 38 : #-1
                num = -1
            elif 25 < result < 29 : #-2
                num = -2
            elif 20 < result < 24 : #-3
                num = -3
            elif 15 < result < 19 : #-4
                num = -4
            elif 10 < result < 14 : #-5
                num = -5

            print(result, num, last_num)

            Zoom(num, last_num)

            last_num = num

        cv2.imshow('A', frame)
        if cv2.waitKey(1) == ord('q') :
            break

    cam.release()

    cv2.destroyAllWindows()