#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: SGD_regressor.py
# Sklearn中定义的随机梯度下降实现
import numpy as np
from sklearn.linear_model import SGDRegressor

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

sgd_reg = SGDRegressor(n_iter=50, penalty=None, eta0=0.1) # n_iter 步长  penalty  惩罚系数 eta0 最舒适的学习率，学习率不断下降
# print(X)
# print(y.ravel())# 相当于flat 压扁压平  多行一列的数据压扁成一行。。。一个行向量。
sgd_reg.fit(X, y.ravel()) #因为这个函数需要的y是一个行向量，所以压扁。

print(sgd_reg.intercept_, sgd_reg.coef_) # intercept_ w0   coef_ w1,w2,w3多个参数。








