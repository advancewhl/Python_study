from collections import Counter, defaultdict
import math


# 计算entropy
def entropy(label):
    total = len(label)
    counts = Counter(label)  # 记录每个类别的次数
    H = -sum(c / total * math.log2(c / total) for c in counts.values())
    return H


def information_gain(X, y, n):
    bas = entropy(y)
    total = len(y)
    parts = defaultdict(list)

    for i, row in enumerate(X):
        parts[row[n]].append(i)

    condition_entropy = 0.0
    for idxs in parts.values():
        sub_label = [y[i] for i in idxs]
        condition_entropy += (len(idxs) / total) * entropy(sub_label)
    return bas - condition_entropy


class ID3(object):
    def __init__(self, max_depth=None, min_sample_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_sample_split
        self.tree_ = {}

    def fit(self, X, y, feature_names=None):
        if feature_names is None:
            feature_names = list(X[0].keys())
        self.tree_ = self._build_tree(X, y, feature_names, depth=0)
        return self

    def _build_tree(self, X, y, features, depth):
        counter = Counter(y)

        if len(counter) == 1:
            return ("leaf", counter.most_common(1)[0][0])
        if not features or len(y) < self.min_samples_split:
            return ("leaf", counter.most_common(1)[0][0])
        if self.max_depth is not None and depth >= self.max_depth:
            return ("leaf", counter.most_common(1)[0][0])

        gains = [(attr, information_gain(X, y, attr)) for attr in features]
        best_attr, best_gain = max(gains, key=lambda t: t[1])
        if best_gain <= 0:
            return ("leaf", counter.most_common(1)[0][0])

        parts = defaultdict(lambda: ([], []))
        for row, label in zip(X, y):
            Xp, yp = parts[row[best_attr]]
            Xp.append(row)
            yp.append(label)

        remaining = [f for f in features if f != best_attr]

        node = ("node", best_attr, {})

        for val, (Xp, yp) in parts.items():
            child = self._build_tree(Xp, yp, remaining, depth + 1)
            node[2][val] = child
        return node
