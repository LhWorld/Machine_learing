#coding:utf-8
import numpy as np

# list1=[1,2,3,4]
# a =np.array(list1)
# print(a**2)

a = np.random.randint(0,10,(3,2))
print(a)
b =np.arange(6).reshape((2,3))

# 计算两个矩阵相乘
print(a.dot(b))

# 矩阵的转置矩阵
print(a.T)

# 生成一个随机的bool矩阵，3 x 3

# c =np.random.randn(9).reshape((3,3))
# f1 =np.where(c>0,True,False)
#
# c2 =np.random.randn(9).reshape((3,3))
# f2 =np.where(c2>0,True,False)

# 根据f1 和 f2的值来获得一个新的矩阵，规则：f1 & f2 ，取值0, f1 true 1, f2 true 2 ，3

# print(np.where(f1 & f2 ,0,np.where(f1,1,np.where(f2,2,3))))

d =np.random.randn(100)
# 求矩阵中大于 0的和
print((d>0).sum())


n1 =np.random.randint(0,9,(3,3))

print(np.linalg.inv(n1))


