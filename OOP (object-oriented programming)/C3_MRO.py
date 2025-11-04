class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")


class C(A):
    def show(self):
        print("C")


class B2:
    def show(self):
        print("B2")


class D(B, B2):
    # def show(self):
    #     print("D")
    pass


class C2:
    def show(self):
        print("C2")


class E(C, C2):
    # def show(self):
    #     print("E")
    pass


class F(D, E):
    # def show(self):
    #     print("F")
    pass


f = F()
f.show()
print(F.mro())
