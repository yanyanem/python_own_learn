
# numpy-01.py

import numpy as np

np.version.full_version

a = np.array([0,1,2,3,4,5])

print ("a = ", a )
print ("a.ndim = ", a.ndim )
print ("a.shape = ", a.shape )

b = a.reshape((3,2))

print ("b = ", b )
print ("b.ndim = ", b.ndim )
print ("b.shape = ", b.shape )

b[1][0]=77

print ("b = ", b )
print ("a = ", a )

c = a.reshape((3,2)).copy()

print ("c = ", c )

c[0][0] = -99

print ("c = ", c )


print ("a = ", a )
print ("a+a = ", a + a ) 
print ("a*2 = ", a*2 )
print ("a**2 = ", a**2 )
print ("a/2 = ", a/2 )
#print ("a/a = ", a/a )

print ("[1,2,3,4,5]*2 = ",[1,2,3,4,5]*2)
#print ("[1,2,3,4,5]**2 = ",[1,2,3,4,5]**2)
print ("[1,2,3,4,5]+[1,2,3,4,5] = ",[1,2,3,4,5]+[1,2,3,4,5] )
print ("[1,2,3,4,5]+[6,7,8] = ",[1,2,3,4,5]+[6,7,8] )
 
print ("a = ", a )
print ("a[np.array([2,3,4]) = ", a[np.array([2,3,4]) ] )
print ("a>4 = ", a>4 )
print ("a[a>4] = ", a[a>4] )

a.clip(0,4)
print ("a.clip(0,4) = ", a.clip(0,4) )
print ("a = ", a )

a[a>4]=4
print ("a = ", a )

d = np.array([1,2,np.NAN,3,4])
print ("d = ", d )

print ("np.isnan(d) = ", np.isnan(d) )

print ("~np.isnan(d) = ", ~np.isnan(d) )

print ("np.mean(d[~np.isnan(d)]) = ", np.mean(d[~np.isnan(d)])  )








