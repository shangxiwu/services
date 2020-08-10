#!/usr/bin/env python
# coding: utf-8

# ## TensorFlow unstack使用 
# 
# ### unstack at axis = 0
# ![Alt text](./images/basic_tensorflow/unstack_axis0.png)
# ### unstack at axis = 1
# ![Alt text](./images/basic_tensorflow/unstack_axis1.png)
# ### unstack at axis = 2
# ![Alt text](./images/basic_tensorflow/unstack_axis2.png)
# 

# In[6]:


import tensorflow as tf
x = tf.constant([[0.7,0.9],[0.1,0.4],[0.5,0.8]], name='x')
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


# ## TensorFlow stack使用
# 
# ### origin data
# ![Alt text](./images/basic_tensorflow/stack_origin.png)
# ### stack at axis = 0
# ![Alt text](./images/basic_tensorflow/stack_axis0.png)
# ### stack at axis = 1
# ![Alt text](./images/basic_tensorflow/stack_axis1.png)

# In[12]:


import tensorflow as tf

x = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], name='x')
y = tf.constant([[1.0, 1.0], [0.0, 1.0], [1.0, 1.0]], name='y')

stacked_axis0_result = tf.stack([x,y], axis=0)
stacked_axis1_result = tf.stack([x,y], axis=1)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    stacked_axis0_result_, stacked_axis1_result_ = sess.run([stacked_axis0_result, stacked_axis1_result])
    print(stacked_axis0_result_)
    print(stacked_axis0_result_.shape)
    
    print(stacked_axis1_result_)
    print(stacked_axis1_result_.shape)
           


# 
# 
# 

#  

# # RNN實作MNIST分類

# In[1]:


from __future__ import print_function
import tensorflow as tf

# Import MNIST data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# Training Parameters
learning_rate = 0.001
training_steps = 2000
batch_size = 128
display_step = 200

# Network Parameters
num_input = 28 # MNIST data input (img shape: 28*28)
timesteps = 28 # timesteps
num_hidden = 128 # hidden layer num of features
num_classes = 10 # MNIST total classes (0-9 digits)
tf.reset_default_graph()

# tf Graph input
X = tf.placeholder("float", [None, timesteps, num_input])
Y = tf.placeholder("float", [None, num_classes])


# Define weights
weights = {
    'out': tf.Variable(tf.random_normal([num_hidden, num_classes]))
}
biases = {
    'out': tf.Variable(tf.random_normal([num_classes]))
}

def RNN(x, weights, biases):


    # Define a cell with tensorflow
    cell=tf.contrib.rnn.BasicRNNCell(num_hidden)
    #cell = tf.contrib.rnn.LSTMCell(num_hidden, state_is_tuple=True)
    #cell = tf.contrib.rnn.GRUCell(num_hidden)
    
    ## switch to multiple layer RNN
    #cell = tf.nn.rnn_cell.MultiRNNCell([tf.contrib.rnn.BasicRNNCell(num_hidden) for _ in range(3)])
    
    init_state = cell.zero_state(batch_size, dtype=tf.float32)
    
    # Get cell output
    
    #if inputs is (batches, steps, inputs) ==> time_major=False
    #if inputs is (steps, batches, inputs) ==> time_major=True
    #state_is_tuple = Treu mean output of dynamic_rnn is (c_state, h_state)
    
    outputs, final_state = tf.nn.dynamic_rnn(cell, x, initial_state=init_state, time_major=False)
    # change outputs to list [(batch, outputs)..] * steps
    outputs = tf.unstack(tf.transpose(outputs, [1,0,2]))
    # Linear activation, using rnn inner loop last output
    return tf.matmul(outputs[-1], weights['out']) + biases['out']

logits = RNN(X, weights, biases)
#prediction = tf.nn.softmax(logits)

# Define loss and optimizer
loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
train_op = optimizer.minimize(loss_op)

# Evaluate model (with test logits, for dropout to be disabled)
correct_pred = tf.equal(tf.argmax(logits , 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Start training
with tf.Session() as sess:

    # Run the initializer
    sess.run(tf.global_variables_initializer())

    for step in range(1, training_steps+1):
        batch_x, batch_y = mnist.train.next_batch(batch_size)
        # Reshape data to get 28 seq of 28 elements
        batch_x = batch_x.reshape((batch_size, timesteps, num_input))
        # Run optimization op (backprop)
        sess.run(train_op, feed_dict={X: batch_x, Y: batch_y})
        if step % display_step == 0 or step == 1:
            # Calculate batch loss and accuracy
            loss, acc = sess.run([loss_op, accuracy], feed_dict={X: batch_x,
                                                                 Y: batch_y})
            print("Step " + str(step) + ", Minibatch Loss= " +                   "{:.4f}".format(loss) + ", Training Accuracy= " +                   "{:.3f}".format(acc))

    print("Optimization Finished!")

    # Calculate accuracy for 128 mnist test images
    test_len = 128
    test_data = mnist.test.images[:test_len].reshape((-1, timesteps, num_input))
    test_label = mnist.test.labels[:test_len]
    print("Testing Accuracy:",         sess.run(accuracy, feed_dict={X: test_data, Y: test_label}))


# In[ ]:




