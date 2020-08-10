#!/usr/bin/env python
# coding: utf-8

# # Numpy的使用
# ## 在Tensorflow中我們會大量使用到numpy的陣列，請依照以下提示找出陣列的各種資訊

# In[1]:


import numpy as np


# ## 1.請建立並印出1個3x4，元素都是0的ndarray A與1個3x4，元素都是1的ndarray B

# In[2]:


A = np.zeros((3,4))
B = np.ones((3,4))
print(A)
print(B)


# ## 2.請將以上2個陣列相加成另一個ndarray C並印出

# In[3]:


C = A + B
print(C)


# ## 3.將C乘以2倍後取該陣列的transpose存成陣列D並印出

# In[4]:


D = C*2
D = D.T
print(D)


# ## 4.將B與D做矩陣相乘存成陣列E並印出

# In[5]:


E = B.dot(D)
print(E)


# In[ ]:




