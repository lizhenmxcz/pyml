#!/usr/bin/env python
# @Time    : 16-11-21 下午9:46
# @Author  : lizhenmxcz@163.com
# @Todo    :adaboost to improve the classfication performence


import numpy as np


def loadSimpData():
    datMat = np.matrix([[1., 2.1],
                        [2., 1.1],
                        [1.3, 1.],
                        [1., 1.],
                        [2., 1.]])
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return datMat, classLabels


def stumpClassify(dataMatrix, dimen, threshVal, threashIneq):
    retArray = np.ones((np.shape(dataMatrix[0]), 1))
    if threashIneq == 'lt':
        retArray[dataMatrix[:dimen] <= threshVal] = -1.0
    else:
        retArray[dataMatrix[:dimen] > threshVal] = -1.0
    return retArray

def buildStump(dataArr, classLabels, D):
    dataMatrix = np.mat(dataArr)
    labelMat = np.mat(classLabels).T
    m, n = np.shape(dataMatrix)
