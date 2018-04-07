
import numpy as np

# b = np.arange(20).reshape(5,4)
# b[2,3]
# b[0:5, 1]
# b[ : ,1]
# b[1:3, : ]
# b = np.arange(20).reshape(5,4)
# print(b)
# # print(b[2,3])
# # print(b[0:5, 1])
# # print(b[ : ,1])
# # print(b[1:3, : ])
# print(b[-1])
# c = np.arange(12).reshape(2,3,2)
# print(c)
# c[1]
# c[2,1]    # 等价于c[2][1]
# c[2,1,1]  # 等价于c[2][1][1]
# 通过布尔数组索引
# f = np.arange(12).reshape(3, 4)
# print(f)
# g = f>4
# print(g)
# print(f [g])
# h = np.arange(12).reshape(3,4)
# print(h)
# for i in h:
#    print(i)
# for i in h.flat:
#        print(i)
import numpy as np
a = np.array([[1,2], [3, 4], [5, 6]])

print(a.flatten())
b = np.mat([[1,2,3], [4, 5, 6]])
print(b)
b.flatten()
# c = [[1,2,3], [4, 5, 6]]
# c.flatten()
# 多维数组的索引
# # print(a)
# # print(a[2][1])# 第三行第二列
# # print(a[2,1])# 第三行第二列
# # print(a[[2,1]])# 第二三两行
# # print(a[:3])# 第一到三行
# #
# # print(a[3,:3])# 取第四行一到三列
# # print(a[-1:-3:-1,:-3])# 后两行 第四列
# # print(a[[0,2,4],:-3])# 后两行 第四列
# # print(a[[0,2,4],-3:])
#
# # tile是矩阵级别的拷贝 copy矩阵级别的拷贝
# # repart是元素级别的拷贝
# # 1是行  0是列
# # h = np.arange(12).reshape(3,4)
# # print(h)
# # # for i in h:
# # #    print(i) #打印行  如果是三维矩阵 则打印二维
# #
# # for i in h.flat:
# #        print(i)
#
# # a = np.arange(5)
# # print(a)
# # a[:, np.newaxis]
# # print(a)
# # a[np.newaxis, :]
# # print(a)
#
#
# # a = np.arange(10).reshape(2,5)
# # print(a)
# # # print(a.ravel())
# # print(a.resize(5,2))
#
#
# b = np.arange(6).reshape(2,3)
# c = np.ones((2,3))
# print(b)
# print(c)
# d = np.hstack((b,c)) # hstack：horizontal stack 左右合并
# print(d)
# #
# # e = np.vstack((b,c)) # vstack: vertical stack 上下合并
# # print(e)
# # f = np.column_stack((b,c))  # 左右合并column_stack
# # g = np.row_stack((b,c))  # 上下合并column_stack
# # print(g)
# h = np.stack((b, c), axis=1)      # 按行合并
# #print(h)
# i = np.stack((b,c), axis=0)       # 按列合并
# print(i)
# j = np.concatenate ((b, c, c, b), axis=0)   #多个合并