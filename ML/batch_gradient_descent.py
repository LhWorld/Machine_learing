#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: batch_gradient_descent.py

import numpy as np

__author__ = 'yasaka'

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)
X_b = np.c_[np.ones((100, 1)), X]
# print(X_b)

learning_rate = 0.22
n_iterations = 1000
m = 100

theta = np.random.randn(2, 1)
count = 0

for iteration in range(n_iterations):
    count += 1
    gradients = 1/m * X_b.T.dot(X_b.dot(theta)-y)
    theta = theta - learning_rate * gradients

print(count)
print(theta)









