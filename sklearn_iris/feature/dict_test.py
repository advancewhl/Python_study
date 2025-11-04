from sklearn.feature_extraction import DictVectorizer

data = [
    {"age": 25, "city": "New York", "income": 50000},
    {"age": 30, "city": "Boston", "income": 65000},
    {"age": 35, "city": "New York", "income": 75000},
]

vectorizer = DictVectorizer(sparse=True)
 
X = vectorizer.fit_transform(data)
print("特征矩阵：\n", X)
print("特征名称：", vectorizer.get_feature_names_out())
