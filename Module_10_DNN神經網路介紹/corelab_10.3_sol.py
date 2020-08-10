#!/usr/bin/env python
# coding: utf-8

# # 建立DNN網路

# In[1]:


import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# ## 請建立一個5層的DNN網路，各層的神經元數量請自行給定，並將MNIST代入

# In[2]:


mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

INPUT_NODE =784

LAYER1_NODE = 128
LAYER2_NODE = 64
LAYER3_NODE = 64
LAYER4_NODE = 32
LAYER5_NODE = 10


x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

W1 = tf.Variable(tf.truncated_normal([INPUT_NODE, LAYER1_NODE], stddev=0.1))
b1 = tf.Variable(tf.truncated_normal([LAYER1_NODE], stddev=0.1))
W2 = tf.Variable(tf.truncated_normal([LAYER1_NODE, LAYER2_NODE], stddev=0.1))
b2 = tf.Variable(tf.truncated_normal([LAYER2_NODE], stddev=0.1))
W3 = tf.Variable(tf.truncated_normal([LAYER2_NODE, LAYER3_NODE], stddev=0.1))
b3 = tf.Variable(tf.truncated_normal([LAYER3_NODE], stddev=0.1))
W4 = tf.Variable(tf.truncated_normal([LAYER3_NODE, LAYER4_NODE], stddev=0.1))
b4 = tf.Variable(tf.truncated_normal([LAYER4_NODE], stddev=0.1))
W5 = tf.Variable(tf.truncated_normal([LAYER4_NODE, LAYER5_NODE], stddev=0.1))
b5 = tf.Variable(tf.truncated_normal([LAYER5_NODE], stddev=0.1))


layer_1 = tf.matmul(x, W1) + b1
out1 = tf.nn.relu(layer_1)
layer_2 = tf.matmul(out1, W2) + b2
out2 = tf.nn.relu(layer_2)
layer_3 = tf.matmul(out2, W3) + b3
out3 = tf.nn.relu(layer_3)
layer_4 = tf.matmul(out3, W4) + b4
out4 = tf.nn.relu(layer_4)
layer_5 = tf.matmul(out4, W5) + b5
out5 = tf.nn.relu(layer_5)

y_predict = out5


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    batch_xs, batch_ys = mnist.train.next_batch(5)
        
    y_predict_ = sess.run(y_predict, feed_dict={x: batch_xs, y: batch_ys})
    print(y_predict_)
    print(y_predict_.shape)


# In[ ]:




