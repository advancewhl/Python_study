class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwds):
        print("my name is %s, age is %s" % (self.name, self.age))


s = Student("mjj", 18)
s()  # 等同于s.__call__()
