class Dog:
    d_type = "京巴"  # 类属性,类变量,所有实例共享
    ss = "sss"

    def __init__(self, name, age):  # 初始化方法，构造方法，实例化时自动调用
        print("a dog is born", name, age)
        self.name = name
        self.age = age

    def say_hi(self):  # 实例方法
        print(
            "hi, i am a dog,my type is",
            self.d_type,
            "my name is",
            self.name,
            "and my age is",
            self.age,
        )



d = Dog("ma", 3)  # 实例化
d2 = Dog("as", 4)

d.say_hi()  # 调用实例方法
d2.say_hi()
d.name="talon"

print(d.d_type, d.ss)
