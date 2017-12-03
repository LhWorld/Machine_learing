#coding:utf-8
# t=(1,2,3)
# list1 =[1,2,3,4,4,4,4]
# l =list(t)
# print(l)
#
# s = set(list1)
# t1 =tuple(list1)
# print(s,t1)
#
#
# a =1
# a =2

# str ="abcefg"
# # str[2] = 'x'
#
# list1 =[i for i in range(10)]
#
# # 两个for循环是嵌套
# tuple1 =[(i,j) for i in range(1,5) for j in range(6,10)]
# print(list1)
# print(tuple(list1))
#
# # 生成一个[[1,2,3],[4,5,6]....]的列表最大值在100以内
#
# list2 =[[i+1,i+2,i+3] for i in range(100) if i%3==0]

m =[[1,2,3],[4,6,6],[7,8,9]]
n =[[2,2,2],[3,3,3],[4,4,4]]
# 两个矩阵相乘.第一个矩阵的行乘以第二个矩阵列

result = [ m[r][c]*n[c][r] for r in range(3) for c in range(3) ]

print(result)

