#testSVC002_LinearSVC.py

from sklearn.svm import SVC, LinearSVC
from sklearn.feature_extraction.text import CountVectorizer

question_list = ["sales person", "employee", "top sales person", "profit", "best products"]
label_list = ['a','a','b','c','d']

vectorizer = CountVectorizer(min_df=1)
X = vectorizer.fit_transform(question_list).toarray()

#clf = SVC() #cause error!
clf = LinearSVC()
clf.fit (X, label_list)
for q in question_list:
	feature = vectorizer.transform([q]).toarray()
	print (clf.predict(feature))


