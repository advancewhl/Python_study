from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

a = np.array([2, 2, 4], dtype=np.float64)
# print('a:',a.dtype)
b = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float64)
# print('b:',b.dtype)
c = np.zeros((3, 4))
d = np.ones((3, 4))
e = np.empty((3, 4))
p = np.arange(12).reshape((3, 4))
# print('c:',c)
print('p:',p)
aa = np.linspace(1, 10, 5).reshape((5, 1))
print('aa:',aa)
a = np.array([[1, 2], [3, 4]])
b = np.arange(4).reshape((2, 2))
c = a - b
d = a**2
c = 10 * np.sin(a)
print(a)
print(b)
c = a.dot(b)
print(c)
a = np.random.random((2, 4))
print(a)
print(np.sum(a, axis=1))
print(a.sum(axis=1).reshape((2, 1)))
A = np.arange(10).reshape((2, 5))
print(np.argmin(A))
# 索引
print(np.mean(A))
print(np.median(A))
print(np.cumsum(A))
print(np.diff(A))
# 非零
print(np.nonzero(A))
# 排序
print(np.sort(A))
# 转置
print(np.transpose(A))
print((A.T).dot(A))
print(np.clip(A, 3, 8))
# 索引
B = np.arange(12).reshape(3, 4)
print(B)
# print(B[0])
# print(B[0][3])
# print(B[1,1])
# print(B[1,:])
for i in B.T:
    print(i)
for item in A.flat:
    print(item)
C = np.array([[1, 2, 3], [2, 4, 6]]).reshape(3, 2)
print(C)

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
print(np.vstack((A, B)))  # vertical stack
print(np.hstack((A, B)))  # horizaontal stack
print(A[:, np.newaxis])
C = np.concatenate((A, B, A), axis=0)
print(C)

A = np.arange(12).reshape(3, 4)
print(A)
print(np.split(A, 2, axis=1))
print(np.array_split(A, 3, axis=1))
print(np.vsplit(A, 3))
print(np.hsplit(A, 2))
