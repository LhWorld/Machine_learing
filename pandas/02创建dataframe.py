#coding:utf-8
import pandas as pd
import numpy as np
# data = {'name':['zs','ls','ww'],
#         'age':[34,23,14]}
# df1 =pd.DataFrame(data)
#
# print(df1['age'][1])
# print(df1.ix[1]['age'])
# df1['age'].ix[1]=60
# print(df1)


# df2 =pd.DataFrame(np.arange(9).reshape((3,3)),columns=['col1','col2','col3'],index=['one','two','three'])
# print(df2)

# -*- coding: utf-8 -*-

import numpy as np
from pandas import Series, DataFrame

data = [1,2,3,4,5]
a = DataFrame(data)
print(a)


#用字典生成DataFrame，key为列的名字。'
data = {'state':['beijing', 'beijing', 'beijing', 'shangsha', 'shangsha'],
        'year':[2000, 2001, 2002, 2001, 2002],
        'pop':[1.5, 1.7, 3.6, 2.4, 2.9]}
print(DataFrame(data))
print(DataFrame(data, columns = ['year', 'state', 'pop'])) # 指定列顺序
print("-"*40)
#
# #指定索引，在列中指定不存在的列，默认数据用NaN。'
frame2 = DataFrame(data,
                    columns = ['year', 'state', 'pop', 'debt'],
                    index = ['one', 'two', 'three', 'four', 'five'])
print(frame2.ix['three']) # 一行值
print(frame2)
print(frame2['state'])  # 获取一列值，结果为一个series
print(frame2.ix['one'])
print(frame2.year)
print(frame2['pop'].ix['three'])
frame2['debt'] = 16.5 # 修改一整列
print(frame2)
frame2.debt = np.arange(5)  # 用numpy数组修改元素
print(frame2)
print("-"*40)

#用Series指定要修改的索引及其对应的值，没有指定的默认数据用NaN。'
val = Series([-1.2, -1.5, -1.7], index = ['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)
print("-"*40)
#
# #赋值给新列'
# frame2['eastern'] = (frame2.state == 'beijing')  # 如果state等于beijing为True
# print(frame2)
# print(frame2.columns)
# print("-"*40)
#
# #DataFrame转置'
pop = {'shangsha':{2001:2.4, 2002:2.9},
        'beijing':{2000:1.5, 2001:1.7, 2002:3.6}}
frame3 = DataFrame(pop)
print(frame3['2000':'2002'])
print(frame3)
print(frame3.T)
print("-"*40)

#指定索引顺序，以及使用切片初始化数据。'
print(DataFrame(pop, index = [2001, 2002, 2003]))
pdata = {'beijing':frame3['beijing'][:-1], 'shangsha':frame3['shangsha'][:2]}
print(DataFrame(pdata))
print("-"*40)

#指定索引和列的名称'
frame3.index.name = 'year'
frame3.columns.name = 'state'
print(frame3)
print(frame3.values)
