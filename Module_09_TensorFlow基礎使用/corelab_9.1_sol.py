#!/usr/bin/env python
# coding: utf-8

# # Tensorflow的使用

# In[1]:


import tensorflow as tf


# ## 請使用tf.session的方式計算A與B的四則運算
# 
# ### 除法請取到小數點第3位

# In[2]:


A = 2245
B = 268

A = tf.constant(A)
B = tf.constant(B)

tf_add = tf.add(A, B)
tf_subtract = tf.subtract(A, B)
tf_multiply = tf.multiply(A, B)
tf_divide = tf.divide(A, B)

with tf.Session() as sess:
    print("A + B = %d" % sess.run(tf_add))
    print("A - B = %d" % sess.run(tf_subtract))
    print("A x B = %d" % sess.run(tf_multiply))
    print("A / B = %.3f" % sess.run(tf_divide))


# In[ ]:




