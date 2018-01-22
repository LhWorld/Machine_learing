#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: linear_regression_1.py

import numpy as np
from sklearn.linear_model import LinearRegression


X = 2 * np.random.rand(100, 1) # 随机取100个数，然后放到一列中去，是一个向量
y = 4 + 3 * X + np.random.randn(100, 1) # randn 正态分布，（1列100行） 3，预测值  所以这里是真实值

lin_reg = LinearRegression()
lin_reg.fit(X, y)
print(lin_reg.intercept_)
print(lin_reg.coef_)

X_new = np.array([[0], [2]])
print(lin_reg.predict(X_new))








