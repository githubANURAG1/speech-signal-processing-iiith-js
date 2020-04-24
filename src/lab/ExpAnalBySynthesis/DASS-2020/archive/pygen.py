from bokeh.plotting import figure, output_file, show
import librosa
from bokeh.models import *
import scipy
import numpy as np
from scipy.io import wavfile

#Input filename and order to generate graph. Ensure ./graphs/lpresidual-wav is a folder before running
#Gives LP residual graph
def lp_residual(file, order):

    file = str(file)
    audio_path = 'wav/audio' + file + '.wav'
    audio, sampling_rate = librosa.load(audio_path)

    lp_result = librosa.lpc(audio, order)
    y_result = scipy.signal.lfilter([0] + -1*lp_result[1:], [1], audio)

    output_file("graphs/lpresidual-wav"+file+"-order"+str(order)+".html")
    p = figure(plot_width=700, plot_height=300, x_axis_label='Time', y_axis_label="Magnitude")
    p.title = Title(text = 'Excitation')
    timefilter = [i for i in range(len(audio))]
    p.line(timefilter, audio-y_result, line_width = 2)
    
    show(p)

#Input filename and order to generate graph. Ensure ./graphs/lpresidual-wav is a folder before running
#Gives lp impulse graph
def lp_impulse(file, order):
    
    file = str(file)
    audio_path = 'wav/audio' + file + '.wav'
    audio, sampling_rate = librosa.load(audio_path)

    lp_result = librosa.lpc(audio, order)
    y_result = scipy.signal.lfilter([0] + -1*lp_result[1:], [1], audio)

    output_file("graphs/lpresidual-wav"+file+"-order"+str(order)+".html")
    p = figure(plot_width=700, plot_height=300, x_axis_label='Time', y_axis_label="Magnitude")
    p.title = Title(text = 'Excitation')
    timefilter = [i for i in range(len(audio))]
    p.line(timefilter, audio-y_result, line_width = 2)
    
    show(p)

order = [1,3,5,8,10,12,14,16,18]
for i in range(1,5):
    for orders in order:
        lp_residual(i,orders)

