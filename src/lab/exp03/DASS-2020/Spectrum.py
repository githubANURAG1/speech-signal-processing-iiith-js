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
    p = figure(plot_width=600, plot_height=300, x_axis_label='Time', y_axis_label="Amplitude", title="Autocorrelation")
    autoCorr = librosa.autocorrelate(y)
    p.line(time_filter, autoCorr)
    save(p, filename ='graphs/autocorr/'+audioFile+'autocorr.html')
    

    p = figure(plot_width=600, plot_height=300, x_axis_label="Sample Number", y_axis_label="Amplitude", title="LPC")
    lpc= librosa.lpc(y,10)
    lpc_x = range(len(lpc))
    p.line(lpc_x, lpc)
    save(p, filename = 'graphs/lpc/'+audioFile+'lpc.html')
    
    spf = wave.open("wav/"+audioFile+".wav", 'r') 
    x = spf.readframes(-1)
    x = numpy.fromstring(x, 'Int16')

    N = len(x)
    w = numpy.hamming(N)

    x1 = x * w
    x1 = lfilter([1], [1., 0.63], x1)

    rts = numpy.roots(lpc)
    rts = [r for r in rts if numpy.imag(r) >= 0]

    angz = numpy.arctan2(numpy.imag(rts), numpy.real(rts))

    Fs = spf.getframerate()
    frqs = sorted(angz * (Fs / (2 * math.pi)))
    fmin = 5
    fmax= 20000
    i_min = sr/fmax
    i_max = sr/fmin
    autoCorr[:int(i_min)] = 0
    autoCorr[int(i_max):] = 0
    i = autoCorr.argmax()
    f0 = float(sr)/i
    freqFile=open('freqFile.txt', "a")
    freqFile.write(str(frqs)+" "+str(f0)+"\n")
    freqFile.close()
    return frqs, f0



os.remove('freqFile.txt')
for i in range(1,5):
    createSpectAutoCorr('ex'+str(i))

