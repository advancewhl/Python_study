class Scudent(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("执行了init方法")

    def __new__(cls, *args, **kwargs):
        # 负责执行__init__方法
        instance = super().__new__(cls)
        print("执行了new方法", cls, args, kwargs)
        return instance


p1 = Scudent("whl", 12)


# 设计模式 单例模式
class Printer(object):
    tasks = []
    instance = None

    def __init__(self, name):
        self.name = name

    def add_task(self, job):
        print(f"打印机{self.name}添加了任务{job}")
        self.tasks.append(job)
        print(f"当前任务列表{self.tasks}")

    def __new__(cls, *arg, **kwargs):
        # 只有第一次实例化的时候，正常进行，后面每次实例化，并不会创建新的对象
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


p1 = Printer("Word app")
p2 = Printer("Excel app")
p3 = Printer("Pdf app")
p1.add_task("打印word文档")
p2.add_task("打印Excel表格")
p3.add_task("打印PDF文件")
print(p1, p2, p3)
