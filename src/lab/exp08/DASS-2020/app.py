from flask import Flask, render_template, Response, send_file
import librosa
from scipy.io import wavfile
import matplotlib.pyplot as plt
import io
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

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
    fig = create_window_plot(type, file)
    return send_file('static/images/windowed-'+type+'-wav'+file+'.png', mimetype='image/gif')

# @app.route('/stft/<file>/<nfft>')
# def log_spectrum(file,nfft):
#     fig = create_stft(file,nfft)
#     return send_file('static/images/stft-wav'+file+'.png', mimetype='image/gif')



def create_window_plot(window_type, file):
    file = str(file)
    audio, sample_rate = librosa.load('static/wav/audio'+file+'.wav')
    filter = librosa.filters.get_window(window_type, len(audio))
    windowed_output = audio * filter
    plt.figure(figsize=(5, 2))
    plt.plot(windowed_output)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.savefig('static/images/windowed-'+window_type+'-wav'+file+'.png')
    return plt


# def create_stft(file, nfft):
#     print(nfft)
#     file = str(file)
#     audio, sample_rate = librosa.load('static/wav/audio'+file+'.wav')
#     output = np.abs(librosa.stft(audio, n_fft=int(nfft)))
#     output = librosa.amplitude_to_db(output)
#     plt.figure(figsize=(5, 2))
#     plt.plot(output)
#     plt.grid(color='grey', linestyle='--', linewidth=0.5)
#     plt.savefig('static/images/stft-wav'+file+'.png')
#     return plt

if __name__ == '__main__':
    app.run()
    create_window_plot("rectangular")
