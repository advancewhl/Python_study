import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler

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

imputer = SimpleImputer(strategy="mean")

numeric_feature = ["age", "salary"]

df_numeric = df[numeric_feature]

imputer.fit(df_numeric)

df[numeric_feature] = imputer.transform(df_numeric)


minmax_scale = MinMaxScaler()
df_numeric = df[["age", "salary"]]
minmax_scale.fit(df_numeric)
df_normalized = minmax_scale.transform(df_numeric)
print("归一化的数据：\n", df_normalized)
