
from preWork_01 import cutWavFile

fromPath = "C:\\00-Erics\\01-Current\\YuShi\\ML-KWS-for-MCU\\DataSet\\ASR\\36-0922-sj\\train_wav_1_origin\\sj\\wav_all\\"
toPath = "C:\\00-Erics\\01-Current\\YuShi\\ML-KWS-for-MCU\\DataSet\\ASR\\36-0922-sj\\train_wav_1_origin\\sj\\wav_all_cut\\"

import os
for fileName in os.listdir(fromPath):
    inFile=os.path.join(fromPath, fileName)
    outFile=os.path.join(toPath, fileName)
    cutWavFile(inFile,outFile)











