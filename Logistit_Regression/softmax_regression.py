#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: softmax_regression.py
# softmax多分类
from sklearn import datasets
from sklearn.linear_model import LogisticRegression


iris = datasets.load_iris()
print(iris['DESCR'])
print(iris['feature_names'])
X = iris['data'][:, (2, 3)] #一般是选花瓣来做特征。
print(X)
y = iris['target'] #最终的分类号

softmax_reg = LogisticRegression(multi_class='multinomial', solver='sag', C=8, max_iter=1000)#采用的是多分类 c=8  L2正则中的阿尔法参数
#选用的是sag 随机梯度下降来求 Multionmial 是多分类   max_iter是迭代次数
softmax_reg.fit(X, y)
print(softmax_reg.predict([[5, 2]]))# soft_max是直接选定结果，根据概率大的。
print(softmax_reg.predict_proba([[5, 2]]))









