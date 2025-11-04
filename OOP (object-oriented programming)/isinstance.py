class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class junior(Student):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.hobby = hobby


s1 = Student("mjj", 18)
s2 = junior("zyy", 16, "basketball")
isinstance(s1, Student)  # True
isinstance(s1, junior)  # False
issubclass(junior, Student)  # True

