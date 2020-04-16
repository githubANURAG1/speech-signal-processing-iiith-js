import librosa
import matplotlib.pyplot as plt
import scipy
import numpy as np

def create_lp_graph(file, order):

    file = str(file)
    audio_path = 'static/wav/audio' + file + '.wav'
    audio, sampling_rate = librosa.load(audio_path)

    lp_result = librosa.lpc(audio, order)
    ds = len(audio)
    y_result = scipy.signal.lfilter([0] + -1*lp_result[1:], [1], audio)
    plt.title("LP Log Spectrum")
    plt.magnitude_spectrum(y_result, Fs=1/ds, scale='dB', color='C1')
    plt.show()
    # Xf_mag = np.abs(np.fft.fft(y_result))
    # freqs = np.abs(np.fft.fftfreq(len(Xf_mag), d = 2/sampling_rate))

    # import matplotlib.pyplot as plt
    # plt.plot(freqs, Xf_mag)
    # plt.yscale("log")
    # plt.show()






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

plt = create_lp_graph(1,4)
#plt.show()

