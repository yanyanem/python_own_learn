import os

rootPath = "C:\\00-Erics\\01-Current\\YuShi\\ML-KWS-for-MCU\\DataSet\\ASR\\36-0922-sj\\"
inWavPath = rootPath + "wav\\"
newFolderPath = rootPath+"newFolder\\"

def cutWavFile(inFile,outFile):
    from pydub import AudioSegment
    song = AudioSegment.from_wav(inFile)
    newSong = song[-1000:]
    newSong.export(outFile, format="wav")

wavInFile = "ch-sj-01_dakai.wav"
wavOutFile = "newSong.wav"
cutWavFile(wavInFile,wavOutFile)

def readcsv():
    result=[]
    resultDict={}
    import csv
    csvFile = rootPath + "mapping.csv"
    with open(csvFile, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            # print(', '.join(row))
            result.append(row)
            resultDict[row[0]]=row[0]+'_'+row[2]
    return result,resultDict

csvList,csvListDict = readcsv()
tempStr=''
for row in csvList:
#    print(row[0],' ',row[1],' ',row[2])
#    os.mkdir(rootPath+'newFolder\\'+row[0]+'_'+row[2])
    print(csvListDict.get(row[0]))
    tempStr = tempStr+csvListDict.get(row[0])+','
print(tempStr)


list_of_files = {}
for (dirpath, dirnames, filenames) in os.walk(inWavPath):
    for filename in filenames:
        if filename.endswith('.wav'):
            list_of_files[filename] = os.sep.join([dirpath, filename])

for fName in list_of_files.keys():
    fPath = list_of_files.get(fName)
    key = fName.split('wantedWords_value_')[1].split('-')[0]
    outPath = newFolderPath+csvListDict[key]+'\\'+fName;
    #print(fPath,outPath)
    try:
        #cutWavFile(fPath,outPath)
        a=0
    except Exception as e:
        print(e)
        print('in exception:',fPath)








