class Empty:
    pass

obj = Empty()
print(type(obj))         # <class '__main__.Empty'>


class Dog:
    species = "dog"

    def bark(self):
        return "Woof!"

d = Dog()
print(d.species)         # dog
print(d.bark())          # Woof!

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(calc.add(3, 4))       # 7
print(calc.multiply(3, 4))  # 12


class Color:
    def __str__(self):
        return "My favorite color is blue"

c = Color()
print(c)          


class Point:
    pass

p = Point()
p.x = 10
p.y = 20
print(p.x, p.y)          # 10 20