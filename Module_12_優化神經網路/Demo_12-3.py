#!/usr/bin/env python
# coding: utf-8

# ## 改變學習率

# In[1]:


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

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_predict))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
#train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        
        train_step_, cross_entropy_ =sess.run([train_step, cross_entropy], feed_dict={x: batch_xs, y: batch_ys})
        if step % 50 == 0:
            print("step {}: cross_entropy is {}".format(step, cross_entropy_))


# # DNN神經網路訓練及驗證

# In[2]:


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

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_predict))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(y_predict, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        
        train_step_, cross_entropy_ =sess.run([train_step, cross_entropy], feed_dict={x: batch_xs, y: batch_ys})
        if step % 50 == 0:
            print("step {}: cross_entropy is {}".format(step, cross_entropy_))
    accuracy_ = sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels})
    print('Testing...... accuracy is {}'.format(accuracy_))


# In[ ]:




