#CountVectorizer.py

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(min_df=1)

print(vectorizer)

content = ["How to format my hard disk", " Hard disk format problems" ]
X = vectorizer.fit_transform(content)
Y = vectorizer.get_feature_names()
print("X=",X)
print("Y=",Y) 
print("len(Y)=",len(Y)) 
print("X.toarray().transpose()=",X.toarray().transpose())

import os

DIR = "C:\\00-Erics\\03-prjs\\python\\py\\scikit\\txt01"
posts = [open(os.path.join(DIR,f)).read() for f in os.listdir(DIR) ]

X_train=vectorizer.fit_transform(posts)

num_samples, num_features = X_train.shape

print("#samples: %d, #features: %d" % (num_samples, num_features)) #samples: 5, #features: 25

print(vectorizer.get_feature_names())

new_post = "databases is very huge. eric like it to build toy image. "
new_post_vec = vectorizer.transform([new_post])

print("new_post=",new_post)
print(new_post_vec)
print(new_post_vec.toarray())

import scipy as sp
def dist_raw(v1,v2):
	delta = v1-v2
	return sp.linalg.norm(delta.toarray())


import sys

'''
print("use dist_raw")
best_doc=None
best_dist=sys.maxsize
best_i=None
for i in range(0,num_samples):
	post=posts[i]
	if post==new_post:
		continue
	post_vec = X_train.getrow(i)
	d=dist_raw(post_vec,new_post_vec)
	print("=== Post %i with dist=%.2f: %s" %(i,d,post))
	
	if d<best_dist:
		best_dist=d
		best_i=i
		
print("best post is %i with dist=%.2f" %(best_i,best_dist)) 

print("X_train.getrow(3).toarray()=",X_train.getrow(3).toarray())
print("X_train.getrow(4).toarray()=",X_train.getrow(4).toarray())

'''

def dist_norm(v1,v2):
	v1_normalized = v1/sp.linalg.norm(v1.toarray())
	v2_normalized = v2/sp.linalg.norm(v2.toarray())
	delta = v1_normalized - v2_normalized
	return sp.linalg.norm(delta.toarray()) 
	

print("use dist_norm")
best_doc=None
best_dist=sys.maxsize
best_i=None
for i in range(0,num_samples):
	post=posts[i]
	if post==new_post:
		continue
	post_vec = X_train.getrow(i)
	d=dist_norm(post_vec,new_post_vec)
	print("=== Post %i with dist=%.2f: %s" %(i,d,post))
	
	if d<best_dist:
		best_dist=d
		best_i=i
		
print("best post is %i with dist=%.2f" %(best_i,best_dist)) 
print("new_post_vec=",new_post_vec.getrow(0).toarray())
print("X_train.getrow(3).toarray()=",X_train.getrow(3).toarray())
print("X_train.getrow(4).toarray()=",X_train.getrow(4).toarray())
print("X_train.getrow(5).toarray()=",X_train.getrow(5).toarray())





