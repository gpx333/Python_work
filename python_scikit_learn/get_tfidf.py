# coding=utf-8
import codecs
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

'''
sklearn里面的TF-IDF主要用到了两个函数：CountVectorizer()和TfidfTransformer()。 
    CountVectorizer是通过fit_transform函数将文本中的词语转换为词频矩阵。 
    矩阵元素weight[i][j] 表示j词在第i个文本下的词频，即各个词语出现的次数。 
    通过get_feature_names()可看到所有文本的关键字，通过toarray()可看到词频矩阵的结果。 
    TfidfTransformer也有个fit_transform函数，它的作用是计算tf-idf值。 
'''

def main():
    corpus = []  # 文档语料 空格连接

    # 读取语料 一行语料为一个文档
    for line in open('../python_dealdata/nefu_news.txt', 'r', encoding='utf-8').readlines():
        print(line)
        corpus.append(line.strip())
    # time.sleep(5)

    # 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
    vectorizer = CountVectorizer()

    # 该函数会统计每个词语的tf-idf权值
    transformer = TfidfTransformer()

    # 第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))

    # 获取词袋模型中的所有词语
    word = vectorizer.get_feature_names()

    # 将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
    weight = tfidf.toarray()

    resName = "Tfidf_nefu_news.txt"
    result = codecs.open(resName, 'w', encoding='utf-8')
    for j in range(len(word)):
        result.write(word[j] + ' ')
    result.write('\r\n\r\n')

    # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for遍历某一类文本下的词语权重
    for i in range(len(weight)):
        print(u"-------这里输出第", i, u"条新闻的词语tf-idf权重------")
        for j in range(len(word)):
            result.write(str(weight[i][j]) + ' ')
        result.write('\r\n\r\n')
    result.close()


main()
