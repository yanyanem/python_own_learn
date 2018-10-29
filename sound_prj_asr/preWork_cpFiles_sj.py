import os
from shutil import copyfile

from preWork_01 import readcsv,createFolderFor36

rootPath = "C:\\00-Erics\\01-Current\\YuShi\\ML-KWS-for-MCU\\DataSet\\ASR\\36-0922-sj\\"
inWavPath = rootPath + "train_wav_1_origin\\wav_all_cut_ok\\"
outWavPath = rootPath+"train_wav_1\\"

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
    key = fName.split('wantedWords_value_')[1].split('-')[0]
    outPath = outWavPath+csvListDict[key]+'\\'+fName;
    print(fPath,outPath)
    try:
        copyfile(fPath,outPath)
    except Exception as e:
        print(e)
        print('in exception:',fPath)




