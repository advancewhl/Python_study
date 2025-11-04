class ShenXianBase:
    def fight(self):
        print("原始神仙会打架")


class ShenXian(ShenXianBase):
    def fly(self):
        print("我会飞")

    # def fight(self):
    #     print("神仙会打架")


class MokeyBase:
    def fight(self):
        print("猿猴会打架")


class Mokey(MokeyBase):
    def eat_peach(self):
        print("猴子喜欢吃桃子")

    def fight(self):
        print("猴子会打架")


class MokeyKing(ShenXian, Mokey):
    def play_goden_stick(self):
        print("孙悟空喜欢玩金箍棒")


wukong = MokeyKing()
wukong.eat_peach()
wukong.play_goden_stick()
wukong.fly()
wukong.fight()#不是真正的深度优先
