#!/usr/bin/env python
# coding: utf-8

# # Numpy array創建

# In[1]:


import numpy as np

np_array_1d = np.array([1,2,3]) 
print(type(np_array_1d))
print(np_array_1d.shape)
print(np_array_1d)

np_array_2d = np.array([[1, 2], [3, 4]]) 
print(type(np_array_2d))
print(np_array_2d.shape)
print(np_array_2d)
print(np_array_2d.ndim)
print(np_array_2d.size)


# In[2]:


import numpy as np
np_array_zeros = np.zeros([3,4])
np_array_ones = np.ones([2,3])
np_array_full = np.full([3,2], 5)
np_array_eye = np.eye(2)   
np_random = np.random.random((2,2))
np_arange = np.arange(4) # given number from 0~3
np_linspace = np.linspace(0, 2*np.pi, 5) # given 5 value start from 0 in steps: 2pi

print(np_array_zeros)
print(np_array_ones)
print(np_array_full)
print(np_array_eye)
print(np_random)
print(np_arange)
print(np_linspace)

#arr2[1,1] = np.nan  # not a number
#arr2[1,2] = np.inf  # infinite


# # Numpy基礎運算

# In[3]:


import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print(np.add(x, y))
print('==============')
# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))
print('==============')

# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print(x * y)
print(np.multiply(x, y))
print('==============')

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))
print('==============')

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))


# In[4]:


import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))
print('==============')
# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.matmul(x, v))
print('==============')
# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))
print('==============')

# Matrix transpose
print(x)
print(x.T)
print('==============')

# Matrix inverse
print(x)
print(np.linalg.inv(x))
print('==============')

# Matrix determinant
print(x)
print(np.linalg.det(x))

print('==============')
# SVD
U, S, V = np.linalg.svd(x)
print(U)
print(S)
print(V)


# # Numpy broadcasting性質

# In[5]:


import numpy as np
a = np.array([0, 1, 2])
b = a + 3
print(b)

M = np.ones((3, 3))
print(M + a)


# In[6]:


a = np.arange(3)
b = np.arange(3)[:, np.newaxis]

print(a)
print(b)
print(a+b)


# In[ ]:




