#!/usr/bin/env python
# coding: utf-8

# # 計算MNIST資料集的MSE

# In[ ]:


import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# ## 取出MNIST的前2筆資料，計算兩張圖片矩陣的MSE值

# In[ ]:


mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

#請補上如何取出前兩筆MNIST的程式碼

img1 = tf.constant(batch_xs[0])
img2 = tf.constant(batch_xs[1])

MSE = #請補上計算MSE的程式碼

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    cost1_ =  sess.run(MSE)

    print('mean square is\n {} \n'.format(cost1_))


# In[ ]:




