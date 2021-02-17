# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class MyComplex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return complex(self.a * other.a, self.b * other.b)


c1 = MyComplex(2, -5)
c2 = MyComplex(4, 2)

print(c1 + c2)
print(c1 * c2)
