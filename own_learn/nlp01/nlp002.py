#nlp002.py

import readFile
#import dbCall
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm, metrics 
from sklearn.metrics import precision_recall_fscore_support

print("")
print("nlp002.py Start --------------------  ")
print("")


def getContentFeature(x):
	r = []
	x0=getJieBaContent(x)
	print("JieBaContent=",x0)
	v = cv.transform(x0)
	r.append( sum(v.toarray()) )
	return r


#jieba.add_word("上月", freq=None, tag=None)
def getJieBaContent(x):
	seg_list = jieba.cut(x)  # 默认是精确模式
	t=[x for x in seg_list]
	return t

train_data_file = "nlp002_train_data.txt"

dataCsv=readFile.readCsv(train_data_file)
#print("train_data_file=",csvData)

X_train_0=[y for (x,y) in dataCsv[1:] ]
Y_train=[x for (x,y) in dataCsv[1:] ]

#print("Y_train=",Y_train)
#print("X_train_0=",X_train_0)


X_train_1=[]
for x in X_train_0:
	t=getJieBaContent(x)
	X_train_1.append(t)

X_train_1_sum = sum(X_train_1,[])

#print("X_train_1=",X_train_1)
#print("sum(X_train_1,[])=",X_train_1_sum)

cv = CountVectorizer(min_df=1,ngram_range=(1,1),analyzer=(lambda s: s.split()))
#cv = CountVectorizer()
X = cv.fit_transform(X_train_1_sum)
#print("\n X.toarray()=", X.toarray())
#print("\n X.shape[0]=",X.shape[0])
#print("\n X.shape[1]=",X.shape[1])
featureNames = cv.get_feature_names()
print("featureNames=",featureNames) 


X_train_set=[]
for index, x in enumerate(X_train_1):
	v=cv.transform(x)
	X_train_set.append(sum(v.toarray())) 
	#print("v[%s]=%s" % (index,v))
	#print("v.toarray()=",v.toarray())
	#print("[%s] - sum(v.toarray())=%s" % (index,sum(v.toarray())) )


clf = svm.LinearSVC()
#clf = svm.SVC()
#clf.set_params(kernel='linear',probability=True)
#clf.set_params(kernel='rbf')
clf.fit(X_train_set, Y_train)
print("clf=",clf)
Y_predicted = clf.predict(X_train_set)

for i in range(len(X_train_0)): 
	if not (Y_train[i]==Y_predicted[i]):
		print(" %s ---  [Y_train] %s ---- [Y_predicted] %s --- %s" % (X_train_0[i],Y_train[i],Y_predicted[i],Y_train[i]==Y_predicted[i]) )


def showPercision(Y_train, Y_predicted): 

	A1=Y_train
	A2=Y_predicted

	labels=[]
	for x in A1:
		if (x not in labels): labels.append(x)
	labels.sort()

	precision, recall, fscore, support = precision_recall_fscore_support(A1,A2,labels=labels)

	print("") 
	print("%s %s %s %s %s" % ("Labels".ljust(30),"precision".ljust(10),"recall".ljust(10),"fscore".ljust(10),"support".ljust(10)) )
	for i in range(len(labels)):
		t_1=labels[i]
		t0=float('%.2f' % precision[i])
		t1=float('%.2f' % recall[i])
		t2=float('%.2f' % fscore[i])
		t3=support[i]
		print("%s %s %s %s %s" % (str(t_1).ljust(30),str(t0).ljust(10),str(t1).ljust(10),str(t2).ljust(10),str(t3).ljust(10)) )

showPercision(Y_train, Y_predicted)


#Test
print("")
while True:
	query = str(input("Input query:")).strip().lower()
	feature = getContentFeature(query)
	#print("feature=",feature)
	print("\n predict = ",  clf.predict((feature)) )
	print("clf.decision_function=", clf.decision_function(feature))
	#print("clf.predict_proba=",clf.predict_proba(feature))






'''
db = dbCall.initDB()
dbCall.sel_Dept_Total_Quantity(db)
dbCall.closeDB(db);
'''



print("")
print("nlp002.py End --------------------  ")
print("")
