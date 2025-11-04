# 可以通过字符串的形式来操作一个对象的属性
# getattr hasatter setatter delatter
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print("person %s is walking" % self.name)


def talk(self):
    print(self.name, "is talking")


p = Person("add", 12)

# if hasattr(p, "name"):
#     print("exist name")

# # getattr
# a = getattr(p, "age")
# print(a)
# user_command = input(">>:").strip()
# if hasattr(p, user_command):
#     func = getattr(p, user_command)
#     func()
# # else:
# #     pass

# # setattr
# # #static属性
# setattr(p, "sex", "Female")
# print(p.sex)
# # #method方法
# setattr(Person, "speak", talk)
# p.speak()

# # delattr
# delattr(p, "age")

# 反射一个文件下的属性
# 在当前模块为__main__
# 只会在被其它模块导入的时候发挥作用
if __name__ == "__main__":
    print("hahah")
import sys

print(sys.modules["__main__"])
mod = sys.modules[__name__]
if hasattr(mod, "p"):
    o = getattr(mod, "p")
    o.walk()
