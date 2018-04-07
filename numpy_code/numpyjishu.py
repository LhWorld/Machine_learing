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

# import numpy as np
# a = np.dtype(np.int_)     #  np.int64, np.float32 …
# print(a)

# import numpy as np
# a = np.dtype('i8')   # ’f8’, ‘i4’’c16’,’a30’(30个字符的字符串), ‘>i4’…
# print (a)
# import numpy as np
# a = np.array([[1,2,3], [4, 5, 6]], dtype=int)
# print(a.shape)       #  a.ndim, a.size, a.dtype
#
# import numpy as np
# a = np.array([(1,2,3), (4, 5, 6)], dtype=float)
# print(a.shape)      #  a.ndim, a.size, a.dtype
# import numpy as np
# a = np.arange(10).reshape(2, 5) # 创建2行5列的二维数组，
# # 也可以创建三维数组，
# c = np.arange(12).reshape(2,3,2)
# a = np.array([[[1,2,3], [4, 5, 6], [7, 8, 9]]])
# b = np.array([[[1,2,3]], [[4, 5, 6]], [[7, 8, 9]]])
# print(a.shape)
# print(b.shape)
# import numpy as np
a = np.random.random(6)
b = np.random.rand(6)
# c = np.random.randn(6)
# print(a-b)                    # print(a+b),print(a*c) …

# d=np.random.randn(10)
# print(d)
# print((d>0).sum())
# d = np.random.random((2,3))
# e = np.random.randn(2, 3)
# f = np.random.rand(2,3)
# print(d-e)                    # print(d+f),print(e*f) …
# print(np.dot(a,b))          #复习矩阵乘法
# print(a.dot(b))
# import numpy as np
# a = np.ones((2,3))
# b = np.zeros((2,3))
# a*=3
# b+=a
# print(a)
# print(b)
# import numpy as np
# a = np.arange(10)
# np.where()
# import numpy as np
# #增加维度
# a = np.arange(5)
# print(a[:, np.newaxis])
# print(a[np.newaxis, :])
# print(np.tile([1,2], 2))
a = np.arange(10).reshape(2,5)
# print(a)
# print(a.ravel())
# print(a.resize(5,2))
# b = np.arange(6).reshape(2,3)
# c = np.ones((2,3))
# d = np.hstack((b,c))
# print(b)
# print(c)
# print(d)# hstack：horizontal stack 左右合并
# e = np.vstack((b,c))
# print(e)# vstack: vertical stack 上下合并
# f = np.column_stack((b,c))
# g = np.row_stack((b,c))
# h = np.stack((b, c), axis=1)      # 按行合并
# i = np.stack((b,c), axis=0)       # 按列合并
# j = np.concatenate ((b, c, c, b), axis=0)   #多个合并
k = np.hsplit(a, 2)
print(k)
# l = np.vsplit(i, 2)
# m = np.split(i, 2, axis=0)
# n = np.split(i, 2,axis=1)