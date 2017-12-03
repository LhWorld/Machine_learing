#coding:utf-8

import numpy as np
# c=np.ones((3,3))
# print(1)

# a=np.random.randint(0,10,(3,2))
# b=np.arange(6).reshape(2,3)
# print(a.dot(b))

# c=np.random.randn(9).reshape(3,3)
# f1=np.where(c>0,True,False)
# print(f1)
# c2=np.random.randn(9).reshape(3,3)
# f2=np.where(c2>0,True,False)
# print(f2)
# print(np.where(f1&f2,0,np.where(f1,1,np.where(f2,2,3))))



d=np.random.randn(10)
print(d)
print((d>0).sum())