class Student(object):
    role = "student"

    def __init__(self, name):
        self.name = name

    @staticmethod  # 静态方法
    def fly(self):
        print("%s can fly" % self.name)


stu1 = Student("mjj")
stu1.fly(stu1)
