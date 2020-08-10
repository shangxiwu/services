#!/usr/bin/env python
# coding: utf-8

# # TensorFlow的矩陣操作

# In[1]:


import tensorflow as tf


# ## 請依照以下提示建立兩個tf.constant的矩陣，並輸出相乘結果

# In[2]:


matrix1 = tf.constant([[-1, 2.1],[1, -3]], name='matrix1', dtype=tf.float32)
matrix2 = tf.constant([[15, -2],[-7, 6]], name='matrix2', dtype=tf.float32)

result = tf.matmul(matrix1, matrix2)

with tf.Session() as sess: 
    print("matrix multiplication: {}\n".format(sess.run(result)))


# In[ ]:




