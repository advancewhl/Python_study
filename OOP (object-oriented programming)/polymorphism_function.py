class Dog(object):
    def sound(self):
        print("狗在叫")


class Cat(object):
    def sound(self):
        print("猫在叫")


def make_sound(animal_type):
    animal_type.sound()#函数实现多态

d1 = Dog()
c1 = Cat()
make_sound(d1)
make_sound(c1)
