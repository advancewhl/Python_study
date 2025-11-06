# 采用SGD优化
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

eta_0 = 0.5


def fit(X, y, max_iter, eta=eta_0):
    w = np.random.randn(X.shape[1], 1)
    w_history = []  # 用来记录每次迭代的权重

    for i in range(max_iter):
        idx = np.random.choice(X.shape[0])
        x_radm = X[idx].reshape(-1, 1)
        y_radm = y[idx]
        gradient = (y_radm - np.dot(w.T, x_radm)) * x_radm
        w += eta * gradient

        # 记录每次迭代的 w 值
        w_history.append(w.copy())
    return w, w_history


# 设置模型的参数
w = 2.5  # 斜率
b = 1.0  # 偏置

# 生成随机的输入特征 X（例如，10个数据点）
X = np.random.rand(50, 1) * 10  # 生成0到10之间的随机数，作为输入特征
# 创建一个全是 1 的列（大小与 X 的行数相同）
ones_column = np.ones((X.shape[0], 1))

# 将 X 和 ones_column 水平堆叠成增广矩阵
augmented_matrix = np.hstack((ones_column, X))

# 根据模型计算标签 y
# 添加噪声：随机生成一些误差模拟现实数据中的波动
noise = np.random.randn(50, 1)  # 正态分布噪声
y = w * X + b + noise  # 生成真实的标签

# 执行拟合
w_final, w_history = fit(augmented_matrix, y, 150, eta=0.001)

# 获取拟合后的模型参数
b_train = w_final[0][0]  # 偏置
w_train_slope = w_final[1][0]  # 斜率


rcParams["font.family"] = "Microsoft YaHei"  # 如果是 Windows 用户，可以尝试 'Microsoft YaHei'
# 绘制数据点和拟合的直线
plt.scatter(X, y, color="blue", label="真实数据")
plt.plot(X, w_train_slope * X + b_train, color="red", label="拟合直线")

# 添加标签和标题
plt.xlabel("X")
plt.ylabel("y")
plt.title("线性回归拟合效果")
plt.legend()

# 使用非阻塞模式显示图形
plt.show(block=False)


# 现在，绘制 w[0] 和 w[1] 的变化过程

# 转换为 numpy 数组（方便绘图）
w_history = np.array(w_history).squeeze()

# 创建两个子图展示 w[0] 和 w[1] 的变化
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

# 绘制偏置变化（w[0]）
ax1.plot(w_history[:, 0], label="Bias (w[0])", color="blue")
ax1.set_xlabel("Iteration")
ax1.set_ylabel("Bias Value")
ax1.set_title("Evolution of Bias (w[0]) during SGD")
ax1.legend()

# 绘制斜率变化（w[1]）
ax2.plot(w_history[:, 1], label="Slope (w[1])", color="red")
ax2.set_xlabel("Iteration")
ax2.set_ylabel("Slope Value")
ax2.set_title("Evolution of Slope (w[1]) during SGD")
ax2.legend()

# 调整图像布局，避免重叠
plt.tight_layout()

# 使用非阻塞模式显示图形
plt.show()

# 打印最终的 w 值
print(f"Final w: {w_final}")
