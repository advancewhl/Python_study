from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "I love love machine learning",
    "Machine learning is fun",
    "I love coding in Python",
]

vectorizer = CountVectorizer(min_df=1, max_df=0.9, stop_words="english")

x = vectorizer.fit_transform(corpus)

print("特征矩阵：\n", x.toarray())
print("特征名称：", vectorizer.get_feature_names_out())
