class Dog:
    role = "dog"

    def __init__(self, name, breed, attack_val):
        self.name = name
        self.breed = breed
        self.attack_val = attack_val
        self.life_val = 100

    def bite(self, person):
        person.life_val -= self.attack_val
        print(
            "狗[%s]咬了人[%s],人掉血[%s],还剩血量[%s]"
            % (self.name, person.name, self.attack_val, person.life_val)
        )


class Person:
    role = "person"

    def __init__(self, name, sex, attack_val):
        self.name = name
        self.attack_val = attack_val
        self.life_val = 100
        self.sex = sex
        self.wepon = Weapon()  # 直接实例化

    def attack(self, dog):
        dog.life_val -= self.attack_val
        print(
            "人[%s]打了狗[%s]，狗掉血[%s]，还剩血量[%s]"
            % (self.name, dog.name, self.attack_val, dog.life_val)
        )


class Weapon:
    def dog_stick(self, obj):
        """打狗棒"""
        self.name = "打狗棒"
        self.attack_val = 40
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def knife(self, obj):
        """屠龙刀"""
        self.name = "屠龙刀"
        self.attack_val = 80
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def gun(self, obj):
        """ak47"""
        self.name = "ak47"
        self.attack_val = 100
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def print_log(self, obj):
        print(
            "[%s]被[%s]攻击了，掉血[%s],还剩血量[%s]"
            % (obj.name, self.name, self.attack_val, obj.life_val)
        )


d = Dog("zzz", "erha", 50)
p = Person("taoln", "M", 50)
d.bite(p)
p.wepon.gun(d)
