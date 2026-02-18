class Person:
    def __init__(self, name):
        self.name = name

p = Person("Алиса")
print(p.name)            # Алиса


class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year  = year

car = Car("Toyota", 2022)
print(car.brand, car.year)  # Toyota 2022


class Counter:
    def __init__(self, start=0):
        self.count = start

c1 = Counter()
c2 = Counter(100)
print(c1.count, c2.count)   # 0 100


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area   = 3.14159 * radius ** 2

circle = Circle(5)
print(round(circle.area, 2))  # 78.54


class Basket:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

basket = Basket()
basket.add("яблоко")
basket.add("груша")
print(basket.items)      # ['яблоко', 'груша']