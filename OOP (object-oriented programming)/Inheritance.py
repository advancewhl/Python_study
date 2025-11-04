class Animal:
    a_type = "哺乳动物"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print("%s is eating" % self.name)


class Person(Animal):
    a_type = "高等哺乳动物"

    def talk(self):
        print("person %s is talking" % self.name)

    def eat(self):
        print("人在优雅的吃")


class Dog(Animal):
    def chase_rabbit(self):
        print("狗%s在追兔子" % self.name)


d = Dog("zon", 11, "Fm")
d.eat()
d.chase_rabbit()
print(d.a_type)
p = Person("talon", 24, "m")
p.eat()
p.talk()
print(p.a_type)
