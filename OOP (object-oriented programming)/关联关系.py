class Person:
    def __init__(self, name, age, sex, relation):
        self.name = name
        self.age = age
        self.sex = sex
        self.parter = None
        self.relation = relation  # 存储关系对象

    def do_prite_stuff(self):
        pass


class RelationShip:
    """保存couple的关系"""

    def __init__(self):
        self.couple = []

    def makecouple(self, obj1, obj2):
        self.couple = [obj1, obj2]
        print("[%s]和[%s]确定了男女关系..." % (obj1.name, obj2.name))

    def get_my_parter(self, obj):
        print("找[%s]的对象" % obj.name)
        for i in self.couple:
            if i != obj:
                return i
        else:
            print("你没对象")


relation_obj1 = RelationShip()
p1 = Person("maaj", 24, "M", relation_obj1)
p2 = Person("lll", 23, "F", relation_obj1)


relation_obj1.makecouple(p1, p2)
p1.parter = p2
p2.parter = p1
print(p2.relation.couple)
print(p1.parter.name)

p2.parter = None
p1.parter = None


print(p1.relation.get_my_parter(p1).name)
