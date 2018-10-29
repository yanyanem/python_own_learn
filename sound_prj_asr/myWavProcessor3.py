import random
import numpy as np
from scipy.io.wavfile import read,write
import math

import matplotlib
import matplotlib.pyplot as plt

def plotWav(ds): 
   plt.plot(range(len(ds)), ds) 
   plt.show()  
  
   return 

def shift(xs, n):
    if n >= 0:
        return np.r_[np.full(n, 0, dtype=np.int16), xs[:-n]]
    else:
        return np.r_[xs[-n:], np.full(-n, 0, dtype=np.int16)]
 
def speedx(iData, factor):        
    indices = np.round( np.arange(0, len(iData), factor) )
    indices = indices[indices < len(iData)].astype(int)
    if factor > 1:
       fillLen = int(round(len(iData) * (factor -1)))
       return np.r_[iData[ indices.astype(int) ], np.full(fillLen, 0, dtype=np.int16)]
    else:
       newData = []
       ratio = 1 - factor
       tempArray = np.random.random(len(iData))
       
       for i in range(len(iData)):
           if tempArray[i] < ratio:
               newData.append(iData[i])
               newData.append(iData[i])
           else:
               newData.append(iData[i])            
       return np.asarray(newData[0:len(iData)],np.int16)

#For reading wav files in mono
def monoWavRead(filename):
    fs, x = read(filename=filename)
    print("read file:", filename)
    #print("x.ndim:", x.ndim)
    if (x.ndim==1):
        samples = x
    else:
        samples = x[:, 0]
    return fs, samples

def augmentWrite(folder, sampleRate, iData, nCopy):
    nThreshold = 32767 * 0.02
    nLen = len(iData)
    
    #determine the start/end position
    nStart, nEnd = 0, nLen -1
    for i in range(nLen):
        if abs(iData[i]) > nThreshold:
            nStart = i
            break
    for i in range(nLen):
        if abs(iData[nLen -1 - i]) > nThreshold:
            nEnd = nLen -1 - i
            break
        
    nAmplitude = np.max(abs(iData))
    
    pitch_high = 1.25
    pitch_low = 0.75
    pitch_array = np.arange(pitch_low, pitch_high, (pitch_high - pitch_low)/(nCopy - 1e-9))
    
    nLeft, nRight = -nStart, nLen - nEnd
    try:
        shift_array = np.random.randint(nLeft, int(nRight/pitch_high), nCopy)
    except ValueError as ve:
        print('ValueError:',ve)
        print('folder:',folder)
        print('nStart, nEnd, nAmplitude:', nStart, nEnd, nAmplitude)
        print('nLeft, nRight, pitch_high,int(nRight/pitch_high):', nLeft, nRight,pitch_high,int(nRight/pitch_high))
        #print('shift_array:', shift_array)
        #print('amp_array:', amp_array)
        print('pitch_array:', pitch_array)
        return
    
    ampMin = 0.3
    ampMax = 32768/nAmplitude
    amp_array = ampMin + (ampMax - ampMin) * np.random.random_sample(nCopy)
    


    for i in range(nCopy):
       newData = speedx(iData, pitch_array[i])
       #plotWav(newData)
       newData = shift(newData, shift_array[i])
       #plotWav(newData)
       newData = np.round(newData * amp_array[i])       
       #print(newData.dtype)
       newData = np.asarray(newData, np.int16) #important !!!!!
       #print(newData.dtype)       
       #plotWav(newData)
       
       newFileName = folder + 'sh' + str(shift_array[i]) \
          + '_am' + str(int(amp_array[i] * 100))  \
          + '_pi'+ str(round(pitch_array[i],1)) + '.wav' 
       #print ('newFileName:', newFileName)
       write(newFileName, sampleRate, newData)
           
def test():

    fromFolder = '/DataSet/ASR/modified_from_mao.1s/dakai/'
    toFolder = '/DataSet/ASR/augmentTest/'
    strFile = fromFolder + 'ch-sj-01_dakai.wav'
    samplefrequency, data = monoWavRead(strFile)
    print("samplefrequency:", samplefrequency)
    print("len(data)", len(data))
    print("data:", data)
    print("data[:-2]", data[:-2])
    print("data[2:]", data[2:])

    print("min(data):", np.min(data))
    print("max(data):", np.max(data))
    print("avg(data):", np.average(data))
    print("std(data):", np.std(data))

    #fft_data = np.fft.fft(data)
    #fft_data = fft_data[0:len(fft_data)/2]
    augmentWrite(toFolder, samplefrequency, data, 3)

    #plotWav(data)

    #plotWav(fft_data)

