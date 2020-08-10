#!/usr/bin/env python
# coding: utf-8

# # Numpy的使用
# ## 在Tensorflow中我們會大量使用到numpy的陣列，請依照以下提示找出陣列的各種資訊

# In[1]:


import numpy as np


# In[2]:


array = np.array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])


# ## 1.請印出array這個物件是否為numpy.ndarray的型態，若是請輸出"True"

# In[3]:


if type(array) is np.ndarray:
    print(True)


# ## 2.請確認該陣列中的資料型態為何

# In[4]:


print(array.dtype)


# ## 3.在使用TensorFlow時，我們的訓練資料的維度被嚴格規定，假設我們的資料維度要求為(5, 3)，請確認array的維度是否正確，若是請輸出"True"，反之請輸出"False"

# In[5]:


if array.shape == (5, 3):
    print(True)
else:
    print(False)


# ## 4.在運算中我們有時候會需要知道陣列中會有多少元素，請確認array中有幾個元素

# In[6]:


print(array.size)


# In[ ]:




