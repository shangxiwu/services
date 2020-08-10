#!/usr/bin/env python
# coding: utf-8

# # Tensorflow的使用

# In[1]:


import tensorflow as tf


# ## 請使用tf.subtract、tf.divide等方式計算 (10/2)-1的答案

# In[2]:


x = tf.constant(10)
y = tf.constant(2)
z = tf.subtract(tf.divide(x,y),tf.cast(tf.constant(1), tf.float64))
with tf.Session() as sess:
    output = sess.run(z)
    print(output)


# In[ ]:




