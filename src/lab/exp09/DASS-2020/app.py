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
from audiolazy import (sHz, maverage, rint, AudioIO, ControlStream,
                       CascadeFilter, resonator, saw_table, chunks)
from time import sleep
import sys
from tkinter import *        
formants ={
    "i": [240, 2400],
    "y": [235, 2100],
    "e": [390, 2300],
    "ø": [370, 1900],
    "ɛ": [610, 1900],
    "œ": [585, 1710],
    "a": [850, 1610],
    "æ": [820, 1530],
    "ɑ": [750, 940],
    "ɒ": [700, 760],
    "ʌ": [600, 1170],
    "ɔ": [500, 700],
    "ɤ": [460, 1310],
    "o": [360, 640],
    "ɯ": [300, 1390],
    "u": [250, 595],
    }

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


@app.route('/add')
def call():


	vowels=['a','e','i','y','ø','ɛ','æ','ɑ','ɒ','ʌ','ɔ','ɤ','ɯ','u']
	
	formants = {
    "i": [240, 2400],
    "y": [235, 2100],
    "e": [390, 2300],
    "ø": [370, 1900],
    "ɛ": [610, 1900],
    "œ": [585, 1710],
    "a": [850, 1610],
    "æ": [820, 1530],
    "ɑ": [750, 940],
    "ɒ": [700, 760],
    "ʌ": [600, 1170],
    "ɔ": [500, 700],
    "ɤ": [460, 1310],
    "o": [360, 640],
    "ɯ": [300, 1390],
    "u": [250, 595],
    }

	#for me in vowels:
	root=Tk()
	Button(root, text = 'a') #,command=call_me(vowels[0],390,2300))
	Button(root, text = 'e') #,command=call_me(vowels[1],390,2300))
	
@app.route('/addnumber')
def call_me(vowels,a,b):    

	# Initialization
    rate = 44100
    s, Hz = sHz(rate)
    inertia_dur = .5 * s
    inertia_filter = maverage(rint(inertia_dur))

    api = sys.argv[1] if sys.argv[1:] else None # Choose API via command-line
    chunks.size = 1 if api == "jack" else 16

    with AudioIO(api=api) as player:
        first_coeffs = formants[vowels[0]]

        # These are signals to be changed during the synthesis
        f1 = ControlStream(first_coeffs[0] * Hz)
        f2 = ControlStream(first_coeffs[1] * Hz)
        gain = ControlStream(0) # For fading in

        # Creates the playing signal
        filt = CascadeFilter([
            resonator.z_exp(inertia_filter(f1).skip(inertia_dur), 400 * Hz),
            resonator.z_exp(inertia_filter(f2).skip(inertia_dur), 2000 * Hz),
        ])
        sig = filt((saw_table)(100 * Hz)) * inertia_filter(gain)

        th = player.play(sig)
        for vowel in vowels:
            #coeffs = formants[vowel]
            print("Now playing: ", vowel,a,b)
            f1.value = a * Hz
            f2.value = b * Hz
            gain.value = 1 # Fade in the first vowel, changes nothing afterwards
            sleep(2)

        # Fade out
        gain.value = 0
        sleep(inertia_dur / s + .2) # Divide by s because here it's already
                                    # expecting a value in seconds, and we don't
                                    # want ot give a value in a time-squaed unit
                                # like s ** 2
	



if __name__ == '__main__':

	#add()
	app.run()
	

