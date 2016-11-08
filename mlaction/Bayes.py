#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/8 14:29
# @Author  : lizhenmxcz@163.com
# @File    : Bayes.py
# @Todo    : use bayes to classify

from numpy import *


def loadDataSet():
    """ create the dataset """
    postingList = [['my', 'dog', 'has', 'flea', 'problem', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'grabage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
                   ]
    classVec = [0, 1, 0, 1, 0, 1]
    return postingList, classVec


def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            location = vocabList.index[word]
            returnVec[location] = 1
        else:
            print("the word %s is not in my Vocabulary!" % word)
    return returnVec


def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = zeros(numWords)
    p1Num = zeros(numWords)
    p0Denom = 0.0
    p1Denom = 0.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom == sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom == sum(trainMatrix[i])
    p1Vect = p1Num/p1Denom
    p0Vect = p0Num/p0Denom
    return p0Vect, p1Vect, pAbusive


def createTrainMat(postList, vocabList):
    trainMats = []
    for post in postList:
        trainMats.append(setOfWords2Vec(vocabList, post))
    return trainMats
postingList, classVec = loadDataSet()
vocablist = createVocabList(postingList)
trainMat = createTrainMat(postingList, vocablist)
p0V, p1V, pAb = trainNB0(trainMat, classVec)
print(pAb)
print(p0V)
print(p1V)



