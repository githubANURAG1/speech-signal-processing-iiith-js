from bokeh.plotting import figure, output_file, show
import librosa
from bokeh.models import *
import scipy
import numpy as np
from scipy.io import wavfile

def lp_residual(file, order):
    
    file = str(file)
    audio_path = 'wav/audio' + file + '.wav'
    audio, sampling_rate = librosa.core.load(audio_path)
    audio = librosa.core.to_mono(audio)
    output_file("graphs/impulse/impulse-wav"+file+"-order"+str(order)+".html")
    p = figure(plot_width=700, plot_height=300, x_axis_label='Time', y_axis_label="Magnitude")
    p.title = Title(text = 'Excitation')
    timefilter = [i for i in range(len(audio))]
    p.line(timefilter, audio, line_width = 2)
    
    show(p)

order = [1,3,5,8,10,12,14,16,18]
for i in range(1,5):
    for orders in order:
        lp_residual(i,orders)
