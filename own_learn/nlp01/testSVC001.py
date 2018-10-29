#testSVC001.py

from sklearn.svm import SVC
from nltk.classify import SklearnClassifier
from sklearn.feature_extraction.text import CountVectorizer

import nltk
import xlrd

def getTrainingData():
    #10 sample questions
    d_list = []
    d_list.append(("sales employee", "sales employee"))
    d_list.append(("sales person", "sales employee"))
    d_list.append(("top sales person", "sales amount"))
    d_list.append(("top 3 sales employee", "sales amount"))
    d_list.append(("the 3 most lucrative products", "profit"))
    d_list.append(("how much is earned", "profit"))
    d_list.append(("sales order", "sales order"))
    d_list.append(("order", "sales order"))
    d_list.append(("sales invoice", "sales invoice"))
    d_list.append(("invoice", "sales invoice")) 
    return d_list

def getContentFeature(x):
    xx = vectorizer.transform([x]).toarray()
    print ("shape: %i" % xx.shape[1])
    print("\n xx=", xx)
    result = {"word%i" % i : xx[0,i] for i in range (xx.shape[1])}
    print("\n result=", result)
    return result

#main 
data_list = getTrainingData()
question_list = [x for (x,y) in data_list]
label_list = [y for (x,y) in data_list]

print("\n question_list = ", question_list)
print("\n label_list = ", label_list)

vectorizer = CountVectorizer(min_df=1)
X = vectorizer.fit_transform(question_list)
print("\n X.toarray()=", X.toarray())
print("\n X.shape[0]=",X.shape[0])

test_v = vectorizer.transform(['it is a test of sales order'])
print("\n test_v.toarray()=", test_v.toarray())

training_set= [ (getContentFeature(question_list[i]), label_list[i]) for i in range(X.shape[0])]
print("\n training_set=", training_set)
    
myClassifier = nltk.SklearnClassifier(SVC()).train(training_set)

#Test
while True:
    query = str(input("Input query:")).strip().lower()
    feature = getContentFeature(query)
    #print feature
    print("\n result = ", myClassifier.classify(feature))



