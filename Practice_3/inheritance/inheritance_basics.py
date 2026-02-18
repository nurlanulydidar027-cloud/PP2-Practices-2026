class Animal:
    def breathe(self):
        return "Дышу воздухом"

class Dog(Animal):
    pass

d = Dog()
print(d.breathe())       # Дышу воздухом


class Animal:
    def eat(self):
        return "Ем еду"

class Cat(Animal):
    def purr(self):
        return "Мурр..."

c = Cat()
print(c.eat())           # Ем еду
print(c.purr())          # Мурр...


class Vehicle:
    pass

class Car(Vehicle):
    pass

car = Car()
print(isinstance(car, Car))      # True
print(isinstance(car, Vehicle))  # True
print(issubclass(Car, Vehicle))  # True


class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

s = Student("Иван")
print(s.name)            # Иван


class LivingThing:
    def is_alive(self):
        return True

class Animal(LivingThing):
    def move(self):
        return "Двигаюсь"

class Bird(Animal):
    def fly(self):
        return "Лечу"

b = Bird()
print(b.is_alive())      # True
print(b.move())          # Двигаюсь
print(b.fly())           # Лечу