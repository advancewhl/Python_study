class Dog:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master
        self.sayhi()

    def sayhi(self):
        print(
            "hi,i am a dog,my name is",
            self.name,
            "my age is",
            self.age,
            "my master is",
            self.master.name,
        )


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk_dog(self, dog):
        print("%s遛%s" % (self.name, dog.name))


p1 = Person("小明", 18)
d1 = Dog("旺财", 3, p1)
p1.walk_dog(d1)
