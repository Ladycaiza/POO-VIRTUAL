class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    pass

class A:
    def hablar(self):
        print("Hola desde A")

class C(A):
    def hablar(self):
        print("Hola desde C")

class D(B,C):
    def hablar(self):
        print("Hola desde D ")

d = D()
d.hablar()

