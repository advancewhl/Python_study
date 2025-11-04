# 把一个方法变成一个静态的属性（不需要实例化对象就能访问的方法）
# class Studdent:
#     def __init__(self, name):
#         self.name = name

#     @property  # 把一个方法变成一个属性
#     def fly(self):
#         print(f"{self.name} can fly")


# stu1 = Studdent("mjj")
# stu1.fly  # 访问属性，不需要加括号


class Flight(object):
    def __init__(self, name):
        self.flight_name = name

    def checking_status(self):
        print("connecting airline compline api")
        print("checking flight %s status " % self.flight_name)
        return 1

    @property
    def flight_status(self):
        status = self.checking_status()
        if status == 0:
            print("flight got concelf")
        elif status == 1:
            print("flight  is arrived")
        elif status == 2:
            print("flight has departured already")
        else:
            print("cannot confrim the fight status please check later")

    @flight_status.setter
    def flight_status(self, status):
        print("changeing flight status", status)

    @flight_status.deleter
    def flight_status(self):
        print("del")


f = Flight("ASD1")
f.flight_status
f.flight_status = 0
del f.flight_status
