class Dog:
    role = "dog"

    def __init__(self, name, age, attack_val):
        self.name = name
        self.age = age
        self.attack_val = attack_val
        self.hp = 100

    def dog_attack(self, person):
        person.life_val -= self.attack_val
        print(
            "%s攻击了%s,%s掉了%s血,还剩%s血"
            % (self.name, person.name, person.name, self.attack_val, person.life_val)
        )

class Person:
    role = "person"

    def __init__(self, name, age, attack_val):
        self.name = name
        self.age = age
        self.attack_val = attack_val
        self.life_val = 100

    def person_attack(self, dog):
        dog.hp -= self.attack_val
        print(
            "%s攻击了%s,%s掉了%s血,还剩%s血"
            % (self.name, dog.name, dog.name, self.attack_val, dog.hp)
        )


d1 = Dog("旺财", 3, 20)
p1 = Person("小明", 18, 30)
p1.person_attack(d1)
d1.dog_attack(p1)
