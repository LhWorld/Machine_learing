#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: elastic_net.py
# elastic_net函数
import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import SGDRegressor


X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)
#两种方式实现Elastic_net
elastic_net = ElasticNet(alpha=0.1, l1_ratio=0.5)
elastic_net.fit(X, y)
print(elastic_net.predict(1.5))

sgd_reg = SGDRegressor(penalty='elasticnet')
sgd_reg.fit(X, y.ravel())
print(sgd_reg.predict(1.5))




