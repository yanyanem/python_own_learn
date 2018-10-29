
def readcsv():
    result=[]
    resultDict={}
    import csv
    #csvFile = "C:\\00-Erics\\01-Current\\YuShi\\ML-KWS-for-MCU\\DataSet\\ASR\\36-0922-sj\\mapping.csv"
    csvFile = "./conf/mapping.csv"
    with open(csvFile, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            # print(', '.join(row))
            result.append(row)
            resultDict[row[0]]=row[0]+'_'+row[2]
    return result,resultDict

def test_readcsv():
    csvList, csvListDict = readcsv()
    tempStr = ''
    for row in csvList:
        print(row[0], ' ', row[1], ' ', row[2], ' ', csvListDict.get(row[0]))
        # os.mkdir(outWavPath+row[0]+'_'+row[2])
        #tempStr = tempStr + csvListDict.get(row[0]) + ','
        #print(tempStr)

#test_readcsv()

def connectWavFile(inFile,outFile):
    from pydub import AudioSegment
    song = AudioSegment.from_wav(inFile)
    newSong = song+song
    newSong.export(outFile, format="wav")

def test_connectWavFile():
    wavInFile = "./SoundIn/ch-sj-01_dakai.wav"
    wavOutFile = "./SoundOut/connectWavFile.wav"
    connectWavFile(wavInFile, wavOutFile)

#test_connectWavFile()

def cutWavFile(inFile,outFile):
    from pydub import AudioSegment
    song = AudioSegment.from_wav(inFile)
    print(inFile,song.channels)
    newSong = song[-1000:]
    newSong.export(outFile, format="wav")

def test_cutWavFile():
    wavInFile = "ch-sj-01_dakai.wav"
    wavOutFile = "newSong.wav"
    cutWavFile(wavInFile, wavOutFile)

#test_cutWavFile()

def createFolderFor36(dirPath):
    import os
    csvList, csvListDict = readcsv()
    for row in csvList:
        folderName=csvListDict.get(row[0])
        createFolder = dirPath+folderName
        if not os.path.exists(createFolder) :
            os.mkdir(createFolder)
            print('Created:'+createFolder)

def test_createFolderFor_en():
    import os
    dirPath='C:\\00-Erics\\04-git-dataset\\ML-KWS-for-MCU\\speech_commands.v0.02-2s\\'
    dirNames = 'backward,bed,bird,cat,dog,down,eight,five,follow,forward,four,go,happy,house,learn,left,marvin,nine,no,off,on,one,right,seven,sheila,six,stop,three,tree,two,up,visual,wow,yes,zero'
    for dirName in dirNames.split(','):
        os.mkdir(os.sep.join([dirPath,dirName]))

#test_createFolderFor_en()

def test_createFolderFor36():
    dirPath='C:\\00-Erics\\01-Current\\YuShi\\ML-KWS-for-MCU\\DataSet\\ASR\\36-0922-sj\\train_wav_1\\'
    createFolderFor36(dirPath)

#test_createFolderFor36()


def stat_person_sound(dirPath):
    import os
    import re
    from os.path import isfile, join
    #dirNames = 'backward,bed,bird,cat,dog,down,eight,five,follow,forward,four,go,happy,house,learn,left,marvin,nine,no,off,on,one,right,seven,sheila,six,stop,three,tree,two,up,visual,wow,yes,zero'
    dirNames = [d for d in os.listdir(dirPath) if not isfile(join(dirPath,d))]
    map_dirNames={}
    for dirName in dirNames:
        #print (dirName)
        list_fileNames=[]
        for (dirpath, dirnames, filenames) in os.walk(dirPath+dirName):
            for filename in filenames:
                if filename.endswith('.wav'):
                    personName = re.sub(r'_nohash_.*$', '', filename)
                    wavFile = os.sep.join([dirpath, filename])
                    list_fileNames.append(personName)
                    #print(personName)
        map_dirNames[dirName]=[len(set(list_fileNames)),len(list_fileNames)]

    for key in map_dirNames.keys():
        print(key,map_dirNames[key])

def test_stat_person_sound():
    dirPath='C:\\00-Erics\\04-git-dataset\\ML-KWS-for-MCU\\speech_commands.v0.02\\'
    dirPath='C:\\00-Erics\\01-Current\\YuShi\\ML-KWS-for-MCU\\DataSet\\ASR\\36-0922-sj\\train_wav-v0.2\\'
    stat_person_sound(dirPath)

#test_stat_person_sound()
