#!/usr/bin/env python
# @Time    : 16-11-10 下午9:12
# @Author  : lizhenmxcz@163.com
# @Todo    : logistic regression classification

from numpy import *


def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('/home/workspace/dataset/Ch05/testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat


def sigmoid(inX):
    return 1.0/(1+exp(-inX))


def gradAscent(dataMatIn, classLabels):
    """梯度上升"""
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    m, n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n, 1))
    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights)
        error = (labelMat - h)
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights

def plotBestFit(wei):
    import matplotlib.pyplot as plt
    #weights = wei.getA()
    dataMat, labelMat = loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (- wei[0] - wei[1]*x) / wei[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


def stocGradAscent0(dataMatrix, classLabels):
    """随机梯度上升"""
    m, n = shape(dataMatrix)
    #dataM = mat(dataMatrix)
    alpha = 0.01
    weights = ones(n)
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i] * weights))
        error = classLabels[i] - h
        #print(alpha * error * array(dataMatrix[i]))
        #print(weights, dataMatrix[i])
        weights += alpha * error * array(dataMatrix[i])# should be array
    return weights


def stocGradAscent1(dataMatrix, classLabels, numInter=150):
    m, n = shape(dataMatrix)
    weights = ones(n)
    for j in range(numInter):
        dataIndex = list(range(m))
        for i in range(m):
            alpha = 4 / (1.0 + j + i) + 0.01
            randIndex = int(random.uniform(0, len(dataIndex)))
            h = sigmoid(sum(dataMatrix[randIndex] * weights))
            error = classLabels[randIndex] - h
            weights += alpha * error * array(dataMatrix[randIndex])
            del(dataIndex[randIndex])
    return weights

dataArr, labelMat = loadDataSet()
w = stocGradAscent1(dataArr, labelMat)
plotBestFit(w)
