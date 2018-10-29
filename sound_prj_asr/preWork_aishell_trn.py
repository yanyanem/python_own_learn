#encoding:utf-8

# create trn for wzl keras lstm train
# in: aishell aishell_transcript_v0.8.txt lexicon.txt
# out: BAC009S0002W0122.wav.trn
# BAC009S0002W0122.wav.trn
# 打 开
# da3 kai1
# d a3 k ai1

import re


file_aishell_transcript = open('./aishell/aishell_transcript_v0.8.txt','r',encoding='utf8')
#file_aishell_transcript = open('./aishell/b.txt','r',encoding='utf8')
file_lexicon = open('./aishell/lexicon.txt','r',encoding='utf8')

f1_lines = file_aishell_transcript.readlines()
f2_lines = file_lexicon.readlines()

dict_lexicon = {}
for line in f2_lines[0:]:
    line=line.replace('\n','').split(' ')
    try:
        v = dict_lexicon[line[0]]
        v.append(line)
    except KeyError:
        dict_lexicon[line[0]]=[line]

count=0
len=len(f1_lines)
for line in f1_lines[0:5]:
    line=line.replace('\n','').strip()
    line=re.split(r" +",str(line))
    # print(line)
    new_line = [line[0]]
    line1Str=''
    line2Str=''
    line3Str=''
    for w in line[1:]:
        line1Str=line1Str+w+' '
        try:
            v = dict_lexicon[w]
        except KeyError:
            v = [['UK','UKa','UKb']]
            print (line[0],w,v)
        new_line.append(v[0][1:])
        for pingying in v[0][1:]:
            line2Str=line2Str+pingying+' '
            line3Str=line2Str
    # print(new_line)

    writeFileName='./aishell/wav_trn/'+line[0]+'.wav.trn'
    f_w = open(writeFileName,'wb')
    f_w.write(bytes(line1Str+'\n',encoding='utf8'))
    f_w.write(bytes(line2Str+'\n',encoding='utf8'))
    f_w.write(bytes(line3Str+'\n',encoding='utf8'))
    f_w.close()

    count=count+1
    print (count,len,'%.2f' % (count/len*100),line[0])