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

def stft(file, nfft):
    print(nfft)
    file = str(file)
    audio, sample_rate = librosa.load('static/wav/audio'+file+'.wav')
    output = np.abs(librosa.stft(audio,n_fft = len(audio)*2))
    output = librosa.amplitude_to_db(output)
    plt.figure()
    plt.plot(output)
    plt.savefig('static/images/stft-wav'+file+'.png')
    return plt

#plot = create_window_plot("hann", 1)
#plot.show()
plot = stft(1,65536)

