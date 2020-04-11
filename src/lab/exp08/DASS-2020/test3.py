import librosa
import matplotlib.pyplot as plt
import scipy
import numpy as np

def create_lp_graph(file, order):

    file = str(file)
    audio_path = 'static/wav/audio' + file + '.wav'
    audio, sampling_rate = librosa.load(audio_path)

    lp_result = librosa.lpc(audio, order)
    y_result = scipy.signal.lfilter([0] + -1*lp_result[1:], [1], audio)
    plt.title("LP Spectrum")
    plt.magnitude_spectrum(y_result, Fs=sampling_rate, color='C2')
    plt.show()


def create_lplog(file, order):
    file = str(file)
    audio_path = 'static/wav/audio' + file + '.wav'
    audio, sampling_rate = librosa.load(audio_path)

    lp_result = librosa.lpc(audio, order)
    y_result = scipy.signal.lfilter([0] + -1*lp_result[1:], [1], audio)

    plt.figure()
    plt.grid()
    plt.magnitude_spectrum(y_result, Fs=sampling_rate, color='blue')
    plt.title('LP Spectrum')
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.show()
    plt.savefig('static/images/lpresidual-wav'+file+'-order'+str(order)+'.png')



def create_lpresidual(file,order):
    file = str(file)
    audio_path = 'static/wav/audio' + file + '.wav'
    audio, sampling_rate = librosa.load(audio_path)

    lp_result = librosa.lpc(audio, order)
    y_result = scipy.signal.lfilter([0] + -1*lp_result[1:], [1], audio)

    plt.figure()
    plt.grid()
    plt.plot(audio-y_result)
    plt.xlabel("Frequency")
    plt.ylabel("Time")
    plt.title('LP Residual')
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.savefig('static/images/lpresidual-wav'+file+'-order'+str(order)+'.png')
    #plt.close()
    return plt

create_lplog(1,6)
#plt.show()

