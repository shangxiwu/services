#!/usr/bin/env python
# coding: utf-8

# # jieba使用 
# 精確模式 ：將句子最精確地切開，叫適合文本分析。
# 寫法:words = jieba.cut(content, cut_all=False)
# 
# 全模式：把句子中所有的可以成詞的詞語都掃描出來, 速度快。
# 寫法:words = jieba.cut(content, cut_all=True)
# 
# 搜索引擎模式：在精確模式的基礎上對長詞再次切分，提高召回率，適合用於搜尋引擎分詞。 寫法:jieba.cut_for_search(Content)

# In[3]:


import jieba

sentence = "足球運動需要大家一起來推廣，歡迎加入我們的行列！"
print("輸入： {}".format(sentence))
words1 = jieba.cut(sentence, cut_all=False)
words2 = jieba.cut(sentence, cut_all=True)
words3 = jieba.cut_for_search(sentence)

print("精確模式：", end=' ')
for word in words1:
    print(word+'/', end='')

print('')

print("全模式：", end=' ')
for word in words2:
    print(word+'/', end='')

print('')

print("搜索引擎模式：", end=' ')
for word in words3:
    print(word+'/', end='')


# # 實作bag of words  

# In[1]:


from sklearn.feature_extraction.text import CountVectorizer
bards_words =["The fool doth think he is wise,",
              "but the wise man knows himself to be a fool"]

# CountVectorizer(stop_words="english")
vect = CountVectorizer()
vect.fit(bards_words)


print("Vocabulary size: {}".format(len(vect.vocabulary_)))
print("Vocabulary content:\n {}".format(vect.vocabulary_))

bag_of_words = vect.transform(bards_words)
print("Features name:\n{}".format(vect.get_feature_names()))
print("Dense representation of bag_of_words:\n{}".format(bag_of_words.toarray()))


# In[ ]:




