class Dog:
    species = "Canis lupus familiaris"  # переменная класса

d1 = Dog()
d2 = Dog()
print(d1.species)    # Canis lupus familiaris
print(d2.species)    # Canis lupus familiaris


class Robot:
    count = 0  # переменная класса

    def __init__(self):
        Robot.count += 1

Robot()
Robot()
Robot()
print(Robot.count)   # 3


class Cat:
    legs = 4            # переменная класса

    def __init__(self, name):
        self.name = name  # переменная экземпляра

c = Cat("Мурка")
print(Cat.legs)      # 4  (доступ через класс)
print(c.legs)        # 4  (наследуется экземпляром)
print(c.name)        # Мурка


class Circle:
    pi = 3.14159

    def area(self, r):
        return self.pi * r * r

c1 = Circle()
c2 = Circle()
c2.pi = 3.14   # создаёт переменную экземпляра, не меняет класс
print(c1.area(5))   # 78.53975 (использует Circle.pi)
print(c2.area(5))   # 78.5     (использует c2.pi)


class Config:
    debug = False

a = Config()
b = Config()

Config.debug = True   # меняем через класс
print(a.debug)        # True
print(b.debug)        # True