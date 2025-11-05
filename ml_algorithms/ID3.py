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
