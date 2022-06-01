#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://www.youtube.com/watch?v=udeQhZHx-00
def ppt_motion_action():
    
    #################### ▼패키지 임포트▼ ####################
    import cv2
    import pyautogui
    import mediapipe as mp
    import numpy as np
    import time
    import math
    #################### ▲패키지 임포트▲ ####################

    moveTo = 0 # 드래그 판단 변수
    past = 0 # 과거 시간 저장 변수
    flag = 0 # 과거 기준 시간 보다 일정시간이 지날 경우를 판단
    now = time.time_ns() # 현재 시간을 저장
    mode = 0
    
    pyautogui.PAUSE = 0.0001    # 딜레이 관련
    pyautogui.FAILSAFE = False  # 강제 초기화 비활성

    max_num_hands = 1 # 손 갯수

    actions = {0:'middle_Click', 3:'left_click', 1:'Move', 4:'back', 5:'full', 9:'right_click'}

    # MediaPipe hands model
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    hands = mp_hands.Hands(
        max_num_hands=max_num_hands,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5)

    # Gesture recognition model
    file = np.genfromtxt('시스템/Control_Gesture/data/gesture_train.csv', delimiter=',')
    angle = file[:,:-1].astype(np.float32)
    label = file[:, -1].astype(np.float32)
    knn = cv2.ml.KNearest_create()
    knn.train(angle, cv2.ml.ROW_SAMPLE, label)

    screenWidth, screenHeight = pyautogui.size()
    print(f'모니터 사이즈 : {screenWidth}, {screenHeight}')

    last_x = 0
    last_y = 0
    
    cap = cv2.VideoCapture(0)
    start = time.time()
    
    
    
    while True :
        ret, img = cap.read()
    
        if time.time() - start >= 2: # 1초 버튼이 동시에 여러번 눌리는 것을 방지
            start = time.time()
            flag = 1

        ret, img = cap.read()
        if not ret:
            continue

        img = cv2.flip(img, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        result = hands.process(img)

        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        if result.multi_hand_landmarks is not None:
            for res in result.multi_hand_landmarks:
                joint = np.zeros((21, 3))
                for j, lm in enumerate(res.landmark):
                    joint[j] = [lm.x, lm.y, lm.z]

                # Compute angles between joints
                v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19],:] # Parent joint
                v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],:] # Child joint
                v = v2 - v1 # [20,3]
                # Normalize v
                v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

                # Get angle using arcos of dot product
                angle = np.arccos(np.einsum('nt,nt->n',
                    v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
                    v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]

                angle = np.degrees(angle) # Convert radian to degree

                # Inference gesture
                data = np.array([angle], dtype=np.float32)
                ret, results, neighbours, dist = knn.findNearest(data, 3)
                idx = int(results[0][0])

                # Draw gesture result
                if idx in actions.keys():
                    cv2.putText(img, text=actions[idx].upper(), 
                                org=(int(res.landmark[0].x * img.shape[1]), 
                                     int(res.landmark[0].y * img.shape[0] + 20))
                                , fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, 
                                color=(255, 255, 255), thickness=2)

                    if idx == 1:
                        print(mode)
                        if mode != 1:
                            pyautogui.mouseDown(button='right')
                            pyautogui.hotkey('O', 'L')
                            mode = 1
                        
                        distance1 = joint[[8],:]
                        distance2 = joint[[4],:]
                        distance = int(math.sqrt(math.pow(distance1[0][0] - distance2[0][0], 2) + math.pow(distance1[0][1] - distance2[0][1], 2))*1000)
                        x = int(distance1[0][0] * screenWidth*1.7)-300# 1920, 1080
                        y = int(distance1[0][1] * screenHeight*2.5)-200# 손인식에 맞게 조정
                        pyautogui.moveTo(x, y)

                    elif idx == 5:
                        if mode == 1:
                            pyautogui.hotkey('esc')
                            mode = 5
                            
                        if flag == 1:
                            distance_0 = joint[[0],:]
                            distance_12 = joint[[12],:]
                            distance_0_12 = distance_0[0][0] - distance_12[0][0]
                            if distance_0_12 > 0.1:
                                pyautogui.hotkey('left')
                            elif distance_0_12 < -0.1:
                                pyautogui.hotkey('right')
                            flag = 0;
                            
                #mp_drawing.draw_landmarks(img, res, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('mouse', img)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

