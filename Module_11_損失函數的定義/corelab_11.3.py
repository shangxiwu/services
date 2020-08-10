#!/usr/bin/env python
# coding: utf-8

# # 建立5層的DNN並套用Cross-Entropy

# In[ ]:


import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# ## 取出MNIST的前20筆資料，將其代入建立的DNN網路，並輸出Cross-Entropy值

# In[ ]:


mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

INPUT_NODE =784

LAYER1_NODE = 128
LAYER2_NODE = 64
LAYER3_NODE = 48
LAYER4_NODE = 32
LAYER5_NODE = 10

#請依照以上給的條件建立出5層的DNN並再加一層cross_entropy


# In[ ]:




