class Dog(object):
    name = "dog"

    def __init__(self, name):
        self.name = name

    @classmethod  # 类方法
    def eat(self):
        print(self)
        print(f"{self.name}在吃东西")


d1 = Dog("mjj")
d1.eat()


class Student(object):
    __stu_num = []

    def __init__(self, name):
        self.name = name
        self.num(self)

    @classmethod
    def num(cls, stu):
        # stu = cls(name)
        if stu.name:
            if any(s.name == stu.name for s in cls.__stu_num):
                print(f"学生{stu.name}已经注册过了")
                return

            cls.__stu_num.append(stu)
            print(f"学生{stu.name}注册成功，当前一共有{len(cls.__stu_num)}名学生")


s1 = Student("mjj")
s2 = Student("zyy")
s3 = Student("zyy")
# Student.num("mjj")
