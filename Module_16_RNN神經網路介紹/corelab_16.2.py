#!/usr/bin/env python
# coding: utf-8

# # stack數據組
# ## 給予多個數據組，針對軸0以及軸1分別取stack

# In[1]:


import tensorflow as tf

x = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], name='x')
y = tf.constant([[1.0, 1.0], [0.0, 1.0], [1.0, 1.0]], name='y')

## write your code here

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    stacked_axis0_result_, stacked_axis1_result_ = sess.run([stacked_axis0_result, stacked_axis1_result])
    print(stacked_axis0_result_)
    print(stacked_axis0_result_.shape)
    
    print(stacked_axis1_result_)
    print(stacked_axis1_result_.shape)
           


# In[ ]:




