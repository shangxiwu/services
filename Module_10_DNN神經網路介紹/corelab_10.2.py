#!/usr/bin/env python
# coding: utf-8

# # MNIST資料集的操作

# In[ ]:


from tensorflow.examples.tutorials.mnist import input_data


# ## 請將MNIST資料集讀取進來，取出第一筆資料印出，並以簡單判斷式判斷該資料為哪個數字

# In[ ]:


# Load mnist dataset
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

# 請從mnst讀出資料，並完成程式碼


# ### PS: 可以試著甮執行幾次，觀察結果是否相同

# In[ ]:




