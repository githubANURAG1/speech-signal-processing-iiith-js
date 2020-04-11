from flask import Flask, render_template, Response, send_file
import librosa
from scipy.io import wavfile
import matplotlib.pyplot as plt
import io
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from os import path
import scipy
from time import sleep

app = Flask(__name__)

@app.route('/objective')
def Objectives():
    return render_template('Objective.html')

@app.route('/procedure')
def Procedure():
    return render_template('Procedure.html')


@app.route('/experiment')
def Experiment():
    return render_template('Experiment.html')


@app.route('/observations')
def Observations():
    return render_template('Observations.html')


@app.route('/references')
def References():
    return render_template('References.html')


@app.route('/feedback')
def Feedback():
    return render_template('Feedback.html')

@app.route('/tutorial')
def Tutorial():
    return render_template('Tutorial.html')

@app.route('/assessment')
def Assesment():
    return render_template('Assessment.html')

@app.route('/windowed/<file>/<type>')
def windowed_waveform(type, file):
    if(path.exists('static/images/windowed-'+type+'-wav'+file+'.png') is False) :
        fig = create_window_plot(type, file)

    return send_file('static/images/windowed-'+type+'-wav'+file+'.png', mimetype='image/gif')

@app.route('/stft/<file>/<nfft>')
def log_spectrum(file,nfft):
    if(path.exists('static/images/stft-wav'+file+'-nfft'+nfft+'.png') is False):
        fig = create_stft(file,int(nfft))

    return send_file('static/images/stft-wav'+file+'-nfft'+nfft+'.png', mimetype='image/gif')

@app.route('/lpresidual/<file>/<order>')
def lpresidual_spectrum(file, order):
    if(path.exists('static/images/lpresidual-wav'+file+'-order'+str(order)+'.png') is False):
        fig = create_lpresidual(file,int(order))

    return send_file('static/images/lpresidual-wav'+file+'-order'+str(order)+'.png', mimetype='image/gif')


@app.route('/lpspectrum/<file>/<order>')
def lp_spectrum(file, order):
    if(path.exists('static/images/lpspectrum-wav'+file+'-order'+str(order)+'.png') is False):
        fig = create_lpspectrum(file, int(order))

    return send_file('static/images/lpspectrum-wav'+file+'-order'+str(order)+'.png', mimetype='image/gif')


def create_window_plot(window_type, file):
    file = str(file)
    audio, sample_rate = librosa.load('static/wav/audio'+file+'.wav')
    filter = librosa.filters.get_window(window_type, len(audio))
    windowed_output = audio * filter
    #plt.figure(figsize=(5, 2))
    plt.plot(windowed_output)
    plt.title("Windowed Waveform")
    plt.xlabel("Time")
    plt.ylabel("Magnitude")
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.savefig('static/images/windowed-'+window_type+'-wav'+file+'.png')
    plt.close()
    return plt


def create_stft(file, nfft):
    file = str(file)
    audio_path = 'static/wav/audio' + file + '.wav'
    audio, sampling_rate = librosa.load(audio_path)
    n = len(audio)
    T = nfft / sampling_rate
    yf = scipy.fft(audio)
    xf = np.linspace(0.0, 1.0/(2.0 * T), n/2)
    fig, ax = plt.subplots()
    ax.plot(xf, 2.0/n * np.abs(yf[:n//2]))
    plt.grid()
    plt.title("Log Spectrum")
    plt.yscale("log")
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.savefig('static/images/stft-wav'+file+'-nfft'+str(nfft)+'.png')
    plt.close()
    return plt


def create_lpresidual(file, order):
    file = str(file)
    audio_path = 'static/wav/audio' + file + '.wav'
    audio, sampling_rate = librosa.load(audio_path)

    lp_result = librosa.lpc(audio, order)
    y_result = scipy.signal.lfilter([0] + -1*lp_result[1:], [1], audio)

    plt.figure()
    plt.grid()
    plt.plot(audio-y_result)
    plt.xlabel("Time")
    plt.ylabel("Magnitude")
    plt.title('LP Residual')
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.savefig('static/images/lpresidual-wav'+file+'-order'+str(order)+'.png')
    plt.close()
    return plt

def create_lpspectrum(file, order):
    file = str(file)
    audio_path = 'static/wav/audio' + file + '.wav'
    audio, sampling_rate = librosa.load(audio_path)

    lp_result = librosa.lpc(audio, order)
    y_result = scipy.signal.lfilter([0] + -1*lp_result[1:], [1], audio)

    plt.figure()
    plt.grid()
    plt.magnitude_spectrum(y_result, Fs=sampling_rate, color="blue")
    plt.title('LP Spectrum')
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.savefig('static/images/lpspectrum-wav'+file+'-order'+str(order)+'.png')
    plt.close()
    return plt

if __name__ == '__main__':
    type = ['rectangular','hamming','hann','cosine']

    for file in range(1,3):
        for option in type:
            create_window_plot(option,file)

    nfft_values = [64,128,256,512,1024,2048, 4096,8192]

    for file in range(1,3):
        for nfft in nfft_values:
            create_stft(file, nfft)

    app.run()

    orders = [1,2,4,6,8,10,12,16,20,24,30,40]

    for file in range(1,3):
        for order in orders:
            create_lpresidual(file, order)
            create_lpspectrum(file, order)
    

