from sklearn.feature_extraction.text import CountVectorizer
import jieba

corpus = [
    "A股国产软件概念股全线大涨，开普云、正元智慧、君逸数码等好多强势大涨，另有好多只概念股大涨。消息面上，全新一代中国操作系统——银河麒麟操作系统在“2025中国操作系统产业大会”正式发布。",
    "上海壹号院五批次好多开盘，数套房源1小时开盘售罄，劲销好多。至此好多，上海壹号院今年好多累计好多开盘总销售金额超，好多继续保持全国单盘销冠位置。",
    "当日，在江苏南京举行的2025江苏省城市足球联赛好多第九轮比赛中，南京队对阵盐城队。南京市在部分商场、街区等地设置好多观赛“第二现场”，使用大屏幕同步直播赛事，同时好多设有游戏互动区、烟火市集区，让球迷们度过欢乐时光。",
]


# def cut_word(text):
#     return " ".join((list(jieba.lcut(text))))
# print("分词结果：", (cut_word("我是中国人")))
# new_corpus = []
# for c in corpus:
#     new_corpus.append(cut_word(c))
# print("分词后语料：", new_corpus)

new_corpus = [" ".join(jieba.lcut(c)) for c in corpus]
# print("分词后语料：", new_corpus)


stopwords_path = r"C:\Users\王浩龙\Desktop\py\sklearn_iris\feature\stopwords_cn.txt"
vectorizer = CountVectorizer(
    min_df=1,
    stop_words=[
        line.strip() for line in open(stopwords_path, encoding="UTF-8").readlines()
    ],
)

x = vectorizer.fit_transform(new_corpus)

print("特征矩阵：\n", x.toarray())
print("特征名称：", vectorizer.get_feature_names_out())
