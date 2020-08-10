#!/usr/bin/env python
# coding: utf-8

# # 資料批次輸入網路

# In[1]:


import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# ## 請以100筆為單位，將其一次輸入DNN網路，並輸出Cross-Entropy值

# In[2]:


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

# note on this line
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_predict))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    batch_xs, batch_ys = mnist.train.next_batch(100)
        
    cross_entropy_ =sess.run(cross_entropy, feed_dict={x: batch_xs, y: batch_ys})
    print("cross_entropy is {}".format(cross_entropy_))


# In[ ]:




