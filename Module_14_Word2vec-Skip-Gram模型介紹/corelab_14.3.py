#!/usr/bin/env python
# coding: utf-8

# # 電影影評分類
# ## 給予電影影評資料集，分類評論好或壞

# In[1]:


# -*- coding: utf-8 -*-
import os
import re
import numpy as np
import tensorflow as tf

tf.reset_default_graph()

train_pos = "movie_review/train/pos/"
train_neg = "movie_review/train/neg/"
test_pos = "movie_review/test/pos/"
test_neg = "movie_review/test/neg/"

epochs = 17
batch_size = 64
max_sequence_length = 150
rnn_size = 10
embedding_size = 50
min_word_frequency = 10
learning_rate = 0.0005

def read_txt(dir_n):
    directory = os.fsencode(dir_n)

    train_data = []
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        with open(dir_n+filename, 'r') as f:
            train_data.append(f.read())
    return train_data


train_pos_data = read_txt(train_pos)
train_neg_data = read_txt(train_neg)
test_pos_data = read_txt(test_pos)
test_neg_data = read_txt(test_neg)

# Create a text cleaning function
def clean_text(text_string):
    text_string = re.sub(r'([^\s\w]|_|[0-9])+', '', text_string)
    text_string = " ".join(text_string.split())
    text_string = text_string.lower()
    return(text_string)

# Clean texts
train_pos_data = [clean_text(x) for x in train_pos_data]
train_neg_data = [clean_text(x) for x in train_neg_data]
test_pos_data = [clean_text(x) for x in test_pos_data]
test_neg_data = [clean_text(x) for x in test_neg_data]

train_pos_target = np.ones( (len(train_pos_data),1), dtype=np.int32 )
train_neg_target = np.zeros( (len(train_pos_data),1), dtype=np.int32 )

test_pos_target = np.ones( (len(test_pos_data),1), dtype=np.int32 )
test_neg_target = np.zeros( (len(test_pos_data),1), dtype=np.int32 )

train_target = np.concatenate((train_pos_target,train_neg_target), axis=0)
test_target = np.concatenate((test_pos_target,test_neg_target), axis=0)

all_data = np.concatenate((train_pos_data,train_neg_data,test_pos_data,test_neg_data), axis=0)

vocab_processor = tf.contrib.learn.preprocessing.VocabularyProcessor(max_sequence_length,
                                                                     min_frequency=min_word_frequency)
all_data_pd = np.array(list(vocab_processor.fit_transform(all_data)))

train_data_pd,test_data_pd = np.split(all_data_pd, 2, axis=0)

shuffled_ix = np.random.permutation(np.arange(len(train_target)))
x_train = train_data_pd[shuffled_ix]
y_train = train_target[shuffled_ix]
y_train  = y_train.reshape((len(y_train),))


shuffled_ix = np.random.permutation(np.arange(len(test_target)))
x_test = test_data_pd[shuffled_ix]
y_test = test_target[shuffled_ix]
y_test  = y_test.reshape((len(y_test),))


vocab_size = 28685
print("Vocabulary Size: {:d}".format(vocab_size))

# Create placeholders
x_data = tf.placeholder(tf.int32, [None, max_sequence_length])
y_output = tf.placeholder(tf.int32, [None])

# Create embedding

## finish this part
## write your code here


# Loss function
losses = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits_out, labels=y_output) # logits=float32, labels=int32
loss = tf.reduce_mean(losses)
train_step = tf.train.RMSPropOptimizer(learning_rate).minimize(loss)

accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(logits_out, 1), tf.cast(y_output, tf.int64)), tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    train_loss = []
    test_loss = []
    train_accuracy = []
    test_accuracy = []
    # Start training
    for epoch in range(epochs):

        # Shuffle training data
        shuffled_ix = np.random.permutation(np.arange(len(x_train)))
        x_train = x_train[shuffled_ix]
        y_train = y_train[shuffled_ix]
        num_batches = int(len(x_train)/batch_size) + 1
        # TO DO CALCULATE GENERATIONS ExACTLY
        for i in range(num_batches):
            # Select train data
            min_ix = i * batch_size
            max_ix = np.min([len(x_train), ((i+1) * batch_size)])
            x_train_batch = x_train[min_ix:max_ix]
            y_train_batch = y_train[min_ix:max_ix]

            # Run train step
            train_dict = {x_data: x_train_batch, y_output: y_train_batch}
            sess.run(train_step, feed_dict=train_dict)
            if i % 50 == 0:
                # Run loss and accuracy for training
                temp_train_loss, temp_train_acc = sess.run([loss, accuracy], feed_dict=train_dict)
                train_loss.append(temp_train_loss)
                train_accuracy.append(temp_train_acc)
                print('Train Loss: {:.2}, Train Acc: {:.2}'.format(temp_train_loss, temp_train_acc))

        # Run Eval Step
        test_dict = {x_data: x_test, y_output: y_test}
        temp_test_loss, temp_test_acc = sess.run([loss, accuracy], feed_dict=test_dict)
        test_loss.append(temp_test_loss)
        test_accuracy.append(temp_test_acc)
        print('Epoch: {}, Test Loss: {:.2}, Test Acc: {:.2}'.format(epoch+1, temp_test_loss, temp_test_acc))

