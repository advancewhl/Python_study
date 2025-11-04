from sklearn.feature_selection import f_classif, SelectKBest
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
print(X)
selector = SelectKBest(score_func=f_classif, k=3)
X_new = selector.fit_transform(X, y)
print(X_new)
print(f"原始特征数：{X.shape[1]}")
print(f"筛选后特征数:{X_new.shape[1]}")
print(f"各特征得分：{selector.scores_}")
