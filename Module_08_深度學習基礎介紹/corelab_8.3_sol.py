#!/usr/bin/env python
# coding: utf-8

# # Numpy的使用
# ## 在Tensorflow中我們會大量使用到numpy的陣列，請依照以下提示找出陣列的各種資訊

# In[1]:


import numpy as np


# ## 請建立1個3x5，元素由0~14的ndarray A，並找出該陣列的中位數、平均值與最大最小值

# In[2]:


A = np.arange(15).reshape(3, 5)
print('平均值: %d' % np.average(A))
print('中位數: %d' % np.median(A))
print('最大值: %d' % np.max(A))
print('最小值: %d' % np.min(A))


# In[ ]:




