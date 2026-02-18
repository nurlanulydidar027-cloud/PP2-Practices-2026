class Greeter:
    def say_hello(self, name):
        return f"Привет, {name}!"

g = Greeter()
print(g.say_hello("Боб"))   # Привет, Боб!


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

acc = BankAccount()
acc.deposit(500)
acc.deposit(200)
print(acc.get_balance())    # 700


class Temperature:
    unit = "Celsius"

    @classmethod
    def get_unit(cls):
        return cls.unit

print(Temperature.get_unit())  # Celsius


class MathHelper:
    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

print(MathHelper.is_prime(7))   # True
print(MathHelper.is_prime(10))  # False


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name.strip(), int(age.strip()))

    def __str__(self):
        return f"{self.name}, {self.age} лет"

p = Person.from_string("Мария, 30")
print(p)                    # Мария, 30 лет