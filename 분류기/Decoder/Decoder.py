#!/usr/bin/env python
# coding: utf-8

# In[1]:


def Decoder(input_text, input_token) :
    # 문장이 입력되면 각 토큰별로 딕셔너리에 저장합니다.
    token_dict = {'LOC': [], 'TIM': [], 'ACT': [], 'TAS': [], 'NUM': []}
    
    # 문장과 토큰의 마지막에 'O'토큰을 넣어 마지막 요소도 출력되도록 합니다.
    input_text.append('O')
    input_token.append('O')

    # 입력 데이터가 들어오면 각 토큰별로 단어를 넣습니다..
    L_text, T_text, A_text, S_text, N_text = '', '', '', '', '' # 각 토큰의 단어를 입력받을 임시 저장소 변수입니다.

    # 입력 텍스트 길이만큼 반복하며 같은 토큰의 단어는 하나로 묶고 딕셔너리에 토큰별로 저장합니다.
    for i in range(len(input_text)) :       # 입력 텍스트 길이만큼 반복합니다..
        if 'LOC' in input_token[i] :        # 입력 토큰의 i번째 요소가 'LOC'와 같다면
            L_text = L_text + input_text[i] # L_text 변수에 저장된 문자와 입력 텍스트의 i 번째 문자를 합칩니다.
        elif 'TIM' in input_token[i] :      # 입력 토큰의 i번째 요소가 'TIM'과 같다면
            T_text = T_text + input_text[i] # T_text 변수에 저장된 문자와 입력 텍스트의 i 번째 문자를 합칩니다.
        elif 'ACT' in input_token[i] :      # 입력 토큰의 i번째 요소가 'ACT'와 같다면
            A_text = A_text + input_text[i] # A_text 변수에 저장된 문자와 입력 텍스트의 i 번째 문자를 합칩니다.
        elif 'TAS' in input_token[i] :      # 입력 토큰의 i번째 요소가 'TAS'와 같다면
            S_text = S_text + input_text[i] # S_text 변수에 저장된 문자와 입력 텍스트의 i 번째 문자를 합칩니다.
        elif 'NUM' in input_token[i] :      # 입력 토큰의 i번째 요소가 'NUM'과 같다면
            N_text = N_text + input_text[i] # N_text 변수에 저장된 문자와 입력 텍스트의 i 번째 문자를 합칩니다.
            
        # 'O' 토큰이 나오면 모든 변수에 저장된 값을 딕셔너리에 넣고 초기화합니다.
        if input_token[i] == 'O' :           # 입력 토큰의 i 번째 토큰이 'O'와 같다면
            token_dict['LOC'].append(L_text) # token_dict 딕셔너리 'LOC' 키에 L_text 값으로 추가합니다.
            token_dict['TIM'].append(T_text) # token_dict 딕셔너리 'TIM' 키에 T_text 값으로 추가합니다.
            token_dict['ACT'].append(A_text) # token_dict 딕셔너리 'ACT' 키에 A_text 값으로 추가합니다.
            token_dict['TAS'].append(S_text) # token_dict 딕셔너리 'TAS' 키에 S_text 값으로 추가합니다.
            token_dict['NUM'].append(N_text) # token_dict 딕셔너리 'NUM' 키에 N_text 값으로 추가합니다.
            L_text = ''                      # L_text 변수를 초기화 합니다.
            T_text = ''                      # T_text 변수를 초기화 합니다.
            A_text = ''                      # T_text 변수를 초기화 합니다.
            S_text = ''                      # T_text 변수를 초기화 합니다.
            N_text = ''                      # T_text 변수를 초기화 합니다.

    # 딕셔너리의 공백을 지우고 합칩니다.
    for key in token_dict.keys() :
        token_dict[key] = ' '.join(token_dict[key]).split()
        
    return token_dict