from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    iris = load_iris()
print("数据集描述：", iris["DESCR"])
print("特征数据值", iris["data"])
print("特征名称", iris["feature_names"])
print("数据集形状", iris["data"].shape)
print("目标名称", iris["target_names"])
print("目标值", iris["target"])

x_train, x_test, y_train, y_test = train_test_split(
    iris.data,
    iris.target,
    test_size=0.2,
    train_size=None,
    random_state=None,
    shuffle=True,
    stratify=None,
)

print("训练集特征形状", x_train, x_train.shape)
print("测试集特征形状", x_test, x_test.shape)
print("训练集目标形状", y_train, y_train.shape)
print("测试集目标形状", y_test, y_test.shape)

