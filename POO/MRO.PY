class A:
    def who_am_i(self):
        return "I am A"


class B(A):
    def who_am_i(self):
        return "I am B"


class C(A):
    def who_am_i(self):
        return "I am C"


class D(B, C):  # Hereda de B y C
    pass


d = D()

print(d.who_am_i())  # ¿Qué imprime?
print(D.__mro__)  # Orden de resolución de métodos
