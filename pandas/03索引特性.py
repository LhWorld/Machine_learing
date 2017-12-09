#coding:utf-8
import pandas as pd

# s1 = pd.Series(range(3),index=['a','b','c'])
# print(s1)
# # s1[2]='e'
#
# s1.index=['e','f','g']
# print(s1)

# -*- coding: utf-8 -*-

import numpy as np
import sys
from pandas import Series, DataFrame, Index

#获取index
obj = Series(range(3), index = ['a', 'b', 'c'])
index = obj.index
print(index[1:])
# index[1] = 'd'  # index对象read only ,但是可以重新构建索引
obj.index=['e','f','g']
print(obj)
#使用Index对象
index = Index(np.arange(3))
obj2 = Series([1.5, -2.5, 0], index = index)
print(obj2)
print(obj2.index is index)

#'判断列和索引是否存在
pop = {'Nevada':{20001:2.4, 2002:2.9},
        'Ohio':{2000:1.5, 2001:1.7, 2002:3.6}}
frame3 = DataFrame(pop)
print('Ohio' in frame3.columns)
print('2003' in frame3.index)
