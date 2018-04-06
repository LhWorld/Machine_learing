import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import math
from sklearn.preprocessing import StandardScaler


df = pd.read_csv('iris.data')
print(df.head())


#手动加上列名称
df.columns = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
print(df.head())

X = df.ix[:, 0:4].values#切片操作 ,逗号左边所有行，逗号右边所有列
y = df.ix[:, 4].values
print(y)

label_dict = {
    1: 'Iris-setosa',
    2: 'Iris-versicolor',
    3: 'Iris-virginica'
}

feature_dict = {
    0: 'sepal length [cm]',
    1: 'sepal width [cm]',
    2: 'petal length [cm]',
    3: 'petal width [cm]'
}

#把原始数据画图
plt.figure(figsize=(8, 6))
for cnt in range(4):#0,1,2,3
    plt.subplot(2, 2, cnt+1)#画哪一张图
    for lab in ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'):
        plt.hist(X[y == lab, cnt],#直方图 y==lab 判断是否等于 cnt
                 label=lab,
                 bins=10,
                 alpha=0.3,)#alpha透明度
    plt.xlabel(feature_dict[cnt])
    plt.legend(loc='upper right', fancybox=True, fontsize=8)

plt.tight_layout()
plt.show()

X_std = StandardScaler().fit_transform(X)#方差归一化，均值归一化
print(X_std)

mean_vec = np.mean(X_std, axis=0)#均值均值 axis=0是代表横向的
cov_mat = (X_std - mean_vec).T.dot((X_std - mean_vec)) / (X_std.shape[0] - 1)#协方差公式
print('Covariance matrix \n%s' % cov_mat)#协方差矩阵
print('Numpy covariance matrix: \n%s' % np.cov(X_std.T))#numpy自带的公式

eig_values, eig_vectors = np.linalg.eig(cov_mat)
print('Eigenvectors \n%s' % eig_vectors)#特征向量
print('Eigenvalues \n%s' % eig_values)#特征值

#构建二元组，特征值和特征向量构成的二元组
eig_pairs = [(np.abs(eig_values[i]), eig_vectors[:, i]) for i in range(len(eig_values))]
print(eig_pairs)
print('----------------')

eig_pairs.sort(key=lambda x: x[0], reverse=True)
print('Eigenvalues in descending order:')
for i in eig_pairs:
    print(i[0])

tot = sum(eig_values)
var_exp = [(i / tot) * 100 for i in sorted(eig_values, reverse=True)]
print(var_exp)
cum_var_exp = np.cumsum(var_exp)#累加 把特征值得占比进行累加
print(cum_var_exp)

plt.figure(figsize=(6, 4))
plt.bar(range(4), var_exp, alpha=0.5, align='center', label='cumulative explained variance')
plt.ylabel('Explained variance ratio')
plt.xlabel('Principal components')
plt.legend(loc='best')
plt.tight_layout()
plt.show()

matrix_w = np.hstack((
    eig_pairs[0][1].reshape(4, 1),#特征值第一的
    eig_pairs[1][1].reshape(4, 1)#特征值第二的
))
print('Matrix W:\n', matrix_w)

new_X = X_std.dot(matrix_w)
print(new_X)#相乘得到一个新的矩阵降维


#原始图
plt.figure(figsize=(6, 4))
for lab, col in zip(('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'),#zip函数 拼接键值对
                    ('blue', 'red', 'green')):
    plt.scatter(X[y == lab, 0],
                X[y == lab, 1],
                label=lab,
                c=col)
plt.xlabel('sepal_len')
plt.ylabel('sepal_wid')
plt.legend(loc='best')
plt.tight_layout()
plt.show()
#最终做了一个旋转 维度整合了不是新的花瓣花萼额度
plt.figure(figsize=(6, 4))
for lab, col in zip(('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'),
                    ('blue', 'red', 'green')):
    plt.scatter(new_X[y == lab, 0],
                new_X[y == lab, 1],
                label=lab,
                c=col)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(loc='lower center')
plt.tight_layout()
plt.show()
