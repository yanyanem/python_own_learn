# Import stuff

import numpy as np
import random
import itertools
import librosa

import matplotlib.pyplot as plt


def load_audio_file(file_path):
    data = librosa.core.load(file_path)[0]
    return data


def plot_time_series(data):
    fig = plt.figure(figsize=(14, 8))
    plt.title('Raw wave ')
    plt.ylabel('Amplitude')
    plt.plot(np.linspace(0, 1, len(data)), data)
    plt.show()


def test():
    data = load_audio_file("wantedWords_value_0-U01-1537605801978_44.wav")
    # plot_time_series(data)
    rate = 16000
    # Adding white noise
    wn = np.random.randn(len(data))
    data_wn = data + 0.005 * wn
    # plot_time_series(data_wn)
    librosa.output.write_wav('./a_0.wav', data_wn, rate)

    # Shifting the sound
    data_roll = np.roll(data, -200)
    # plot_time_series(data_roll)
    librosa.output.write_wav('./a_1.wav', data_roll, rate)

    # Stretch the sound
    data_stretch = librosa.effects.time_stretch(data, 1.1)
    # plot_time_series(data_stretch)
    librosa.output.write_wav('./a_2.wav', data_stretch, rate)


def changeOne(fPath, fName):
    print('starting...' + fName)
    data = load_audio_file(fPath + fName)
    # plot_time_series(data)
    rate = 16000

    # Adding white noise
    wn = np.random.randn(len(data))
    data_wn = data + 0.005 * wn
    # plot_time_series(data_wn)
    librosa.output.write_wav(fPath + fName + '.noise_0.wav', data_wn, rate)

    # Shifting the sound
    data_roll = np.roll(data, -100)
    # plot_time_series(data_roll)
    librosa.output.write_wav(fPath + fName + '.roll_0.wav', data_roll, rate)

    # Stretch the sound
    data_stretch = librosa.effects.time_stretch(data, 0.8)
    # plot_time_series(data_stretch)
    librosa.output.write_wav(fPath + fName + '.stretch_0.wav', data_stretch, rate)

    data_stretch = librosa.effects.time_stretch(data, 1.1)
    # plot_time_series(data_stretch)
    librosa.output.write_wav(fPath + fName + '.stretch_1.wav', data_stretch, rate)
    print('end...' + fName)


# test()


inWavPath = '/DataSet/ASR/36-0922-sj/train_wav_with_augment'
import os

list_of_files = {}
for (dirpath, dirnames, filenames) in os.walk(inWavPath):
    for filename in filenames:
        if filename.endswith('.wav'):
            list_of_files[filename] = os.sep.join([dirpath, ''])

for fName in list_of_files.keys():
    fPath = list_of_files.get(fName)
    changeOne(fPath, fName)

