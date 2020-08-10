#!/usr/bin/env python
# coding: utf-8

# # 計算MNIST資料集的Cross-Entropy

# In[1]:


import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# ## 取出MNIST的前2筆資料，計算兩張圖片矩陣的Cross-Entropy值

# In[2]:


mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

batch_xs, batch_ys = mnist.train.next_batch(2)

img1 = tf.constant(batch_xs[0])
img2 = tf.constant(batch_xs[1])

cost1 = tf.nn.softmax_cross_entropy_with_logits(logits=img1, labels=img2) 

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    cost1_ =  sess.run(cost1)

    print('Cross-Entropy\n {} \n'.format(cost1_))


# In[ ]:




