#!/usr/bin/env python
# coding: utf-8

# # 給予一個英文語料庫，使用scikit-learn做bag of words(進階)

# In[1]:


from sklearn.feature_extraction.text import CountVectorizer
bards_words =["The fool doth think he is wise,",
              "but the wise man knows himself to be a fool",
              "this is an apple"]


## write your code here


print("Vocabulary size: {}".format(len(vect.vocabulary_)))
print("Vocabulary content:\n {}".format(vect.vocabulary_))

## write your code here
bag_of_words = 
print("Features name:\n{}".format(vect.get_feature_names()))
print("Dense representation of bag_of_words:\n{}".format(bag_of_words.toarray()))


# In[ ]:




