import librosa
import math
import scipy
import matplotlib.pyplot as plt
import wave
import numpy
import sys
from scipy.signal import lfilter, hamming
from scipy.io import wavfile
import io
import os
from bokeh.plotting import figure, output_file, show, save


def createSpectAutoCorr(audioFile):
        
    y, sr = librosa.load("wav/"+audioFile+".wav")
    time_filter = [i for i in range(len(y))]

    output_file=('graphs/autocorr/'+audioFile+'autocorr.html')
    p = figure(plot_width=550, plot_height=300, x_axis_label='Time', y_axis_label="Amplitude", title="Autocorrelation")
    autoCorr = librosa.autocorrelate(y)
    p.line(time_filter, autoCorr)
    save(p, filename ='graphs/autocorr/'+audioFile+'autocorr.html')
    

    p = figure(plot_width=550, plot_height=300, x_axis_label="Sample Number", y_axis_label="Amplitude", title="LPC")
    lpc= librosa.lpc(y,10)
    lpc_x = range(len(lpc))
    p.line(lpc_x, lpc)
    save(p, filename = 'graphs/lpc/'+audioFile+'lpc.html')
    
    



for i in range(1,4):
	for j in range(1,4):
	    createSpectAutoCorr(str(i)+str(j))

