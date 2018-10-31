
def loadDataSet():
	return [[1,3,4],[2,3,5],[1,2,3,5],[2,5],[1,2,3,4,5],[1,2,3,4,5,6]]

def createC1(dataSet):
	C1=[]
	for transaction in dataSet:
		for item in transaction:
			if not [item] in C1:
				C1.append([item])
	C1.sort()
	return map(frozenset,C1)


def scanD(D,Ck,minSupport):
	ssCnt={}
	for tid in D:
		for can in Ck: 
			if can.issubset(tid):
				if not ssCnt.has_key(can):ssCnt[can]=1
				else: ssCnt[can]+=1
	numItems = float(len(D))
	retList=[]
	supportData={}
	for key in ssCnt:
		support = ssCnt[key]/numItems
		if support >= minSupport:
			retList.insert(0,key)
		supportData[key]=support
	
	return retList,supportData
	

def aprioriGen(Lk,k):
	retList=[]
	lenLk=len(Lk)
	for i in range(lenLk):
		for j in range(i+1,lenLk):
			L1=list(Lk[i])[:k-2]; L2=list(Lk[j])[:k-2]
			L1.sort(); L2.sort()
			if L1==L2:
				retList.append(Lk[i]|Lk[j])
	return retList

def printCutLine(str):
	print('-'*30)
	print(str)
	print('-'*30)

def apriori(dataSet,minSupport=0.5):

	printCutLine('in apriori')

	C1=createC1(dataSet)
	D=map(set,dataSet)
	L1,supportData=scanD(D,C1,minSupport)
	L=[L1]
	k=2
	print('C1',C1)
	print('D',D)
	print('L1',L1)
	print('L',L)
	print('supportData',supportData)
	while (len(L[k-2])>0):
		print('L[k-2]',L[k-2])
		Ck=aprioriGen(L[k-2],k)
		Lk,supK=scanD(D,Ck,minSupport)
		supportData.update(supK)
		L.append(Lk)
		k+=1
		print('Ck',Ck)
		print('Lk',Lk)
		print('supK',supK)
		print('L',L)
		print('supportData',supportData)

	printCutLine('out apriori')

	return L,supportData

	
def test():
	dataSet = loadDataSet()
	
	print('dataSet',dataSet)
	
	C1=createC1(dataSet)
	for c in C1:print('C1',c)
	
	D=map(set,dataSet)
	for d in D:print('D',d)
	
	L1,suppData0=scanD(D,C1,0.5)
	print('L1',L1)
	print('suppData0',suppData0)
	
	

def generateRules(L,supportData,minConf=0.7):

	printCutLine('in generateRules')
	print('L',L)
	print('supportData',supportData)
	bigRuleList=[]
	for i in range(1,len(L)):
		for freqSet in L[i]:
			H1=[frozenset([item]) for item in freqSet ]
			print('H1',H1)
			print('i',i)
			if (i>1):
				rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
			else:
				calcConf(freqSet,H1,supportData,bigRuleList,minConf)

	printCutLine('out generateRules')
	
	return bigRuleList

def calcConf(freqSet, H, supportData, br1, minConf=0.7):

	printCutLine('in calcConf')
	prunedH=[]
	print('H',H)
	for conseq in H:
		conf = supportData[freqSet]/supportData[freqSet-conseq]
		print('freqSet',freqSet)
		print('conseq',conseq)
		print('supportData',supportData)
		print('supportData[freqSet]',supportData[freqSet])
		print('freqSet-conseq',freqSet-conseq)
		print('supportData[freqSet-conseq]',supportData[freqSet-conseq])
		print('conf',conf)
		if conf >= minConf:
			print (freqSet-conseq,'-->',conseq,'conf:',conf)
			br1.append((freqSet-conseq,conseq,conf))
			prunedH.append(conseq)
	printCutLine('out calcConf')
	return prunedH

def rulesFromConseq(freqSet, H, supportData, br1, minConf=0.7):
	printCutLine('in rulesFromConseq')
	m=len(H[0])
	print('H[0]',H[0])
	print('len(H[0])',len(H[0]))
	print('m',m)
	print('freqSet',freqSet)
	print('len(freqSet)',len(freqSet))
	print('supportData',supportData)
	print('br1',br1)
	print('m+1',m+1)
	print('H',H)
	if (len(freqSet)>(m+1)):
		Hmp1=aprioriGen(H,m+1)
		print('Hmp1 after aprioriGen',Hmp1)
		Hmp1=calcConf(freqSet, Hmp1, supportData, br1, minConf)
		print('Hmp1 after calcConf',Hmp1)
		if (len(Hmp1)>1):
			rulesFromConseq(freqSet,Hmp1,supportData,br1,minConf)
	printCutLine('out rulesFromConseq')


dataSet = loadDataSet()
L,suppData=apriori(dataSet,minSupport=0.5)
print('L',L)
print('suppData',suppData)

rules=generateRules(L,suppData,minConf=0.7)
for i,r in enumerate(rules): print(i,r)



