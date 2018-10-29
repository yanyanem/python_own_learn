import os
from shutil import copyfile

from preWork_01 import readcsv,createFolderFor36

rootPath = "C:\\00-Erics\\01-Current\\YuShi\\ML-KWS-for-MCU\\DataSet\\ASR\\36-0922-sj\\"
inWavPath = rootPath + "train_wav_2_sr16k\\"
outWavPath = rootPath+"train_wav_2\\"

# first make dir
createFolderFor36(outWavPath)

csvList,csvListDict = readcsv()
for row in csvList:
    print(row[0],' ',row[1],' ',row[2],' ',csvListDict.get(row[0]))

list_of_files = {}
for (dirpath, dirnames, filenames) in os.walk(inWavPath):
    for filename in filenames:
        if filename.endswith('.wav'):
            list_of_files[filename] = os.sep.join([dirpath, filename])

for fName in list_of_files.keys():
    fPath = list_of_files.get(fName)
    key = fName.split('_')[3]
    tempPath=''
    for row in csvList:
        if key == row[1] :
            tempPath=csvListDict[row[0]]
    outPath = outWavPath+tempPath+'\\'+fName
    print(fPath,outPath)
    copyfile(fPath, outPath)





