numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)           # [2, 4, 6, 8, 10]


words = ["python", "lambda", "map"]
uppercased = list(map(lambda w: w.upper(), words))
print(uppercased)        # ['PYTHON', 'LAMBDA', 'MAP']


fruits = ["apple", "banana", "kiwi", "mango"]
lengths = list(map(lambda f: len(f), fruits))
print(lengths)           # [5, 6, 4, 5]


a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)              # [11, 22, 33]


prices = [1.234, 5.678, 9.012]
rounded = list(map(lambda p: round(p, 2), prices))
print(rounded)           # [1.23, 5.68, 9.01]