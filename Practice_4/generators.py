# 1. Generator that generates squares up to N
def squares_up_to(n):
    for i in range(1, n + 1):
        yield i ** 2

for val in squares_up_to(5):
    print(val)  # 1, 4, 9, 16, 25


# 2. Even numbers between 0 and n in comma separated form
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Input n: "))
print(",".join(str(x) for x in even_numbers(n)))


# 3. Numbers divisible by 3 and 4 between 0 and n
def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Input n: "))
for val in divisible_by_3_and_4(n):
    print(val)


# 4. Generator squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

for val in squares(2, 5):
    print(val)  # 4, 9, 16, 25


# 5. Generator from n down to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Input n: "))
for val in countdown(n):
    print(val)