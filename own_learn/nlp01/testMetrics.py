

A1=[1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,2,3]
A2=[1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,1,1,1,3]

from sklearn.metrics import precision_recall_fscore_support

labels=[]
for x in A1:
	if (x not in labels): labels.append(x)
labels.sort()
print("labels=",labels)
#labels=[0,1,2,3]

precision, recall, fscore, support = precision_recall_fscore_support(A1,A2,labels=labels)

#print("precision=",precision) 
#print("recall=",recall) 
#print("fscore=",fscore) 
#print("support=",support) 

print("") 
print("%s %s %s %s %s" % ("Labels".ljust(10),"precision".ljust(10),"recall".ljust(10),"fscore".ljust(10),"support".ljust(10)) )
for i in range(len(labels)):
	t_1=labels[i]
	t0=float('%.2f' % precision[i])
	t1=float('%.2f' % recall[i])
	t2=float('%.2f' % fscore[i])
	t3=support[i]
	print("%s %s %s %s %s" % (str(t_1).ljust(10),str(t0).ljust(10),str(t1).ljust(10),str(t2).ljust(10),str(t3).ljust(10)) )