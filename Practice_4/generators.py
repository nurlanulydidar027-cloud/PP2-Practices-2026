#1. generators.py
def count_up(n):
    for i in range(1, n + 1):
        yield i

for num in count_up(5):
    print(num)  # 1, 2, 3, 4, 5


#2. generator for even numbers
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

print(list(even_numbers(10)))  # [0, 2, 4, 6, 8, 10]


#3. infinite generator
def infinite_counter():
    n = 0
    while True:
        yield n
        n += 1

gen = infinite_counter()
for _ in range(5):
    print(next(gen))  # 0, 1, 2, 3, 4



#4. generator for squares
def squares(n):
    for i in range(1, n + 1):
        yield i ** 2

print(list(squares(5)))  # [1, 4, 9, 16, 25]



#5. generator for Fibonacci numbers
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(7)))  # [0, 1, 1, 2, 3, 5, 8]