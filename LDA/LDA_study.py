# -*- coding: utf-8 -*-

import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation


for i in range(4):
    with open('./data/nlp_test%d.txt' % i, encoding='UTF-8') as f:
        document = f.read()

        document_cut = jieba.cut(document)
        result = ' '.join(document_cut)
        print(result)
        with open('./data/nlp_test%d.txt' % (i+10), 'w', encoding='UTF-8') as f2:
            f2.write(result)
    f.close()
    f2.close()


# 从文件导入停用词表
stpwrdpath = "./data/stop_words.txt"
stpwrd_dic = open(stpwrdpath, 'r', encoding='UTF-8')
stpwrd_content = stpwrd_dic.read()
# 将停用词表转换为list
stpwrdlst = stpwrd_content.splitlines()
stpwrd_dic.close()
print(stpwrdlst)


# 向量化 不需要tf_idf
corpus = []
for i in range(4):
    with open('./data/nlp_test%d.txt' % (i+10), 'r', encoding='UTF-8') as f:
        res = f.read()
        corpus.append(res)
    print(res)

cntVector = CountVectorizer(stop_words=stpwrdlst)
cntTf = cntVector.fit_transform(corpus)
print(cntTf)

# 打印输出对应关系
# 获取词袋模型中的所有词
wordlist = cntVector.get_feature_names()
# 元素a[i][j]表示j词在i类文本中的权重
weightlist = cntTf.toarray()
# 打印每类文本的词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
for i in range(len(weightlist)):
    print("-------第", i, "段文本的词语权重------")
    for j in range(len(wordlist)):
        print(wordlist[j], weightlist[i][j])

lda = LatentDirichletAllocation(n_components=3,#3个话题
                                learning_method='batch',
                                random_state=0)
docres = lda.fit_transform(cntTf)

print("文章的主题分布如下：")
print(docres)
print("主题的词分布如下：")
print(lda.components_)
