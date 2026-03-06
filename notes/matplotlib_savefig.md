# Matplotlib `plt.savefig` 说明

## `fname` 路径参数
- `fname` 是保存目标文件的路径或文件名，后缀决定默认格式（如 `.png`、`.pdf`）。
- 可以使用相对路径（相对于当前工作目录）或绝对路径。
- **`plt.savefig` 不会自动创建目录**，保存前请确保目标文件夹已存在（例如使用 `Path("figures").mkdir(parents=True, exist_ok=True)`）。

## 常用可选参数
- `dpi`：输出分辨率；论文或演示文稿可用 300 及以上。
- `bbox_inches`：`"tight"` 时自动收紧空白边距。
- `pad_inches`：与 `bbox_inches` 配合控制边距大小。
- `transparent`：`True` 时背景透明。
- `format`：强制指定输出格式（通常让后缀自动决定即可）。

## 示例
```python
import matplotlib.pyplot as plt
from pathlib import Path

# 确保保存目录存在
Path("figures").mkdir(parents=True, exist_ok=True)

# ... 绘制图形 ...

plt.savefig(
    "figures/scatter_demo.png",  # 保存到相对路径（文件夹需已存在）
    dpi=300,
    bbox_inches="tight",
    pad_inches=0.1,
    transparent=False,
)
```
