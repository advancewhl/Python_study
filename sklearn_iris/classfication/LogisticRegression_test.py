from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train, X_test)
X_test_scaled = scaler.transform(X_test)


LR = LogisticRegression()
LR.fit(X_train_scaled, y_train)
y_pred = LR.predict(X_test_scaled)

print("预测结果：\n", y_pred)
print("正确值:\n", y_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"测试集准确率·{accuracy:.2f}")
print(
    "分类报告：\n",
    classification_report(y_test, y_pred, target_names=iris.target_names),
)
