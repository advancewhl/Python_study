class Animal:
    a_type = "动物"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        print("Animal的init被调用")

    def eat(self):
        print(f"{self.name}在吃饭")


class Person(Animal):
    a_type = "人类"

    def __init__(self, name, age, sex, hobby):
        # Animal.__init__(self, name, age, sex)
        super().__init__(name, age, sex)
        self.hobby = hobby
        print("Person的init被调用")

    def talk(self):
        print(f"{self.name}在说话")

    def eat(self):
        # Animal.eat(self)
        super().eat()
        print(f"{self.name}在优雅的吃饭")


animal = Animal("pig", 3, "M")
animal.eat()
p1 = Person("talon", 12, "M", "game")
p1.eat()
print(p1.hobby)
