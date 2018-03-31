#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: logistic_regression01.py

import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
from time import time

__author__ = 'yasaka'

iris = datasets.load_iris()
print(list(iris.keys()))
print(iris['DESCR'])
print(iris['feature_names'])

X = iris['data'][:, 3:]
# print(X)
print(iris['target'])
y = iris['target']
# y = (iris['target'] == 2).astype(np.int)
print(y)


# Utility function to report best scores
def report(results, n_top=3):
    for i in range(1, n_top + 1):
        candidates = np.flatnonzero(results['rank_test_score'] == i)
        for candidate in candidates:
            print("Model with rank: {0}".format(i))
            print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
                  results['mean_test_score'][candidate],
                  results['std_test_score'][candidate]))
            print("Parameters: {0}".format(results['params'][candidate]))
            print("")

'''
start = time()
param_grid = {"tol": [1e-4, 1e-3, 1e-2],
              "C": [0.4, 0.6, 0.8]}#两个超参数
log_reg = LogisticRegression(multi_class='multinomial', solver='lbfgs')
grid_search = GridSearchCV(log_reg, param_grid=param_grid, cv=3)#交叉验证 3折交叉验证 通过GridSearchCV来找到最好的超参数的组合 9中组合来找到最好的
grid_search.fit(X, y)
print("GridSearchCV took %.2f seconds for %d candidate parameter settings."
      % (time() - start, len(grid_search.cv_results_['params'])))
report(grid_search.cv_results_)
'''

X_new = np.linspace(0, 3, 1000).reshape(-1, 1)
print(X_new)

#  multi_class =multi_class对应的是多分类 就相当于选择使用SoftMax函数，Ovr是二分类 默认是二分类
# solver 算法
# C 正则化系数  越小越看中正则化
# solver默认用的是libliner
log_reg = LogisticRegression(multi_class='multinomial', solver='lbfgs', C=0.8, tol=0.01)
log_reg.fit(X, y)
print("model Coefficient (%s)" % log_reg.intercept_, log_reg.coef_)#intercept截距 w0 coef w1--wn 参数
y_proba = log_reg.predict_proba(X_new)
y_hat = log_reg.predict(X_new)#预测的三个概率值为1，因为这里是相当于softmax
print(y_proba)
print(y_hat)

plt.plot(X_new, y_proba[:, 2], 'g-', label='Iris-Virginica')
plt.plot(X_new, y_proba[:, 1], 'r-', label='Iris-Versicolour')
plt.plot(X_new, y_proba[:, 0], 'b--', label='Iris-Setosa')
plt.show()

print(log_reg.predict([[1.7], [1.5]]))


