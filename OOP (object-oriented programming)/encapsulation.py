class Person(object):
    def __init__(self, name, age, sex):
        self.name = name  # 实例变量
        self.age = age
        self.sex = sex
        self.__life_val = 100  # 私有变量
        self.__breath()

    def get_life_val(self):
        print(f"生命值还有{self.__life_val}")
        return self.__life_val

    def __breath(self):  # 私有方法
        print(f"{self.name}正在呼吸")

    def got_attack(self):
        self.__life_val -= 20
        print(f"生命值被攻击还剩{self.__life_val}")
        return self.__life_val


p1 = Person("talon", 23, "M")
p1.get_life_val()
life_val = p1.got_attack()
# p1._Person__breath()
print(life_val)
