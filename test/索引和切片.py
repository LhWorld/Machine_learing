#coding:utf-8
import  numpy as np

a =np.random.randint(0,10,(6,4))
print(a)

# print(a[2][1]) # 第三行第二列
# print(a[2,1])
# print(a[[2,1]])
# print(a[:3]) # 第1到3行

print(a[3,:3]) # 取第4行，第1到3列
print(a[-2:,:3])   # 后2行，前3列
# 1、3、5，行的后3列
print(a[[0,2,4],-3:])
print(a[[0,2,4]][:,-3:])