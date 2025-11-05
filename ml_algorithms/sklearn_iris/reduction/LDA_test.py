from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# 加载数据
iris = load_iris()
X, y = iris.data, iris.target
# 1. 标准化数据（至关重要！）
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# 2. 初始化LAD，保留2个维度
lda = LinearDiscriminantAnalysis(n_components=2)
# 3. 训练转换数据
X_lda = lda.fit_transform(X_scaled, y)
print("原始数据形状:", X.shape)
print("降维后数据:", X_lda)
