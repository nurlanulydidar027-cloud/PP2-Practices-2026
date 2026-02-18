class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # вызываем Animal.__init__
        self.breed = breed

d = Dog("Рекс", "Лабрадор")
print(d.name, d.breed)   # Рекс Лабрадор



class Shape:
    def describe(self):
        return "Я — фигура"

class Circle(Shape):
    def describe(self):
        parent = super().describe()
        return f"{parent}, а точнее — круг"

c = Circle()
print(c.describe())      # Я — фигура, а точнее — круг



class Employee:
    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

m = Manager("Анна", 90000, "IT")
print(m.name, m.salary, m.department)  # Анна 90000 IT



class A:
    def hello(self):
        return "A"

class B(A):
    def hello(self):
        return super().hello() + "B"

class C(B):
    def hello(self):
        return super().hello() + "C"

print(C().hello())       # ABC



class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

class TimestampLogger(Logger):
    def log(self, message):
        super().log(message)
        print("[TIMESTAMP] 2024-01-01")

tl = TimestampLogger()
tl.log("Старт")
# [LOG] Старт
# [TIMESTAMP] 2024-01-01