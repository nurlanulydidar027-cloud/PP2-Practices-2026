class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу!"

print(Dog().speak())     # Гав!
print(Cat().speak())     # Мяу!


class Product:
    def __init__(self, name, price):
        self.name  = name
        self.price = price

    def __str__(self):
        return f"{self.name} — {self.price} руб."

p = Product("Книга", 350)
print(p)                 # Книга — 350 руб.


class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14159 * self.radius ** 2, 2)

shapes = [Square(4), Circle(3)]
for s in shapes:
    print(s.area())      # 16, затем 28.27


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)
print(p1 == p2)          # True
print(p1 == p3)          # False


class Vehicle:
    def info(self):
        return "Это транспортное средство"

class ElectricCar(Vehicle):
    def info(self):
        base = super().info()
        return f"{base} (электрическое)"

ec = ElectricCar()
print(ec.info())         # Это транспортное средство (электрическое)