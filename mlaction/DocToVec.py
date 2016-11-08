#!/usr/bin/env python
# @Time    : 16-11-8 下午10:13
# @Author  : lizhenmxcz@163.com
# @Todo    : doc to a vector

import scipy as sp
import numpy as np
from sklearn.datasets import load_files
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import  TfidfVectorizer


movie_reviews = load_files('/home/workspace/dataset/movie')
doc_terms_train, doc_terms_test, y_train, y_test\
    = train_test_split(movie_reviews.data, movie_reviews.target, test_size=0.3)

count_vec = TfidfVectorizer(binary=False, decode_error='ignore',
                            stop_words='english')
x_train = count_vec.fit_transform(doc_terms_train)
x_test = count_vec.transform(doc_terms_test)
x = count_vec.transform(movie_reviews.data)
y = movie_reviews.target
#print(doc_terms_train)
print(count_vec.get_feature_names())
#print(x_train.toarray())
#print(movie_reviews.target)