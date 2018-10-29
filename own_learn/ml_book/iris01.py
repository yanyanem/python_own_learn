'''

Book 机器学习系统设计 

page P22 第2章 如何对真实样本分类

code 代码部分

date 2017/03/09

copy sj 

'''


from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']

print ("data=",data)
print ("features=",features)
print ("feature_names=",feature_names)
print ("target=",target)

for t, marker, c in zip(range(3), ">ox", "rgb") :
    plt.scatter(features[target==t,0],
                features[target==t,1],
				marker=marker,
				c=c)
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[1])
plt.show()

for t, marker, c in zip(range(3), ">ox", "rgb") :
    plt.scatter(features[target==t,0],
                features[target==t,2],
				marker=marker,
				c=c)
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[2])
plt.show()

plength=features[:,2]
is_setosa=(target==0) 
print ("is_setosa-",is_setosa)

max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()

print('Maximun of setosa:{0}.'.format(max_setosa))
print('Minimun of others: {0}.' .format(min_non_setosa))

#for temp in features[:,2] :
#  if temp < 2 : print ('Iris Setosa - ',temp )
#  else: print( 'Iris Virginica or Iris Versicolour -', temp )


features = features[~is_setosa]
print("features-",features)
virginica = (target==2)[~is_setosa]


print("virginica-",virginica)

best_acc = -1.0
for fi in range(features.shape[1]):
  print("fi-",fi)
  thresh=features[:,fi].copy()
  print("thresh-",thresh)
  thresh.sort()
  print("thresh-",thresh)
  for t in thresh:
    pred=(features[:,fi]>t) 
    #print ("t-",t)
    #print ("pred-",pred)
    #print("pred==virginica-",pred==virginica)
    acc = (pred==virginica).mean()
    #print ("acc-",acc)
    if acc > best_acc:
       best_acc = acc
       best_fi = fi
       best_t = t
    #break


print("best_fi-",best_fi)
print("best_t-",best_t)
 
  
  
