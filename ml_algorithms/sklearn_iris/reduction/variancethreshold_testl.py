from sklearn.datasets import load_iris
from sklearn.feature_selection import VarianceThreshold

X, y = load_iris(return_X_y=True)

selector = VarianceThreshold(threshold=0.5)
X_new = selector.fit_transform(X)

print(f"原始特征数: {X.shape[1]}")
print(f"筛选后特征数: {X_new.shape[1]}")
