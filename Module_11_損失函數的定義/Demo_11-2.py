#!/usr/bin/env python
# coding: utf-8

# ## MSE

# In[2]:


import tensorflow as tf

predict = tf.constant([-0.5, 1, 2], name='predict')
labels = tf.constant([1.0, 0.0, 0.0], name='labels')

MSE = tf.losses.mean_squared_error(predictions=predict, labels=labels) 

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    cost1_ =  sess.run(MSE)

    print('mean square is\n {} \n'.format(cost1_))


# ## Cross-Entropy

#  

# In[3]:


import tensorflow as tf

predict = tf.constant([-0.5, 1, 2], name='predict')
labels = tf.constant([1.0, 0.0, 0.0], name='labels')

cost1 = tf.nn.softmax_cross_entropy_with_logits(logits=predict , labels=labels)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    cost1_ =  sess.run(cost1)

    print('softmax with cross entropy is\n {} \n'.format(cost1_))


# In[ ]:




