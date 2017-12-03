#coding:utf-8
import numpy as np

# 第一种方法创建数组
# list1 =[[1,2,3],[4,5,6]]
#
# a =np.array(list1)
#
# print(type(a))
# print(a.ndim) # 秩
# print(a.shape) # 每个维度的长度
# print(a.size) # 数组的所有元数的个数
# print(a.dtype)
# print(a)
# # a.dtype=np.float32
# a.shape=(3,2)
# print(a)

# 第二种方法创建数组 ，使用arange函数、random函数
# b =np.arange(16).reshape((2,2,2,2))
# print(b)

b =np.random.randint(0,100,(4,3))
print(b)

# 第三种种方法创建数组 ，使用ones,empty,zeros等函数
c = np.ones((3,3))
print(c)