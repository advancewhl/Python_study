from sklearn.preprocessing import OneHotEncoder
import numpy as np

# 示例类别数据
data = [["red"], ["blue"], ["green"], ["blue"], ["red"]]

# 初始化 OneHotEncoder
# handle_unknown='ignore' 防止遇到未知类别时报错
encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")  # sparse 稀疏

# 学习并转换数据
# fit() ：用于从训练数据生成学习模型参数
# transform()：从fit()方法生成的参数，应用于模型以生成转换数据集。
# fit_transform()：在同一数据集上组合fit()和transform() api
x_encoded = encoder.fit_transform(data)
print("编码结果：\n", x_encoded)
print("编码后的特征名称：", encoder.get_feature_names_out())

# 处理新数据（包含未知类别 ‘Yellow’）
new_data = [["blue"], ["red"], ["yellow"]]
X_new_encoded = encoder.transform(new_data)
print("\n新数据编码后的特征矩阵:")
print(X_new_encoded)
