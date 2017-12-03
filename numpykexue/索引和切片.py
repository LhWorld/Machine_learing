import  numpy as  np
a=np.random.randint(0,10,(6,4))
# print(a)
# print(a[2][1])# 第三行第二列
# print(a[2,1])# 第三行第二列
# print(a[[2,1]])# 第二三两行
# print(a[:3])# 第一到三行
#
# print(a[3,:3])# 取第四行一到三列
# print(a[-1:-3:-1,:-3])# 后两行 第四列
# print(a[[0,2,4],:-3])# 后两行 第四列
# print(a[[0,2,4],-3:])

# tile是矩阵级别的拷贝 copy矩阵级别的拷贝
# repart是元素级别的拷贝
# 1是行  0是列
# h = np.arange(12).reshape(3,4)
# print(h)
# # for i in h:
# #    print(i) #打印行  如果是三维矩阵 则打印二维
#
# for i in h.flat:
#        print(i)

# a = np.arange(5)
# print(a)
# a[:, np.newaxis]
# print(a)
# a[np.newaxis, :]
# print(a)


# a = np.arange(10).reshape(2,5)
# print(a)
# # print(a.ravel())
# print(a.resize(5,2))


b = np.arange(6).reshape(2,3)
c = np.ones((2,3))
print(b)
print(c)
d = np.hstack((b,c)) # hstack：horizontal stack 左右合并
print(d)
#
# e = np.vstack((b,c)) # vstack: vertical stack 上下合并
# print(e)
# f = np.column_stack((b,c))  # 左右合并column_stack
# g = np.row_stack((b,c))  # 上下合并column_stack
# print(g)
h = np.stack((b, c), axis=1)      # 按行合并
#print(h)
i = np.stack((b,c), axis=0)       # 按列合并
print(i)
j = np.concatenate ((b, c, c, b), axis=0)   #多个合并