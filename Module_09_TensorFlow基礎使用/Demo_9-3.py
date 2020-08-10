#!/usr/bin/env python
# coding: utf-8

# ## Save and Restore Model
# TensorFlow saver can save/restore model or variable for future usage. Saver would produce theses three files:
# 1. model.ckpt.meta: preserve computation graph
# 2. model.ckpt: preserve variable in the graph
# 3. checkpoint: preserve the latest model
# 

# In[3]:


import tensorflow as tf
v1 = tf.Variable(tf.constant(1.0, shape=[1]), name='v1')
v2 = tf.Variable(tf.constant(2.0, shape=[1]), name='v2')
result = tf.add(v1, v2, name="result")
saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver.save(sess, "Saved_model/model.ckpt")
    print(sess.run(result))
    


# If you want to restore variable only, you should build the computation graph again and load previous variable.

# In[2]:


import tensorflow as tf
tf.reset_default_graph()
v1 = tf.Variable(tf.constant(1.0, shape=[1]), name='v1')
v2 = tf.Variable(tf.constant(2.0, shape=[1]), name='v2')
result = v1 + v2
saver = tf.train.Saver()

with tf.Session() as sess:
    saver.restore(sess, "Saved_model/model.ckpt")
    print(sess.run(result))


# Or, you can restore previous computation graph and variables by the following code

# In[1]:


import tensorflow as tf
saver = tf.train.import_meta_graph("Saved_model/model.ckpt.meta")
with tf.Session() as sess:
    saver.restore(sess, "Saved_model/model.ckpt")
    print(sess.run("result:0"))


# ## Some Optimizer

# In[20]:


import tensorflow as tf

learning_rate = 0.01
a = tf.constant(2.0)
b = tf.constant(1.0)
c = tf.constant(3.0)
x = tf.Variable(tf.constant(1.0), name='x')
y = a*x*x + b*x + c

optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(y)
#optimizer = tf.train.AdamOptimizer(learning_rate).minimize(y)
#optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(y)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for _ in range(100):
        optimizer_ = sess.run(optimizer)
    x_ = sess.run(x)    
    print('when x = {}, y have min value'.format(x_))    


# 
# 
# 

#  

# In[ ]:




