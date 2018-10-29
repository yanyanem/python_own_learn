#encoding:utf-8

inFolder = 'C:\\00-Erics\\01-Current\\YuShi\\ML-KWS-for-MCU\\DataSet\\ASR\\36-0922-sj\\train_wav-v0.2\\'
outFolder_wav_trn = 'C:\\00-Erics\\04-git-dataset\\thchs30\\lm_dataset\\data\\'
outFolder_test_trn = 'C:\\00-Erics\\04-git-dataset\\thchs30\\lm_dataset\\test_trn\\'
words_txt = 'C:\\00-Erics\\04-git-dataset\\thchs30\\lm_dataset\\words.txt'
lexicon_txt = 'C:\\00-Erics\\04-git-dataset\\thchs30\\lm_dataset\\lexicon.txt'



def get_phone(wordsList):
    file_lexicon = open('./thchs30/lexicon.txt','r',encoding='utf8')
    f2_lines = file_lexicon.readlines()

    dict_lexicon = {}
    for line in f2_lines[0:]:
        line=line.replace('\n','').split(' ')
        try:
            v = dict_lexicon[line[0]]
            v.append(line)
        except KeyError:
            dict_lexicon[line[0]]=[line]

    dict_phone={}
    for w in wordsList:
        try:
            v = dict_lexicon[w][0][1:]
        except KeyError:
            v = []
            for c in w:
                v1 = dict_lexicon[c][0][1:]
                for t in v1:
                    v.append(t)
        dict_phone[w]=v
    return dict_phone

def writeFile(fileName,lineStrList):
    f_w = open(fileName,'wb')
    count=0
    for lineStr in lineStrList:
        count=count+1
        #print(count,len(lineStrList),lineStr)
        if count == len(lineStrList):
            f_w.write(bytes(lineStr,encoding='utf8'))
        else:
            f_w.write(bytes(lineStr+'\n',encoding='utf8'))
    f_w.close()

def gen_conf(wordsList):
    dict_phone = get_phone(wordsList)
    writeFile(words_txt,wordsList)
    lines=[]
    lines.append('# sil')
    lines.append('<SPOKEN_NOISE> sil')
    lines.append('SIL sil')
    for v in dict_phone:
        print(v,dict_phone[v])
        s=v
        for t in dict_phone[v]:
            s=s+' '+t
        lines.append(s)

    writeFile(lexicon_txt,lines)


def deal(no1,w,path1,phone1):
    print('deal:',no1, w, path1, phone1)
    inFolder1 = inFolder+path1
    list_of_files = {}
    import os
    from shutil import copyfile
    count = -1
    for (dirpath, dirnames, filenames) in os.walk(inFolder1):
        for filename in filenames:
            if filename.endswith('.wav'):
                count = count + 1
                filepath = os.sep.join([dirpath, filename])
                newFileName = 'S'+no1+'_'+str(count)+'.wav'
                outF_wav = outFolder_wav_trn+newFileName
                #print(filepath,outF_wav)
            try:
                copyfile(filepath, outF_wav)
                outF_wav_trn = outF_wav+'.trn'
                lines = [w]
                lines.append( ' '.join(phone1))
                lines.append(' '.join(phone1))
                writeFile(outF_wav_trn,lines)

                test_trn = outFolder_test_trn + newFileName+'.trn'
                lines = ['../data/'+ newFileName+'.trn']
                writeFile(test_trn,lines)

            except Exception as e:
                print(e)
                print('in copyfile exception:', filepath)



def gen_data(wordsList, dict_phone):
    from preWork_01 import readcsv
    csvList, csvListDict = readcsv()
    tempStrList = []
    for w in wordsList:
        for row in csvList:
            if w == row[1]:
                # print(row[0], ' ', row[1], ' ', row[2], ' ', csvListDict.get(row[0]),dict_phone[w] )
                no1 = row[0]
                path1 = csvListDict.get(row[0])
                phone1 = dict_phone[w]
                deal(no1, w, path1, phone1)
                tempStrList.append(no1+' '+w+' '+path1+' '+' '.join(phone1))

    writeFile('./log/preWork_thchs30_sj_test_files.log', tempStrList)


#wordsList = ['阿拉丁', '打开', '关闭', '变暗', '变亮', '红色', '白颜色', '最低亮度', '睡眠模式', '最高亮度']
wordsList = ['阿拉丁', '打开', '关闭', '变暗', '变亮', '红色', '白颜色', '最低亮度', '睡眠模式', '最高亮度']
dict_phone = get_phone(wordsList)
#print(dict_phone)

#gen_data(wordsList,dict_phone)


wordsList = ['阿拉丁', '打开', '红色', '白颜色', '最低亮度', '睡眠模式', '最高亮度','东宝','讯飞']
gen_conf(wordsList)

# ngram-count -text words.txt -order 3 -lm 3.lm
# cat decode.1.log | grep '^S'