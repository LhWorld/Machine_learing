#coding:utf-8
import pandas as pd

# s1 = pd.Series(range(3),index=['a','b','c'])
#
# # 两种：1、在当前对象中删除数据。2、删除数据之后生成一个新的对象，原始对象不变
# # del(s1['c'])
# s2 = s1.drop('c')
# print(s2)
# print(s1)


#coding:utf-8
import numpy as np
from pandas import Series, DataFrame
from matplotlib.pyplot import *

#Series根据索引删除元素
obj = Series(np.arange(5.), index = ['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c')
print(new_obj)
print(obj.drop(['d', 'c']))
del(obj['c'])
print(obj)
#DataFrame删除元素，可指定索引或列。
data = DataFrame(np.arange(16).reshape((4, 4)),
                  index = ['beijing', 'shanghai', 'hangzhou', 'shenzhen'],
                  columns = ['one', 'two', 'three', 'four'])
del(data['one']) # del 和pop只能删除列，不能删除index。不能删除某一个元数
# data.pop('one')
data.ix['shanghai']['one']=99


print(data)
print(data.drop(['shanghai', 'hangzhou']))
print(data.drop('two', axis = 1)) # drop 第一个参数label相当于 index
print(data.drop(['two', 'four'], axis = 1))
# print(data.drop(columns='two'))