#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: SGD_regressor.py

import numpy as np
from sklearn.linear_model import SGDRegressor

__author__ = 'yasaka'

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

sgd_reg = SGDRegressor(n_iter=50, penalty=None, eta0=0.1)
print(X)
print(y.ravel())
sgd_reg.fit(X, y.ravel())

print(sgd_reg.intercept_, sgd_reg.coef_)








