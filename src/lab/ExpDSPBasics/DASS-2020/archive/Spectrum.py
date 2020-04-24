
import librosa
import numpy
import scipy
import matplotlib.pyplot as plt
import soundfile as sf


#Input file, bitrate and samplerate. Ensure input path is correct. Ensure ./wav folder exists.
#Gives the changed file with given bitrate and samplerate 
def changeBit( audioFile,bits=8, samplerate=16000 ):
    formatBit = "PCM_" + str(bits)
    y,sr = librosa.load('wav/'+audioFile+'.wav', sr=samplerate)
    sf.write('wav/'+audioFile+ str(bits)+str(int(samplerate/1000))+'.wav', y, samplerate, subtype='PCM_'+str(bits))
    




for i in range(1,5):
    aud = 'ex'+str(i)
    for bits in ['16','24']:
        for samp in [16000,8000,4000,2000,1000]:
            changeBit(aud, bits, samp)



