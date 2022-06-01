#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


#!pip install h5py==2.10
#!pip install git+https://github.com/repodiac/german_transliterate


# In[2]:


#!pip install .


# In[3]:


#!git clone https://github.com/librosa/librosa.git
#!pip install -e librosa


# In[4]:


#!pip install pypinyin


# In[5]:


#!pip install g2p_en


# In[6]:


#!pip install pyopenjtalk


# In[7]:


#!pip install huggingface_hub


# In[58]:


def load_model():
    import tensorflow as tf
    import yaml
    import numpy as np
    import matplotlib.pyplot as plt
    import IPython.display as ipd
    from tensorflow_tts.inference import AutoConfig
    from tensorflow_tts.inference import TFAutoModel
    from tensorflow_tts.inference import AutoProcessor
    
    # tacotron2 text -> mel-spectrogram으로 바꿔주는 model
    tacotron2_config = AutoConfig.from_pretrained('examples/tacotron2/conf/tacotron2.kss.v1.yaml')
    tacotron2 = TFAutoModel.from_pretrained(
        config=tacotron2_config,
        pretrained_path="tacotron2/model-20000.h5", #tacotron2-100k.h5
        name="tacotron2"
    )
    
    # inference 시 attention graph의 alignment value(색깔, 음량의 세기)의 범위를 지정해준다
    # setup window for tacotron2 if you want to try
    tacotron2.setup_window(win_front=100, win_back=100)

    # Vocoder model (mel spectrogram -> audio)
    # 멜로디 생성 모델을 사용합니다.
    mb_melgan_config = AutoConfig.from_pretrained('examples/multiband_melgan/conf/multiband_melgan.v1.yaml')
    mb_melgan = TFAutoModel.from_pretrained(
        config=mb_melgan_config,
        pretrained_path="mb.melgan-1000k.h5", # mb.melgan-1000k.h5
        name="mb_melgan"
    )

    # input text를 inference시 숫자로 이뤄진 sequence로 변환할 때 필요합니다.
    processor = AutoProcessor.from_pretrained(pretrained_path="kss_mapper.json")
    
    return tacotron2,mb_melgan,processor


# In[2]:


# 직접 음성합성을 진행하는 함수입니다.
# text -> mel spectrogram model, vocoder model을 인자로 선택합니다.
def do_synthesis(input_text, text2mel_model, vocoder_model, text2mel_name, vocoder_name, processor):
    import tensorflow as tf
    import yaml
    import numpy as np
    import matplotlib.pyplot as plt
    import IPython.display as ipd
    from tensorflow_tts.inference import AutoConfig
    from tensorflow_tts.inference import TFAutoModel
    from tensorflow_tts.inference import AutoProcessor
    
    input_ids = processor.text_to_sequence(input_text)
    #print('input_ids = ', input_ids)
    # text2mel part
    if text2mel_name == "TACOTRON":
        i, mel_outputs, stop_token_prediction, alignment_history = text2mel_model.inference(
        tf.expand_dims(tf.convert_to_tensor(input_ids, dtype=tf.int32), 0),
        tf.convert_to_tensor([len(input_ids)], tf.int32),
        tf.convert_to_tensor([0], dtype=tf.int32)
        )
    #print('i = ', i)
    #print('mel_outputs = ', mel_outputs)
    #print('stop_token_prediction = ', stop_token_prediction)
    #print('alignment_history = ', alignment_history)
    else:
        raise ValueError("Only TACOTRON are supported on text2mel_name")

      # vocoder part
    if vocoder_name == "MB-MELGAN":
        audio = vocoder_model.inference(mel_outputs)[0, :, 0]
    else:
        raise ValueError("Only MB_MELGAN are supported on vocoder_name")

    # tacotron2 attention graph도 함께 반환합니다.
    if text2mel_name == "TACOTRON":
        return mel_outputs.numpy(), alignment_history.numpy(), audio.numpy()
    else:
        return mel_outputs.numpy(), audio.numpy()
    # attention 시각화해서 보여주는 함수입니다.
    # tacotron2 encoder와 decoder가 어떠한 mapping을 형성하는지 보여줍니다.
    
def visualize_attention(alignment_history):
    import matplotlib.pyplot as plt
    
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.set_title(f'Alignment steps')
    im = ax.imshow(
          alignment_history,
          aspect='auto',
          origin='lower',
          interpolation='none')
    fig.colorbar(im, ax=ax)
    xlabel = 'Encoder timestep'
    plt.xlabel(xlabel)
    plt.ylabel('Decoder timestep')
    plt.tight_layout()
    plt.show()
    plt.close()

def visualize_mel_spectrogram(mels):
    mels = tf.reshape(mels, [-1, 80]).numpy()
    fig = plt.figure(figsize=(10, 8))
    ax1 = fig.add_subplot(311)
    ax1.set_title(f'Predicted Mel-after-Spectrogram')
    im = ax1.imshow(np.rot90(mels), aspect='auto', interpolation='none')
    fig.colorbar(mappable=im, shrink=0.65, orientation='horizontal', ax=ax1)
    plt.show()
    plt.close()


# In[135]:


def tacotron2_sjh(input_text, tacotron2, mb_melgan, processor, idx):
    from IPython.display import Audio
    import soundfile as sf
    _, _, audios = do_synthesis(input_text, tacotron2, mb_melgan, "TACOTRON", "MB-MELGAN", processor)
    display(Audio(audios, rate=22050, autoplay=True))
    sf.write('tts_wav/stereo_file_' + str(idx) + '.wav', audios, 22050, 'PCM_24')


# In[130]:


tacotron2, mb_melgan, processor = load_model() #시간 걸림 모델 로드


# In[131]:


# 입력 문장이 들어가는 곳입니다. 
input_text = "맑습니다. 최저기온은 17도이며, 오늘 서초구 서초4동 날씨는 온도는 30도 입니다."
idx = "ppt"


# In[136]:


tacotron2_sjh(input_text, tacotron2, mb_melgan, processor, idx)

