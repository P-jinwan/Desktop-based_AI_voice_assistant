#!/usr/bin/env python
# coding: utf-8

# In[1]:

def classifier(text, src_tokenizer, tar_tokenizer, max_len, model, index_to_word, index_to_tag) :
    ########## 패키지 임포트 ##########
    from 분류기.BiLSTM_Model import classification_bidirectional_lstm as cbl
    from 분류기.Decoder import Decoder as dc
    ########## 패키지 임포트 ##########
    
    text, token = cbl.classification_bidirectional_lstm(text, src_tokenizer, tar_tokenizer, max_len, model, index_to_word, index_to_tag) # 입력 문장에 대해서 키워드 분류를 진행합니다.
    token_dict = dc.Decoder(text, token) # 텍스트와 토큰 데이터를 각 토큰별로 맞춰 딕셔너리 형태로 반환받습니다.
    
    return token_dict