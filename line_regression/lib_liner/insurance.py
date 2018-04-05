#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: insurance.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model


data = pd.read_csv('../data/insurance.csv')
print(type(data))
print(data.head())
print(data.tail())
# describe做简单的统计摘要
print(data.describe())
# 采样要均匀
data_count = data['age'].value_counts()
print(data_count)
data_count[:10].plot(kind='bar')#切片操作，取前10个，画直方图
plt.show()

print(data.corr())#皮尔逊相关系数 +1正相关 -1负相关 不能仅根据相关系数就把维度去掉

reg = linear_model.LinearRegression()
x = data[['age', 'sex', 'bmi', 'children', 'smoker', 'region']]
y = data['charges']
#python3.6 报错 sklearn ValueError: could not convert string to float: 'northwest'，加入一下几行解决
x = x.apply(pd.to_numeric, errors='coerce')
y = y.apply(pd.to_numeric, errors='coerce')
x.fillna(0, inplace=True)#如果碰到空值就转换成0
y.fillna(0, inplace=True)#如果碰到空值就转换成0

reg.fit(x, y)
print(reg.coef_)
print(reg.intercept_)
