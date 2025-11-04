class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("mjj", 12)
print(type(p1))
print(type(Person))

dog_class = type("Dog", (object,), {"name": "dog", "age": 3})
print(dog_class)
d1 = dog_class()
print(d1.name)
