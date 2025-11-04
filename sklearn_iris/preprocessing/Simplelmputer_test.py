import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

# 创建示例数据，包含不同类型的问题
data = {
    "age": [25, 30, np.nan, 45, 60, 30, 15],  # 数值，含缺失值
    "salary": [
        50000,
        54000,
        60000,
        np.nan,
        100000,
        40000,
        20000,
    ],  # 数值，尺度大，含缺失值
    "country": ["USA", "UK", "China", "USA", "India", "China", "UK"],  # 分类型
    "gender": ["M", "F", "F", "M", "M", "F", "F"],  # 分类型
}

df = pd.DataFrame(data)
print("原始数据：\n", df)

imputer = SimpleImputer(strategy="mean")

numeric_feature = ["age", "salary"]

df_numeric = df[numeric_feature]

imputer.fit(df_numeric)

df[numeric_feature] = imputer.transform(df_numeric)

print("处理后的数据；\n", df)
