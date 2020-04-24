#!/usr/bin/env python
# coding: utf-8

# In[1]:


import librosa
import numpy
import scipy
import matplotlib.pyplot as plt
import soundfile as sf


# In[ ]:





# In[26]:





# In[31]:





# In[ ]:





# In[2]:


def changeBit( audioFile,bits=8, samplerate=16000 ):
    formatBit = "PCM_" + str(bits)
    y,sr = librosa.load('wav/'+audioFile+'.wav', sr=samplerate)
    sf.write('wav/'+audioFile+ str(bits)+str(int(samplerate/1000))+'.wav', y, samplerate, subtype='PCM_'+str(bits))
    


# In[4]:


for i in range(1,5):
    aud = 'ex'+str(i)
    for bits in ['16','24']:
        for samp in [16000,8000,4000,2000,1000]:
            changeBit(aud, bits, samp)


# In[ ]:





# In[ ]:




