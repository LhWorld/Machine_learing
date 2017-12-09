#coding:utf-8
import matplotlib.pyplot as plt
import  numpy as np

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# 需要两点的坐标数据
# data = np.array([0,0,1,1]).reshape((2,2))

# ng = np.arange(0,6,0.01) # 角度：2*pi的倍数
#
# d = np.cos(2*np.pi*ng);
#
#
# plt.plot(ng,d)
#
# plt.title('第一张图片')
# plt.xlabel('x轴')
# plt.ylabel('y轴')
#
# plt.show()

# 第三个例子
# 1D data
x = [1,2,3,4,5]
y = [2.3,3.4,1.2,6.6,7.0]

plt.figure(figsize=(12,6)) # figure 相当于画布。figsize：画布的比例大小，12:6

plt.subplot(231) # 在画布有一个子画布 。画布的布局为：2行3列。子画布为第一个
plt.plot(x,y)
plt.title("plot")

plt.subplot(232)
plt.scatter(x, y) #散布图；散点分析
plt.title("scatter")

plt.subplot(233)
plt.pie(y)
plt.title("pie")

plt.subplot(234)
plt.bar(x, y)
plt.title("bar")

# 2D data
import numpy as np
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
print(x)
# meshgrid函数通常在数据的矢量化上使用，meshgrid的作用适用于生成网格型数据，可以接受两个一维数组生成两个二维矩阵，对应两个数组中所有的(x,y)对
X, Y = np.meshgrid(x, y)  # 网格坐标生成函数
print(X)
Z    = Y**2 + X**2

plt.subplot(235)
plt.contour(X,Y,Z) #画等高线
plt.colorbar()
plt.title("contour")


plt.show()