#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: linear_regression_0.py

import numpy as np
import matplotlib.pyplot as plt

__author__ = 'yasaka'

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)
X_b = np.c_[np.ones((100, 1)), X] #这里是一个组合矩阵，相当于一列全是1，另一列是一个随机出来的数 100行2列的矩阵。
# print(X_b)

# 常规等式求解theta
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y) #解析解得实现方式，自己实现的 dot是点积的意思
print(theta_best)

# X_new = np.array([[0], [2]])
# X_new_b = np.c_[(np.ones((2, 1))), X_new]
# print(X_new_b)
# y_predict = X_new_b.dot(theta_best)
# print(y_predict)
#
# plt.plot(X_new, y_predict, 'r-')
# plt.plot(X, y, 'b.')
# plt.axis([0, 2, 0, 15])
# plt.show()



