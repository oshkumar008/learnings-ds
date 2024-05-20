"""Here we will use technique One-Hot Encoding(ONE), Bag of Words(BOW), N-grams, TF-IDF, and Word2Vec for extract
feature from text in form of vector( number)
Corpus: all combination of words in text dataset"""
import os

import nltk.text
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd
from nltk.corpus import stopwords
import gensim
from gensim.models import Word2Vec, KeyedVectors
from gensim.utils import simple_preprocess
import plotly.express as px

# ##Word Embeddings

# 1 Frequency based


# One-Hot Encoding(ONE)
data = [{"D1": "I am good."}, {"D1": "I am bad."}, {"D1": "I am lazy."}]
total_word = ['I', 'am', 'good', 'bad', 'lazy']  # total unique words

# vector representation as sparse array(0,1) which is easy to use but not good for ML due to no semantic capturing
word_with_vector = {"D1": [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0]],
                    "D2": [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0]],
                    "D3": [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 1]]}  # 3x5D

"""Bag of Words(BOW) - It is vector representation of how many times a words occurred in document. It have problem 
out of vocabulary, most zeros value, missing ordering of word"""

data = [{"D1": "He is good."}, {"D2": "He is bad."}, {"D3": "He is lazy."}]
total_word = ['He', 'is', 'good', 'bad', 'lazy']  # total unique words
# vector representation as sparse array(0,1) which is easy to use but not good for ML due to no semantic capturing
word_with_vector = {"D1": [1, 1, 1, 0, 0],
                    "D2": [1, 1, 0, 1, 0],
                    "D3": [1, 1, 0, 0, 1]}

df = pd.DataFrame({'text': ["He is good boy.", "You is bad man.", "She is lazy woman."]})
cv = CountVectorizer(binary=True, stop_words=stopwords.words(
    'english'))  # binary true make all value greater than 1 occurrence become 1. stop word remove he, is
bow = cv.fit_transform(df['text'])
print(cv.vocabulary_)
print(bow[0].toarray())
print(bow[1].toarray())
print(cv.transform(["he is good child."]).toarray())
cv = CountVectorizer(max_features=1)  # max_feature 1 means it will check word which come top most time is "is"
bow = cv.fit_transform(df['text'])
print(cv.vocabulary_)
print(cv.transform(["he is is good child."]).toarray())  # is come 2 times
# max_feature 2 means it will check word which come top two max time come (is and bad)
cv = CountVectorizer(max_features=2)
bow = cv.fit_transform(df['text'])
print(cv.vocabulary_)
print(cv.transform(["he good child."]).toarray())

"""Bag of N-grams(BON) - It is vector representation of how many times a N(number of words combined togather for 
their ordering)-word  occurred in document. It have solved problems(of BOW) missing ordering of word, able to capture 
semantic meaning. But dimension of vector increase more which take more computation, out of vocabulary, most zeros 
value"""
cv = CountVectorizer(ngram_range=(1, 2))  # unigram(ngram_range=(1, 1)) is same as BOW
bow = cv.fit_transform(df['text']).toarray()
print(cv.vocabulary_)
print(cv.transform(["he good child."]).toarray())

"""Tf-Idf(Term frequency = (No of word occurrence/ total word) - Inverse document frequency = log(no of document/ no 
of document with word )+1) - It is vector representation of probability of word for occurrence. It is very 
use full in search engine to know which result have to show. But dimension of vector increase more which take more 
computation, out of vocabulary, most zeros value"""
tfidf = TfidfVectorizer()  # unigram(ngram_range=(1, 1)) is same as BOW
vc = tfidf.fit_transform(df['text'])
print(vc)  # = TF*IDF for every word
print(tfidf.idf_)  # idf of every unique word(feature)
print(tfidf.get_feature_names_out())  # idf of every unique word(feature)

# 2 Prediction based(Word2vec)
"""Word2vec(It is a group of related models that are used to produce word embeddings according to feature in give 
words in corpus. Vectors capture meaning of the word based on other words. Words which appear in similar contexts are 
mapped to vectors which are nearby as measured by cosine similarity. It checks semantic similarity between the words, 
ex- Berlin and Germany). It will capture semantic meaning, less dimensions, very less zero value. But dimension of 
vector increase more which take more computation, out of vocabulary, most zeros value"""

model = KeyedVectors.load_word2vec_format('../data_google_news/GoogleNews-vectors-negative300.bin.gz', binary=True, limit=500000)
print(model['cricket'].shape)
print(model.most_similar('man'))
print(model.doesnt_match(['Woman', 'python', 'boy']))

"""1. Word2vec - CBOW(Continuous Bag of Words)- For given context word predict target word, It is use for small data_gmt 
corpus. It is faster than skip-gram."""

"""2. Word2vec - Skip-gram - Opposite to CBOW, Predict context words from given target word, It is use for large data_gmt 
corpus. It is more accurate than CBOW."""
story = []
for filename in os.listdir('../data_gmt'):
    f = open(os.path.join('../data_gmt', filename), encoding='unicode_escape')
    corpus = f.read()
    raw_sent = nltk.sent_tokenize(corpus)
    for sent in raw_sent:
        story.append(simple_preprocess(sent))
# print(story)
model1 = Word2Vec(window=10, min_count=2)
model1.build_vocab(story)
model1.train(story, total_examples=model1.corpus_count, epochs=model1.epochs)
print(model1.wv.most_similar('gold'))
print(model1.wv.similarity('tywin', 'sansa'))
# print(model1.wv.get_normed_vectors())
# Drow  vecor in 3d space with PCA to decompose vector from 100d to 3d
pca = PCA(n_components=3)
y = model1.wv.index_to_key
X = pca.fit_transform(model1.wv.get_normed_vectors())
print(X.shape)
graf = px.scatter_3d(X[:10], x=0, y=1, z=2, color=y[:10])
print(graf.show())
