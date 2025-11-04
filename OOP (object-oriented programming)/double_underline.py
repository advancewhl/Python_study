class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __len__(self):
        print("执行了len")
        return 2

    def __hash__(self):
        print("执行了hash")
        return 2

    def __eq__(self, value):
        print("执行了eq")
        return self.name == value.name and self.age == value.age


p1 = Person("whl", 12)
p2 = Person("whl", 11)
print(len(p1))
print(hash(p1))
print(p1 == p2)


class School(object):
    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):
        print("执行了getitem", self.__dict__[item])

    def __setitem__(self, key, value):
        print("执行了setitem")
        self.__dict__[key] = value
        # raise AttributeError("不能设置属性")

    def __delitem__(self, key):
        print("执行了delitem")
        del self.__dict__[key]

    def __delattr__(self, item):
        print("执行了delattr")
        del self.__dict__[item]


school = School("atguigu")
print(school["name"])  # 调用__getitem__
school["name"] = "oldboy"  # 实现__setitem__
print(school.name)
# del school["name"]  # 实现__delitem__
del school.name  # 实现__delattr__


# 重要得
# 字符串表示方法 __str__  __repr__
class School(object):
    def __init__(self, name, add, type):
        self.name = name
        self.add = add
        self.type = type

    def __repr__(self):
        return "School name:%s,add:%s,type:%s" % (self.name, self.add, self.type)

    def __str__(self):
        return "name:%s,add:%s,type:%s" % (self.name, self.add, self.type)


school_1 = School("oldboy", "beijing", "training")
print(school_1)  # 默认调用__str__方法
print(repr(school_1))  # 调用__repr__方法
print(str(school_1))  # 调用__str__方法
# 返回字符串，string用于用户交互，repr用于开发者调试,str没被定义则用repr


# 析构方法 对象消逝的时候执行
class School(object):
    def __init__(self, name, add, type):
        self.name = name
        self.add = add
        self.type = type

    def __del__(self):
        print("del school objcet")


s1 = School("sss", "111", 111)
