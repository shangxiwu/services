#!/usr/bin/env python
# coding: utf-8

# ## MNIST 使用
# MNIST is a computer vision dataset. It consists of black and white images from zero to nine. Each image is 28 * 28 and have been flatten to 784 dimension vector. Also, it includes labels for each image, telling us which digit it is.
# 
# ![Alt text](./images/dnn_implement/Selection_017.png)
# ![Alt text](./images/dnn_implement/Selection_018.png)
# 
# 
# The MNIST data is split into three parts: 
# 1. 55000 training data (mnist.train) with a shape of [55000, 784]
# 2. 10000 test data (mnist.test) with a shape of [10000, 784]
# 3. 5000 validation data (mnist.validation) with a shape of [5000, 784]
# 
# you can access:  
# training image as `mnist.train.images` (see below picture)  
# training label as `mnist.train.labels` (see below picture)  
# test image as `mnist.test.images`   
# test label as `mnist.test.labels`   
# 
# Note that label is encoded as "one-hot vectors", which mean if the target image is 2, the label should be [0,0,1,0,0,0,0,0,0,0]
# 
# 
# ![Alt text](./images/dnn_implement/Selection_021.png)
# ![Alt text](./images/dnn_implement/Selection_020.png)

# In[3]:


import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
tf.reset_default_graph()

# Load mnist dataset
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

batch_xs, batch_ys = mnist.train.next_batch(5)

print('first 5 labels {}:\n'.format(batch_ys))
print('first 5 images {}:\n'.format(batch_xs))


# # 建立簡單模型

# In[12]:


import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
tf.reset_default_graph()

# Load mnist dataset
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

# Define image input 784 = 28 * 28. Note that DNN input is a vector
# [None, 784] mean that there are a batch of data and each of them is 784 dimension vector
x = tf.placeholder(tf.float32, [None, 784])

# Define label. There are totally 10 class (0-9)
y = tf.placeholder(tf.float32, [None, 10])

W = tf.Variable(tf.truncated_normal([784, 10], stddev=0.1))
b = tf.Variable(tf.truncated_normal([10], stddev=0.1))
y_predict = tf.matmul(x, W) + b


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    batch_xs, batch_ys = mnist.train.next_batch(5)
        
    y_predict_ = sess.run(y_predict, feed_dict={x: batch_xs, y: batch_ys})
    print(y_predict_)
    print(y_predict_.shape)


# ## 建立DNN神經網路模型 

# In[11]:


import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
tf.reset_default_graph()

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

INPUT_NODE =784

LAYER1_NODE = 128
LAYER2_NODE = 64
LAYER3_NODE = 10


x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

W1 = tf.Variable(tf.truncated_normal([INPUT_NODE, LAYER1_NODE], stddev=0.1))
b1 = tf.Variable(tf.truncated_normal([LAYER1_NODE], stddev=0.1))
W2 = tf.Variable(tf.truncated_normal([LAYER1_NODE, LAYER2_NODE], stddev=0.1))
b2 = tf.Variable(tf.truncated_normal([LAYER2_NODE], stddev=0.1))
W3 = tf.Variable(tf.truncated_normal([LAYER2_NODE, LAYER3_NODE], stddev=0.1))
b3 = tf.Variable(tf.truncated_normal([LAYER3_NODE], stddev=0.1))

layer_1 = tf.matmul(x, W1) + b1
out1 = tf.nn.relu(layer_1)
layer_2 = tf.matmul(out1, W2) + b2
out2 = tf.nn.relu(layer_2)
layer_3 = tf.matmul(out2, W3) + b3
out3 = tf.nn.relu(layer_3)

y_predict = out3


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    batch_xs, batch_ys = mnist.train.next_batch(5)
        
    y_predict_ = sess.run(y_predict, feed_dict={x: batch_xs, y: batch_ys})
    print(y_predict_)
    print(y_predict_.shape)
    


# In[ ]:





# In[ ]:




