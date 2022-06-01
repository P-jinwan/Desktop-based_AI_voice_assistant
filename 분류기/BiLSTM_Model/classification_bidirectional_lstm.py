#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from konlpy.tag import Mecab

def classification_bidirectional_lstm(text, src_tokenizer, tar_tokenizer, max_len, model, index_to_word, index_to_tag) :
    def tokenize(samples):
        tokenizer = Tokenizer(oov_token="O")
        tokenizer.fit_on_texts(samples)
        return tokenizer
    
    # mecab 객체 생성
    mecab = Mecab(dicpath = r"C:\mecab\mecab-ko-dic")

    text = text.replace(" ", "_")

    morpheme = mecab.morphs(text)

    result_sen = []
    result_tag = []

    for i in range(len(morpheme)) :
        sample = src_tokenizer.texts_to_sequences(morpheme)
        sample = pad_sequences(sample, padding= 'post', maxlen=max_len)


        y_predicted = model.predict(np.array([sample[i]]))
        y_predicted = np.argmax(y_predicted, axis= -1)

        for word, pred in zip(sample[i], y_predicted[0]):
            if word != 0:
                result_sen.append(index_to_word[word])
                result_tag.append(index_to_tag[pred].upper())
    
    return result_sen, result_tag




