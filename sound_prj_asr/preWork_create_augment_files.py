

#inWavPath='/DataSet/ASR/36-0922-sj/train_wav/0_alading/'
inWavPath='/DataSet/ASR/36-0922-sj/train_wav/'
import os
#from audio_data_augmentation import changeOne_sj
from myWavProcessor3 import monoWavRead,augmentWrite

list_of_files = {}
for (dirpath, dirnames, filenames) in os.walk(inWavPath):
    for filename in filenames:
        if filename.endswith('.wav'):
            list_of_files[filename] = os.sep.join([dirpath, ''])

for fName in list_of_files.keys():
    fPath = list_of_files.get(fName)
    fromFolder = fPath
    toFolder=fromFolder.replace('train_wav','train_wav_with_augment_100')
    #print(fName,fromFolder,toFolder)
    #changeOne_sj(fPath,fName,toFolder)
    strFile = fromFolder+fName;
    samplefrequency, data = monoWavRead(strFile)
    augmentWrite(toFolder+fName+'_', samplefrequency, data, 100)



