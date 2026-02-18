class Flyable:
    def fly(self):
        return "Лечу!"

class Swimmable:
    def swim(self):
        return "Плыву!"

class Duck(Flyable, Swimmable):
    pass

d = Duck()
print(d.fly())           # Лечу!
print(d.swim())          # Плыву!


class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

class JSONUser(JSONMixin, User):
    pass

u = JSONUser("Алиса", 25)
print(u.to_json())       # {"name": "Алиса", "age": 25}


class A:
    def hello(self):
        return "A"

class B(A):
    def hello(self):
        return "B"

class C(A):
    def hello(self):
        return "C"

class D(B, C):
    pass

print(D().hello())       # B  (сначала идёт B по MRO)
print(D.__mro__)         # (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, ...)


class Logger:
    def log(self):
        print("Запись в лог")

class Notifier:
    def notify(self):
        print("Отправка уведомления")

class Service(Logger, Notifier):
    def run(self):
        self.log()
        self.notify()

Service().run()
# Запись в лог
# Отправка уведомления



class Base:
    def greet(self):
        return "Base"

class Left(Base):
    def greet(self):
        return "Left → " + super().greet()

class Right(Base):
    def greet(self):
        return "Right → " + super().greet()

class Child(Left, Right):
    def greet(self):
        return "Child → " + super().greet()

print(Child().greet())   # Child → Left → Right → Base