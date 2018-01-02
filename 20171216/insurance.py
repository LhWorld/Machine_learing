#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: insurance.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

__author__ = 'yasaka'

data = pd.read_csv('./data/insurance.csv')
print(type(data))
print(data.head())
print(data.tail())
# describe做简单的统计摘要
print(data.describe())
# 采样要均匀
data_count = data['age'].value_counts()
print(data_count)
data_count[:10].plot(kind='bar')
# plt.show()

print(data.corr()) # corr 皮尔逊相关系数

reg = linear_model.LinearRegression() # 相当于给一组参数 W全为零 但是没有调整
x = data[['age', 'sex', 'bmi', 'children', 'smoker', 'region']]
y = data['charges']
#python3.6 报错 sklearn ValueError: could not convert string to float: 'northwest'，加入一下几行解决
x = x.apply(pd.to_numeric, errors='coerce')# 函数里面传一个函数进去
y = y.apply(pd.to_numeric, errors='coerce')
x.fillna(0, inplace=True)
y.fillna(0, inplace=True)

reg.fit(x, y)
print(reg.coef_) #对应w1...wn
print(reg.intercept_) # 对应w0 截距
