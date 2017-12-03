#coding:utf-8
import numpy as np
# a =np.arange(9).reshape((3,3))
# print(a)
# print(a.sum())
# print(a.sum(1)) # 行相加1,列相加0
#
# print(a[0].sum())

a =np.arange(9)
b =np.arange(9)
print(np.concatenate((a,b)))
print(np.hstack((a,b)))
