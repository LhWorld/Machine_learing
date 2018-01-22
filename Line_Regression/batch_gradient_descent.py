#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: batch_gradient_descent.py

import numpy as np

X = 2 * np.random.rand(100, 1)  # 随机取100个数，然后放到一列中去，是一个向量
y = 4 + 3 * X + np.random.randn(100, 1)  # randn 正态分布，（1列100行） 3，预测值  所以这里是真实值
X_b = np.c_[np.ones((100, 1)), X]  # 相当于100行两列，第一列全是1 ，第二列是一个随机的数
# print(X_b)

learning_rate = 0.22 #学习率，步长
n_iterations = 1000  #迭代100次
m = 100  # 100行样本

theta = np.random.randn(2, 1)# 初始w值
count = 0

for iteration in range(n_iterations):# 0-999迭代
    count += 1
    gradients = 1/m * X_b.T.dot(X_b.dot(theta)-y)# 梯度 X_b.dot(theta)-y   是一个向量  X_b.T.dot乘以后面相当于矩阵的一个转置乘以一个向量相当于每一行会分别相乘加和。和
    theta = theta - learning_rate * gradients#每一次迭代，是一组数，相当于一组w参数都解出来了

print(count)
print(theta)









