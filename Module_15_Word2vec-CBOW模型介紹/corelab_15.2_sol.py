#!/usr/bin/env python
# coding: utf-8

# # Gensim套件實作CBOW (進階)
# ## 使用Gensim完成CBOW模型並做文字類推

# In[1]:


import gzip
import gensim
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

data_file="./reviews_data.txt.gz"

with gzip.open ('./reviews_data.txt.gz', 'rb') as f:
    for i,line in enumerate (f):
        print(line)
        break


# In[2]:


def read_input(input_file):
    """This method reads the input file which is in gzip format"""
    
    print("reading file {0}...this may take a while".format(input_file))
    
    with gzip.open (input_file, 'rb') as f:
        for i, line in enumerate (f): 

            if (i%10000==0):
                print("read {0} reviews".format (i))
            # do some pre-processing and return a list of words for each review text
            yield gensim.utils.simple_preprocess (line)

# read the tokenized reviews into a list
# each review item becomes a serries of words
# so this becomes a list of lists
documents = list (read_input (data_file))
print("Done reading data file")


# In[3]:


'''
Word2Vec model parameters

size:
The size of the dense vector to represent each token or word. If you have very limited data, then size should be a much smaller value. If you have lots of data, its good to experiment with various sizes. A value of 100-150 has worked well for me.

window:
The maximum distance between the target word and its neighboring word. If your neighbor's position is greater than the maximum window width to the left and the right, then, some neighbors are not considered as being related to the target word. In theory, a smaller window should give you terms that are more related. If you have lots of data, then the window size should not matter too much, as long as its a decent sized window.

min_count:
Minimium frequency count of words. The model would ignore words that do not statisfy the min_count. Extremely infrequent words are usually unimportant, so its best to get rid of those. Unless your dataset is really tiny, this does not really affect the model.

workers:
How many threads to use behind the scenes?

sg: sg=1 means skip-gram and sg=0 menascbow
'''
model = gensim.models.Word2Vec (documents, size=150, window=10, min_count=2, workers=10, sg=0)
model.train(documents,total_examples=len(documents),epochs=10)


# In[4]:


# print word vector
model.wv['clean']


# In[5]:


# get everything related to stuff on the bed
w1 = ["bed",'sheet']
w2 = ['couch']
model.wv.most_similar (positive=w1,negative=w2,topn=10)


# In[ ]:




