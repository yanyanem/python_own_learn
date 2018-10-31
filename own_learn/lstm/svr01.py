import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


train_df = pd.read_csv("data\\us-air-carrier-traffic-statistic.csv")


print(train_df)

Month=train_df['Month']
PassengerNum=train_df['U.S. Air Carrier Traffic Statistics - Passenger Enplanements']


#Enplanements = pd.DataFrame({"Enplanements":PassengerNum,'log(Enplanements+1)':np.log1p(PassengerNum)})
#Enplanements.hist()
#plt.show()

MonthList = [ m.replace('-','')for m in Month ]
X=[ i for i in range(0,len(Month))]
plt.plot(X,PassengerNum)
plt.show()

from sklearn.svm import SVR

#X=[[float(i)] for i in MonthList]
X=[ [int(i)] for i in range(0,len(Month))]
y=[float(i) for i in PassengerNum]
print(X)
print(y)
tr_X=X[80:130]
tr_y=y[80:130]

# #############################################################################
# Look at the results
lw = 2
plt.scatter(X, y, color='darkorange', label='data')
svr_lin = SVR(kernel='linear', C=1e3,verbose=True)
y_lin = svr_lin.fit(tr_X, tr_y).predict(tr_X)
plt.plot(tr_X, y_lin, color='c', lw=lw, label='Linear model')
svr_rbf = SVR(kernel='rbf', C=2*1e4, gamma=0.05, verbose=True)
y_rbf = svr_rbf.fit(tr_X, tr_y).predict(tr_X)
plt.plot(tr_X, y_rbf, color='navy', lw=lw, label='RBF model')
#svr_poly = SVR(kernel='poly', C=1e3, degree=2)
#y_poly = svr_poly.fit(X, y).predict(X)
#plt.plot(X, y_poly, color='cornflowerblue', lw=lw, label='Polynomial model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()

te_X_pos_start=tr_X[-1][0]+1
print('te_X_pos_start',te_X_pos_start)
te_X = [[int(i)] for i in range(te_X_pos_start,te_X_pos_start+12)]
print('te_X',te_X)
te_y = svr_rbf.fit(tr_X, tr_y).predict(te_X)
#plt.plot(te_X, te_y, color='blue')
plt.scatter(te_X, te_y, color='blue')

plt.show()



