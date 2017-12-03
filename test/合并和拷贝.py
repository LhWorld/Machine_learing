#coding:utf-8
import  numpy as np
a= np.arange(9).reshape((3,3))
b =np.random.randint(0,10,(3,3))

# print(np.hstack((a,b)))
# print(np.vstack((a,b)))

# print(np.tile(a,2)) # tile矩阵级别的拷贝
print(np.repeat(a,2,1)) # repeat元数级别的拷贝