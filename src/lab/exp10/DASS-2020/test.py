import librosa
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import scipy
# y, sr = librosa.load('static/wav/audio1.wav')
# print(y)
# plt.plot(y)
# plt.show()
# filter = librosa.filters.get_window("hann",len(y))
# print(filter)
# output = y*filter
# plt.plot(output)
# plt.show()


def create_window_plot(window_type, file):
    file = str(file)
    audio, sample_rate = librosa.load('static/wav/audio'+file+'.wav')
    filter = librosa.filters.get_window(window_type, len(audio))
    windowed_output = audio * filter
    plt.figure()
    plt.plot(windowed_output)
    plt.savefig('static/images/windowed-'+window_type+'-wav'+file+'.png')
    return plt

def stft(file):
    file = str(file)
    audio, sample_rate = librosa.load('static/wav/audio'+file+'.wav')
    output = librosa.stft(audio)
    plt.figure(figsize=(5, 2))
    plt.magnitude_spectrum(output)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.savefig('static/images/stft-wav'+file+'-nfft'+str(nfft)+'.png')
    plt.close()
    return plt

def create_lp_log(file, order):
    file = str(file)
    audio, sample_rate = librosa.load('static/wav/audio'+file+'.wav')
    lp = librosa.lpc(audio, order)
    #y_hat = scipy.signal.lfilter([0] + -1*lp[1:], [1], audio)
    plt.figure()
    plt.plot(audio)
    #plt.yscale("log")
    plt.show()

#plot = create_window_plot("hann", 1)
#plot.show()
plot = stft(1)
plot.show()

#create_lp_log(2,8)
