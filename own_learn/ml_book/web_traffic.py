# web_traffic.py

import scipy as sp
import numpy as np

data = sp.genfromtxt("web_traffic.csv", delimiter=",")

print ("data[:10]=",data[:10]) 

print ("data.shape=",data.shape) 

x = data[:,0]
y = data [:,1]
print ("x[:10]=",x[:10]) 
print ("y[:10]=",y[:10]) 

print ("sp.sum(sp.isnan(y)=",sp.sum(sp.isnan(y)) )

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

print ("x[:10]=",x[:10]) 
print ("y[:10]=",y[:10]) 


import matplotlib.pyplot as plt



plt.scatter(x,y,linewidths=1,alpha=0.5)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)], ['week %i' %w for w in range(10) ] )
plt.autoscale(tight=True)
plt.grid()
#plt.show()

def error(f,x,y): return sp.sum((f(x)-y)**2) 

fp1,residuals, rank, sv, rcond = sp.polyfit(x,y,1,full=True)
print("Model parameters: %s" %fp1 ) 
print (residuals)
f1=sp.poly1d(fp1)
print("error(f1,x,y)=",error(f1,x,y))
fx=sp.linspace(0,x[-1],1000)
print("x[-1]=",x[-1])
plt.plot(fx,f1(fx),linewidth=1)
plt.legend(["d=%i" % f1.order], loc="upper left" )
#plt.show()

fp2=sp.polyfit(x,y,2)
print(fp2)
f2=sp.poly1d(fp2)
print("error(f2,x,y)=",error(f2,x,y))
plt.plot(fx,f2(fx),linewidth=1)
plt.legend(["d=%i" % f2.order], loc="upper left" )

fp3=sp.polyfit(x,y,10)
print(fp3)
f3=sp.poly1d(fp3)
print("error(f3,x,y)=",error(f3,x,y))
plt.plot(fx,f3(fx),linewidth=1)


plt.legend(["%i" % f1.order, f2.order,f3.order ], loc="upper left" )
#plt.show()



inflection = int(3.0*7*24)
print(inflection)
xa = x[:inflection]
ya = y[:inflection]
xb = x[inflection:]
yb = y[inflection:]

fa=sp.poly1d(sp.polyfit(xa,ya,1))
fb=sp.poly1d(sp.polyfit(xb,yb,1))

fa_error=error(fa,xa,ya)
fb_error=error(fb,xb,yb)
print("Error inflection=%f" % (fa_error+fb_error))


fx=sp.linspace(0,x[inflection],1000)
plt.plot(fx,fa(fx),linewidth=2)
fx=sp.linspace(x[inflection],x[-1],1000)
plt.plot(fx,fb(fx),linewidth=2)

plt.legend(["%i" % f1.order, f2.order,f3.order,fa.order,fb.order ], loc="upper left" )
plt.show()



print("f1=",f1)
print("f2=",f2)
print("fa=",fa)
print("fb=",fb)

from scipy.optimize import fsolve
reached_max = fsolve(f1-100000,800)/(7*24)
print("f1 - 100,000 hits/hour expected at week %f" % reached_max[0]) 
reached_max = fsolve(f2-100000,800)/(7*24)
print("f2 - 100,000 hits/hour expected at week %f" % reached_max[0]) 

reached_max = fsolve(fa-100000,800)/(7*24)
print("fa - 100,000 hits/hour expected at week %f" % reached_max[0]) 
reached_max = fsolve(fb-100000,800)/(7*24)
print("fb - 100,000 hits/hour expected at week %f" % reached_max[0]) 






