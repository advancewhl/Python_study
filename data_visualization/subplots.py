import matplotlib.pyplot as plt


input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

print(plt.style.available)
plt.style.use("seaborn-v0_8-dark-palette")
fig, ax = plt.subplots()
ax.plot(input_value, squares, linewidth=3)

# 设置图题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# 设置刻度标记的样式
ax.tick_params(labelsize=14)


plt.show()
