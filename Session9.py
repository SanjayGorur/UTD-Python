#Session 9 with student.

import numpy as np

a = np.array([i for i in range(999999)])
a = np.array([[1, 2], [3, 4]])

a = np.array([1, 2, 3, 4, 5], dtype=complex)
a = np.array([[1,2,3],[5,6,7]])

a.shape = (3,2,1)
a = a.reshape(3,2)

a.shape = (3,2,1)
x = [1, 2, 3]

a = np.asarray(x, dtype=float)

s = "Hello World"
list(s)

a = np.frombuffer(s, dtype='S1')
a = np.arange(10)

np.char.add(['hello'],['world'])
a = np.array([0,30,45,60,90])
np.sin(a*np.pi/180)

a = np.array([-1.7,1.5,0.2,0.6,10])
np.floor(a)

np.ceil(a)
a = np.arange(9, dtype=np.float_).reshape(3, 3)

a*2+1
[1,2,3]*2

b = np.array([5,6,7])
np.add(a,b)

np.multiply(a,b)([5,6,7])
np.multiply(a,b)

np.append([1,2,3],a).reshape(3,4)
np.reciprocal(a)
