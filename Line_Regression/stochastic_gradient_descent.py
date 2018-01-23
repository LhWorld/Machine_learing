#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: stochastic_gradient_descent.py
#自定义的随机批量梯度下降实现方式
import numpy as np


X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)
X_b = np.c_[np.ones((100, 1)), X]
# print(X_b)

n_epochs = 50
t0, t1 = 5, 50  # 超参数

m = 100


def learning_schedule(t):
    return t0 / (t + t1)

theta = np.random.randn(2, 1) #初始一组w值

for epoch in range(n_epochs): # 50次 0-50
    for i in range(m): #100次 0-99
        random_index = np.random.randint(m) #随机取一行，拿到这一行的标号
        xi = X_b[random_index:random_index+1] #取这行的所有X值，切片左闭右开
        yi = y[random_index:random_index+1]#取这行的Y值
        gradients = 2*xi.T.dot(xi.dot(theta)-yi)#（误差-真实值）*这一行的x值
        learning_rate = learning_schedule(epoch*m + i) #epoch*m+i越来越大 带到上面函数中，学习率越来越小 让步长越来越小 不会随机太大
        theta = theta - learning_rate * gradients

print(theta)
#PS 总结：迭代次数多了，但每一次迭代不用加和，每一次的迭代计算小了





