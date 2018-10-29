
'''

book 机器学习系统设计 

page P113 第7章 回归：推荐

code 代码部分

date 2017/03/09

copy sj 

'''


from sklearn.datasets import load_boston
import numpy as np
from matplotlib import pyplot as plt


boston = load_boston()

print(boston.data)
print(boston.target)
print(boston.DESCR)
print(boston.feature_names)

plt.xlim(2.5,10)
plt.ylim(0,55)

#plt.subplot(221)
plt.scatter(boston.data[:,5],boston.target,color='b')


x=boston.data[:,5]
x=np.array( [ [v,1] for v in x ] )
print(x)
y=boston.target
m,c=np.linalg.lstsq(x,y)[0]
print(m)
print(c)
#plt.subplot(222)
plt.plot(x, m*x + c, 'r', label='Fitted line')
#plt.show()

(slope,bias),total_error,_,_ = np.linalg.lstsq(x,y) 
print(slope)
print(bias)
print(total_error)
rmse=np.sqrt(total_error[0]/len(x))
print(rmse)

#测试一下 concatenate
a = np.array([[1, 2], [3, 4]])
print(a)
b = np.array([[5, 6]])
print(b)
c=np.concatenate((a, b), axis=0)
print(c)
print(b.T)
c=np.concatenate((a, b.T), axis=1)
print(c)


#多维回归
print("--------------------------------------------------------------------------")
x=boston.data

a=np.array([[ (1) for i in range(len(x)) ] ])
#print(a)
#x=np.array( [ np.concatenate(v,[1]) for v in boston.data] )
x=np.concatenate((x,a.T),axis=1)
print(x)

y=boston.target
s,total_error,_,_ = np.linalg.lstsq(x,y)
print(s)
print(total_error)
rmse=np.sqrt(total_error[0]/len(x))
print(rmse)

print ("LinearRegression-----------------------------------------------------------------------")
#线性多维回归的另一种实现方式

from sklearn.linear_model import LinearRegression

lr=LinearRegression(fit_intercept=True)
lr.fit(x,y)
p=lr.predict(x)
e=p-y
#print(e)
total_error=np.sum(e*e)
rmse_train=np.sqrt(total_error/len(p))
print("RMSE on training: {}".format(rmse_train))



#回归的交叉验证

from sklearn.cross_validation import KFold
kf=KFold(len(x), n_folds=10)
err=0
for train,test in kf:
	lr.fit(x[train],y[train])
	p=lr.predict(x[test])
	e=p-y[test]
	err += np.sum(e*e)
rmse_10cv=np.sqrt(err/len(x))
print("RMSE on 10-fold CV: {}".format(rmse_10cv))

print ("ElasticNet-----------------------------------------------------------------------")
#使用弹性网回归

from sklearn.linear_model import ElasticNet

en=ElasticNet(fit_intercept=True,alpha=0.5)
en.fit(x,y)
print(en)
p=en.predict(x)
e=p-y
#print(e)
total_error=np.sum(e*e)
rmse_train=np.sqrt(total_error/len(p))
print("RMSE on training: {}".format(rmse_train))


x_plt=boston.data[:,5]
x_plt=np.array( [ [v,1] for v in x_plt ] )
y_plt=p
m,c=np.linalg.lstsq(x_plt,y_plt)[0]
print(m)
print(c)
#plt.subplot(223)
plt.plot(x_plt, m*x_plt + c, 'g--', label='Fitted line 02 LinearRegression')
plt.show()
#回归的交叉验证

from sklearn.cross_validation import KFold
kf=KFold(len(x), n_folds=10)
err=0
for train,test in kf:
	en.fit(x[train],y[train])
	p=en.predict(x[test])
	e=p-y[test]
	err += np.sum(e*e)
rmse_10cv=np.sqrt(err/len(x))
print("RMSE on 10-fold CV: {}".format(rmse_10cv))



print ("ElasticNetCV-----------------------------------------------------------------------")
#使用弹性网回归+交叉验证
from sklearn.linear_model import ElasticNetCV
met=ElasticNetCV(fit_intercept=True)
print(met)

met.fit(x,y)
p=met.predict(x)
e=p-y
#print(e)
total_error=np.sum(e*e)
rmse_train=np.sqrt(total_error/len(p))
print("RMSE on training: {}".format(rmse_train))

kf=KFold(len(y),n_folds=10)
for train,test in kf:
	met.fit(x[train],y[train])
	p=met.predict(x[test])
	e=p-y[test]
	err += np.dot(e,e)
rmse_10cv=np.sqrt(err/len(y))
print("RMSE on 10-fold CV: {}".format(rmse_10cv))
print(met)




