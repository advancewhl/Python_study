from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
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
)
# 处理缺失值
imputer = SimpleImputer(strategy="mean")
numeric_feature = ["age", "salary"]
df_numeric = df[numeric_feature]
imputer.fit(df_numeric)
df[numeric_feature] = imputer.transform(df_numeric)

# 标准化
standar_scale = StandardScaler()
df_numeric = df[["age", "salary"]]
standar_scale.fit(df_numeric)
df_standardization = standar_scale.transform(df_numeric)
print("标准化的数据：\n", df_standardization)
print(df_standardization.var(axis=0))
