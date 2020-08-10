#!/usr/bin/env python
# coding: utf-8

# # 計算MNIST資料集的Cross-Entropy

# In[ ]:


import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# ## 取出MNIST的前2筆資料，計算兩張圖片矩陣的Cross-Entropy值

# In[ ]:


mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

#請補上讀取前兩筆資料的程式碼

img1 = tf.constant()
img2 = tf.constant()

cost1 = #請補上計算Cross-Entropy的程式碼

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    cost1_ =  sess.run(cost1)

    print('Cross-Entropy\n {} \n'.format(cost1_))


# In[ ]:




