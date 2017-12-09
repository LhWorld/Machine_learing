#coding:utf-8
import pandas as pd

s1 = pd.Series(data=[1,2,4,6,7],index=['a','b','c','d','e'])
print(s1['a'])
print(s1[0])
print(s1[:3])
print(s1['a':'d']) # 范围是一个闭合
print(s1[['a','d']]) #


#coding:utf-8
# -*- coding: utf-8 -*-

from pandas import Series

#用数组生成Series ,默认情况下使用数字索引
obj = Series([4, 7, -5, 3])
print(obj)
print(obj.values)
print(obj.index)
print(obj.shape,obj.ndim)
print("-"*40)
#
#指定Series的index
obj2 = Series([4, 7, -5, 3], index = ['d', 'b', 'a', 'c'])
print(obj2)
print(obj2.index)
print(obj2['a'])
obj2['d']=6
print(obj2[:3]) # 数字的下标还存在，也可以分片
print(obj2[['c', 'a', 'd']]) #获取索引a,c,d的值
print(obj2[obj2 > 0])  # 找出大于0的元素
print('b' in obj2) # 判断索引是否存在
print('e' in obj2)
print("-"*40)

#使用字典生成Series
sdata = {'beijing':45000, 'shanghai':71000, 'guangzhou':16000, 'shengzheng':5000}
obj3 = Series(sdata)
print(obj3)
print("-"*40)

#使用字典生成Series，并额外指定index，不匹配部分为NaN。
states = ['hangzhou', 'shanghai', 'guangzhou','beijing']
obj4 = Series(sdata, index = states) # 索引重置
print(obj4)

#Series相加，相同索引部分相加。不相同的索引部分为NaN
print(obj3 + obj4)

#指定Series及其索引的名字
obj4.name = '我定义的名字'
obj4.index.name = 'index'
print(obj4)
print

#替换index
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)
