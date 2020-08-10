#!/usr/bin/env python
# coding: utf-8

# # MNIST資料集的操作

# In[1]:


from tensorflow.examples.tutorials.mnist import input_data


# ## 請將MNIST資料集讀取進來，取出第一筆資料印出，並以簡單判斷式判斷該資料為哪個數字

# In[2]:


# Load mnist dataset
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

batch_xs, batch_ys = mnist.train.next_batch(1)

print(batch_ys)

num = 0
for i in batch_ys[0]:
    if i != 1:
        num += 1
    else:
        print("Number is: %d" % num)
        break


# In[ ]:




