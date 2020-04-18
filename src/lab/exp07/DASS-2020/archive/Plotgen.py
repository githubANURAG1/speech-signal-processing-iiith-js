from bokeh.plotting import figure, output_file, show
import librosa
from bokeh.models import *
import scipy
import numpy as np
from scipy.io import wavfile
from cepstrum import *

def plot_gen(file,window_type):


    file = str(file)
    output_file("line-"+file+"-"+window_type+".html")

    p = figure(plot_width=550, plot_height=300, x_axis_label='Time', y_axis_label="Amplitude")
    p.title = Title(text = 'Windowed Waveform')
    
    audio, sample_rate = librosa.load('static/wav/audio'+file+'.wav')
    filter = librosa.filters.get_window(window_type, len(audio))
    windowed_output = audio * filter
    time_filter = [i for i in range(len(audio))]
    p.line(time_filter,windowed_output, line_width=2)
    

    show(p)


def create_stft(file, nfft):
    file = str(file)
    audio_path = 'static/wav/audio'+file+'.wav'
    audio, sampling_rate = librosa.load(audio_path)
    n = len(audio)
    T = nfft / sampling_rate
    yf = scipy.fft(audio)
    xf = np.linspace(0.0, 1.0/(2.0 * T), n/2)

    output_file("stft-wav"+file+"-nfft"+str(nfft)+".html")
    p = figure(plot_width=550, plot_height=300,y_axis_type="log", x_axis_label='Frequency', y_axis_label="Amplitude")
    p.title = Title(text = 'Log Spectrum')
    p.line(xf, 2.0/n * np.abs(yf[:n//2]), line_width=2)

    show(p)

def create_liftered(file):
    file = str(file)
    audio_path = 'static/wav/audio'+file+'.wav'
    audio, sampling_rate = librosa.load(audio_path)
    n = len(audio)
    T = 1 / sampling_rate
    yf = scipy.fft(audio)
    xf = np.linspace(0.0, 1.0/(2.0 * T), n/2)

    output_file("LifteredLog-wav"+file+".html")
    p = figure(plot_width=550, plot_height=300, y_axis_type="log", x_axis_label='Frequency', y_axis_label="Amplitude")
    p.title = Title(text='Liftered Log Spectrum')
    p.line(xf, 2.0/n * np.abs(yf[:n//2]), line_width=2)

    show(p)


def create_cepstrum(file):
    import numpy as np

    file = str(file)
    audio_path = 'static/wav/audio1'+'.wav'
    fs, signal = wavfile.read(audio_path)
    ceps = real_cepstrum(signal)
    print(ceps)
    samples = signal.shape[0]
    t = np.arange(samples)

    output_file("cepstrum-wav"+file+".html")

    p = figure(plot_width=550, plot_height=300, x_axis_label='Quefrency (samples)')
    p.title = Title(text='Cepstrum')
    p.line(t,ceps, line_width=2)

    show(p)

for i in range(1,3):
    for type in ['rectangular', 'hamming', 'hann', 'cosine']:
        plot_gen(i,type)
nfft_values = [64, 128, 256, 512, 1024, 2048, 4096, 8192]
for i in range(1,3):
    for value in nfft_values:
        create_stft(i, value)

for i in range(1,3):
    create_liftered(i)
    create_cepstrum(i)


