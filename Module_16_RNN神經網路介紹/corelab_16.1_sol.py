#!/usr/bin/env python
# coding: utf-8

# # unstack數據組
# ## 給予一個數據組，針對軸0取unstack

# In[2]:


import tensorflow as tf
x = tf.constant([[-0.7,2],[-0.3,7],[0.5,0.8]], name='x')
axis0_x = tf.unstack(x, axis=0)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    x_, axis0_ = sess.run([x, axis0_x])
    print('before unstack......')
    print(x_)
    print('after unstack......')
    print(axis0_[0])
    print(axis0_[1])
    print(axis0_[2])


# In[ ]:




