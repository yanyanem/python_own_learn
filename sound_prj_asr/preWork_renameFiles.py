


from preWork_01 import readcsv,createFolderFor36
import os

rootPath = "C:\\00-Erics\\01-Current\\YuShi\\ML-KWS-for-MCU\\DataSet\\ASR\\36-0922-sj\\"

trainWavPath = rootPath + "train_wav\\"
testWavPath = rootPath+"test_wav\\"


#createFolderFor36(trainWavPath_new)

def rename(inWavPath):
    nameDict = {}
    for (dirpath, dirnames, filenames) in os.walk(inWavPath):
        for filename in filenames:
            if filename.endswith('.wav'):
                if filename.find('wantedWords_value'):
                    userName = filename.split('_')[4].split('.')[0]
                    userName_new = userName
                else:
                    userName = filename.split('wantedWords_value_')[1].split('-')[1]
                    userName_new = userName
                    if userName == '1537612909': userName_new = 'SunJin'
                    if userName == '1537616012': userName_new = 'TuMeiHong'
                    if userName == '1537841273': userName_new = 'LingHaiQing'
                    if userName == 'SJ': userName_new = 'SunJin'
                    if userName == 'U01': userName_new = 'SunQinShan'
                    if userName == 'U02': userName_new = 'ZhuYanFang'
                    if userName == 'U03': userName_new = 'SunYongXin'

                #userName_new = userName_new.replace(' ','')
                oldName = os.sep.join([dirpath, filename])
                try:
                    no = nameDict[userName_new]
                except KeyError:
                    no = 0

                nameDict[userName_new]=no+1
                newName = os.sep.join([dirpath, userName_new+'_nohash_'+str(no)+'.wav'])
                print(oldName,newName)
                os.rename(oldName,newName)


def rename01(trainWavPath):
    for (dirpath) in os.listdir(trainWavPath):
        rename(trainWavPath+dirpath)

#rename01(trainWavPath)
rename01(testWavPath)