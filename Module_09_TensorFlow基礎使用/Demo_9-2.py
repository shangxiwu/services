#!/usr/bin/env python
# coding: utf-8

# ## Basic Operation 

# In[2]:


import tensorflow as tf
x = tf.constant([[1, 2],[3, 4]], name='x')
y = tf.constant([[5, 6],[7, 8]], name='y')

tf_sum = x + y
tf_sub = x - y
tf_mul = x * y
tf_div = x / y
tf_mod = x % y
tf_neg = -x

with tf.Session() as sess:

    print("directly print x: {}\n".format(x))
    print("directly print y: {}\n".format(y))

    print("x: {}\n".format(sess.run(x)))
    print("y: {}\n".format(sess.run(y)))
    print("x+y: {}\n".format(sess.run(tf_sum)))
    print("x-y: {}\n".format(sess.run(tf_sub)))
    print("x*y: {}\n".format(sess.run(tf_mul)))
    print("x/y: {}\n".format(sess.run(tf_div)))
    print("x mod y: {}\n".format(sess.run(tf_mod)))
    print("-x: {}\n".format(sess.run(tf_neg)))


# In[4]:


import tensorflow as tf
a = tf.constant(5, name="input_a")
b = tf.constant(3, name="input_b")
c = tf.multiply(a, b, name="mul_c")
d = tf.add(a, b, name="add_d")
e = tf.add(c, d, name="add_e")

with tf.Session() as sess:
    print(sess.run(e)) # output => 23


# ![Alt text](./images/basic_tensorflow/computation_graph.png)
# 

# In[3]:


tf_sum = tf.add(x, y)
tf_sub = tf.subtract(x, y)
tf_mul = tf.multiply(x, y)
tf_div = tf.div(x,y)
tf_mod = tf.mod(x,y)
tf_neg = tf.negative(x)

with tf.Session() as sess:

    print("directly print x: {}\n".format(x))
    print("directly print y: {}\n".format(y))

    print("x: {}\n".format(sess.run(x)))
    print("y: {}\n".format(sess.run(y)))
    print("x+y: {}\n".format(sess.run(tf_sum)))
    print("x-y: {}\n".format(sess.run(tf_sub)))
    print("x*y: {}\n".format(sess.run(tf_mul)))
    print("x/y: {}\n".format(sess.run(tf_div)))
    print("x mod y: {}\n".format(sess.run(tf_mod)))
    print("-x: {}\n".format(sess.run(tf_neg)))


# ## Matrix Operation 

# In[5]:


import tensorflow as tf
matrix1 = tf.constant([[1, 2],[3, 4]], name='matrix1', dtype=tf.float32)
matrix2 = tf.constant([[5, 6],[7, 8]], name='matrix2', dtype=tf.float32)

product = tf.matmul(matrix1, matrix2)
inv = tf.matrix_inverse(matrix1)
trans = tf.matrix_transpose(matrix1)


with tf.Session() as sess:
 
    print("product: {}\n".format(sess.run(product)))
    print("inv: {}\n".format(sess.run(inv)))
    print("trans: {}\n".format(sess.run(trans)))


# ## Tensor Type
# 
# There are many data type in tensorflow. Following list some common type. If you want to change the type of tensor, ```tf.cast()``` can help. Please reference the following code.
# 
# | Python type | Description |  
# | :------: | :------: |  
# | tf.float32 | 32 bits floating point |
# | tf.float64 | 64 bits floating point |
# | tf.int8 | 8 bits signed integer |
# | tf.int16 | 16 bits signed integer |
# | tf.int32 | 32 bits signed integer |
# | tf.int64 | 64 bits signed integer |
# | tf.uint8 | 8 bits unsigned integer |
# | tf.uint16 | 16 bits unsigned integer |
# | tf.string | Variable length byte arrays. Each element of a Tensor is a byte array |
# | tf.bool | Boolean |
# 
# 
# 

# In[13]:


x_float32 = tf.constant([[1.1, 2.2],[3.3, 4.4]], dtype=tf.float32) # define float32 tensor
x_int = tf.cast(x_float32, tf.int32) #change type to int32

with tf.Session() as sess:
    print(x_float32)
    print(sess.run(x_float32))

    print(x_int)
    print(sess.run(x_int))


# ## Constant, Variable, and Placeholder 
# 
# Constant, variable, and placeholder can be set like the following. The difference among them is that 
# 1. constant can't be changed once define
# 2. variable would change while learning. It need to be initialized by constant tensorflow.
# 3. placeholder is used when you want to feed a data in the future. 
# 
# Before we go into code, let's first introduce some of generate function we usually use.
# 
# ### Random Generate Function 
# | function name | distribution | main parameters |  
# | :------: | :------: | :------: |  
# | tf.random_normal | normal distribution | mean, std, data type|
# | tf.truncated_normal | normal distribution within two std | mean, std, data type|
# | tf.random_uniform | uniform distribution | min value, max value, data type|
# | tf.random_gamma | gamma distribution | alpha, beta, data type|
# 
# 
# 
# ### Constant Generate Function
# | function name | function | example 
# | :------: | :------: | :------: |  
# | tf.zeros | produce all zeros | tf.zeros([2,1], int32)|
# | tf.ones | produce all ones | tf.ones([2,3], int32)|
# | tf.fill | produce specific number | tf.fill([2,1], 9)|
# | tf.constant | prodcuce a given constant | tf.constant([2.0,1.0])|
# 

# In[23]:


x_constant1 = tf.constant([[1.1, 2.2],[3.3, 4.4]], dtype=tf.float32) # define float32 tensor
x_constant2 = tf.zeros([2,3])
x_constant3 = tf.random_normal([1,3], stddev=1)

x_variable1 = tf.Variable(tf.constant([[1.1, 2.2],[3.3, 4.4]], dtype=tf.float32))
x_variable2 = tf.Variable(tf.zeros([2,3]))
x_variable3 = tf.Variable(tf.random_normal([1,3], stddev=1))


w1= tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2= tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))
x_placeholder1 = tf.placeholder(tf.float32, shape=(3, 2), name="input")
a = tf.matmul(x_placeholder1, w1)
y = tf.matmul(a, w2)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print('this is constant:')
    print(sess.run(x_constant1))
    print(sess.run(x_constant2))
    print(sess.run(x_constant3))
    print('this is variable:')
    print(sess.run(x_variable1))
    print(sess.run(x_variable2))
    print(sess.run(x_variable3))
    
    print('y is:')
    print(sess.run(y, feed_dict={x_placeholder1: [[0.7,0.9],[0.1,0.4],[0.5,0.8]]}))
 


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




