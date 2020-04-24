

import librosa
import matplotlib.pyplot as plt
import scipy
import numpy as np
from bokeh.plotting import figure, output_file, save


#Input filename to input file. Ensure the filename path is correct and the ./graphs directory exists before executing 
#Gives pitch contour and log energy
def plotGraphs(audioFile):
    y, sr=librosa.load('wav/'+audioFile+'.wav')
   lp_result = librosa.lpc(y,10)
   y_result = scipy.signal.lfilter([0] + -1*lp_result[1:], [1], y)
   p = figure(plot_width=600, plot_height=300, x_axis_label='Time', y_axis_label="dB", title='Excitation')
   p.line(range(len(y)),y_result, line_width=2)
   save(p, filename='graphs/'+audioFile+'exc.html')
   intensity = [i*i for i in y]
   p = figure(plot_width=700, plot_height=300, x_axis_label='Time', y_axis_label="Amplitude", title='Log Energy')
   p.line(range(len(y)),np.log10(intensity), line_width=2)
   save(p, filename='graphs/'+audioFile+'log_energy.html')
    pitch=[]
    pitches, magnitudes = librosa.piptrack(y)
    for t in range(1,int(len(magnitudes[0]))):
        pitch.append(np.max(pitches[:,t]))
    p = figure(plot_width=700, plot_height=300, title='Pitch Contour')
    p.line(range(len(pitch)),pitch, line_width=2)
    save(p, filename='graphs/'+audioFile+'pitch.html')

    


# In[34]:


for i in range(1,5):
    plotGraphs('audio'+str(i))


# In[ ]:





# In[11]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




