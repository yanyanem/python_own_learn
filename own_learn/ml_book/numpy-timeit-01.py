"""

numpy-timeit-01.py

"""

import timeit 

normal_py_sec = timeit.timeit('sum(x*x for x in range(1000))', number=10000) 


print("Normal Python: %f sec" %normal_py_sec)


naive_np_sec = timeit.timeit('sum(na*na)', setup="import numpy as np; na=np.arange(1000)", number=10000)

print("Naive Numpy: %f sec" %naive_np_sec)


good_np_sec = timeit.timeit('na.dot(na)', setup="import numpy as np; na=np.arange(1000)", number=10000)

print("Good NumPy: %f sec" %good_np_sec) 

