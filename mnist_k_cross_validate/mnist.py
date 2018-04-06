#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: mnist_k_cross_validate.py

from sklearn.datasets import fetch_mldata
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.base import clone
from sklearn.model_selection import cross_val_score
from sklearn.base import BaseEstimator #评估指标
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier


# Alternative method to load MNIST, if mldata.org is down
from scipy.io import loadmat #利用Matlib加载本地数据
mnist_raw = loadmat("mnist-original.mat")
mnist = {
    "data": mnist_raw["data"].T,
    "target": mnist_raw["label"][0],
    "COL_NAMES": ["label", "data"],
    "DESCR": "mldata.org dataset: mnist_k_cross_validate-original",
}
print("Success!")
# mnist_k_cross_validate = fetch_mldata('MNIST_original', data_home='test_data_home')
print(mnist)

X, y = mnist['data'], mnist['target'] # X 是70000行 784个特征 y是70000行 784个像素点
print(X.shape, y.shape)
#
some_digit = X[36000]
print(some_digit)
some_digit_image = some_digit.reshape(28, 28)#调整矩阵 28*28=784 784个像素点调整成28*28的矩阵 图片是一个28*28像素的图片 每一个像素点是一个rgb的值
print(some_digit_image)
#
plt.imshow(some_digit_image, cmap=matplotlib.cm.binary,
           interpolation='nearest')
plt.axis('off')
plt.show()
#
X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[:60000]#6/7作为训练，1/7作为测试
shuffle_index = np.random.permutation(60000)#返回一组随机的数据 shuffle 打乱60000中每行的值 即每个编号的值不是原先的对应的值
X_train, y_train = X_train[shuffle_index], y_train[shuffle_index] # Shuffle之后的取值
# #
y_train_5 = (y_train == 5)# 是5就标记为True,不是5就标记为false
y_test_5 = (y_test == 5)
print(y_test_5)
#这里可以直接写成LogGression
sgd_clf = SGDClassifier(loss='log', random_state=42)# log 代表逻辑回归 random_state或者random_seed 随机种子 写死以后生成的随机数就是一样的
sgd_clf.fit(X_train, y_train_5)#构建模型
print(sgd_clf.predict([some_digit]))# 测试模型 最终为5
# #
### K折交叉验证
##总共会运行3次
skfolds = StratifiedKFold(n_splits=3, random_state=42)# 交叉验证 3折 跑三次 在训练集中的开始1/3 中测试，中间1/3 ，最后1/3做验证
for train_index, test_index in skfolds.split(X_train, y_train_5):
    #可以把sgd_clf = SGDClassifier(loss='log', random_state=42)这一行放入进来，传不同的超参数 这里就不用克隆了
    clone_clf = clone(sgd_clf)# clone一个上一个一样的模型 让它不变了 每次初始随机参数w0,w1,w2都一样，所以设定随机种子是一样
    X_train_folds = X_train[train_index]#对应的是训练集中训练的X 没有阴影的
    y_train_folds = y_train_5[train_index]# 对应的是训练集中的训练y 没有阴影的
    X_test_folds = X_train[test_index]#对应的是训练集中的测试的X 阴影部分的
    y_test_folds = y_train_5[test_index]#对应的是训练集中的测试的Y 阴影部分的

    clone_clf.fit(X_train_folds, y_train_folds)#构建模型
    y_pred = clone_clf.predict(X_test_folds)#验证
    print(y_pred)
    n_correct = sum(y_pred == y_test_folds)# 如若预测对了加和 因为true=1 false=0
    print(n_correct / len(y_pred))#得到预测对的精度 #用判断正确的数/总共预测的 得到一个精度
# #PS：这里可以把上面的模型生成直接放在交叉验证里面传一些超参数比如阿尔法，看最后的准确率则知道什么超参数最好。

#这是Sk_learn里面的实现的函数cv是几折，score评估什么指标这里是准确率，结果类似上面一大推代码
print(cross_val_score(sgd_clf, X_train, y_train_5, cv=3, scoring='accuracy')) #这是Sk_learn里面的实现的函数cv是几折，score评估什么指标这里是准确率


class Never5Classifier(BaseEstimator):#给定一个分类器，永远不会分成5这个类别 因为正负列样本不均匀，所以得出的结果是90%，所以只拿精度是不准确的。
    def fit(self, X, y=None):
        pass

    def predict(self, X):
        return np.zeros((len(X), 1), dtype=bool)


never_5_clf = Never5Classifier()
print(cross_val_score(never_5_clf, X_train, y_train_5, cv=3, scoring='accuracy'))#给每一个结果一个结果
# #
# #
##混淆矩阵 可以准确地知道哪一个类别判断的不准
y_train_pred = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3)#给每一个结果预测一个概率
print(confusion_matrix(y_train_5, y_train_pred))
# #
y_train_perfect_prediction = y_train_5
print(confusion_matrix(y_train_5, y_train_5))
#准确率，召回率，F1Score
print(precision_score(y_train_5, y_train_pred))
print(recall_score(y_train_5, y_train_pred))
print(sum(y_train_pred))
print(f1_score(y_train_5, y_train_pred))

sgd_clf.fit(X_train, y_train_5)
y_scores = sgd_clf.decision_function([some_digit])
print(y_scores)

threshold = 0 # Z的大小 wT*x的结果
y_some_digit_pred = (y_scores > threshold)
print(y_some_digit_pred)

threshold = 200000
y_some_digit_pred = (y_scores > threshold)
print(y_some_digit_pred)

y_scores = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3, method='decision_function')
print(y_scores)#直接得出Score

precisions, recalls, thresholds = precision_recall_curve(y_train_5, y_scores)
print(precisions, recalls, thresholds)


def plot_precision_recall_vs_threshold(precisions, recalls, thresholds):
    plt.plot(thresholds, precisions[:-1], 'b--', label='Precision')
    plt.plot(thresholds, recalls[:-1], 'r--', label='Recall')
    plt.xlabel("Threshold")
    plt.legend(loc='upper left')
    plt.ylim([0, 1])


# plot_precision_recall_vs_threshold(precisions, recalls, thresholds)
# plt.savefig('./temp_precision_recall')

y_train_pred_90 = (y_scores > 70000)
print(precision_score(y_train_5, y_train_pred_90))
print(recall_score(y_train_5, y_train_pred_90))


fpr, tpr, thresholds = roc_curve(y_train_5, y_scores)


def plot_roc_curve(fpr, tpr, label=None):
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.axis([0, 1, 0, 1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True positive Rate')


plot_roc_curve(fpr, tpr)
plt.show()
# plt.savefig('img_roc_sgd')

print(roc_auc_score(y_train_5, y_scores))

forest_clf = RandomForestClassifier(random_state=42)
y_probas_forest = cross_val_predict(forest_clf, X_train, y_train_5, cv=3, method='predict_proba')
y_scores_forest = y_probas_forest[:, 1]

fpr_forest, tpr_forest, thresholds_forest = roc_curve(y_train_5, y_scores_forest)
plt.plot(fpr, tpr, 'b:', label='SGD')
plt.plot(fpr_forest, tpr_forest, label='Random Forest')
plt.legend(loc='lower right')
plt.show()
# plt.savefig('./img_roc_forest')

print(roc_auc_score(y_train_5, y_scores_forest))

#
#
