from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

news = fetch_20newsgroups(subset="all")

X_train, X_test, y_train, y_test = train_test_split(
    news.data, news.target, test_size=0.2
)

tfidfVectorizer = TfidfVectorizer()
X_train_scaled = tfidfVectorizer.fit_transform(X_train)
X_test_scaled = tfidfVectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
print("模型预测值:", y_pred)
print("正确值:", y_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"测试集准确率:{accuracy:.2f}")
print(
    "分类报告:\n", classification_report(y_test, y_pred, target_names=news.target_names)
)
