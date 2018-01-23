#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: logistic_regression.py

import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

__author__ = 'yasaka'

iris = datasets.load_iris()
print(list(iris.keys()))
print(iris['DESCR'])
print(iris['feature_names'])

X = iris['data'][:, 3:]
# print(X)
print(iris['target'])
y = (iris['target'] == 2).astype(np.int)
print(y)

log_reg = LogisticRegression()
log_reg.fit(X, y)

X_new = np.linspace(0, 3, 1000).reshape(-1, 1)
print(X_new)
y_proba = log_reg.predict_proba(X_new)
y_hat = log_reg.predict(X_new)
print(y_proba)
print(y_hat)
plt.plot(X_new, y_proba[:, -1], 'g-', label='Iris-Virginica')
plt.plot(X_new, y_proba[:, 0], 'b--', label='Not Iris-Virginica')
plt.show()

print(log_reg.predict([[1.7], [1.5]]))
