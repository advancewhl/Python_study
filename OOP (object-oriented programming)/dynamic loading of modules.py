# __import__("reflection") 解释器用的
import importlib

importlib.import_module("class_method")  # 官方推荐


class User:
    def login(self):
        print("welcome")

    def register(self):
        print("register")

    def save(self):
        print("save")


user = User()
while 1:
    choose = input(">>>").strip()
    if hasattr(user, choose):
        func = getattr(user, choose)
        func()
    else:
        print("no this func")
    break
