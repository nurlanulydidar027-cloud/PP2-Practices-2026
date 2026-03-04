# 1. enumerate() — index + value
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# 1. apple  2. banana  3. cherry

# 2. zip() — pair two lists
names  = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# 3. zip() → dict
keys   = ["name", "age", "city"]
values = ["Alice", 25, "NYC"]
d = dict(zip(keys, values))
print(d)  # {'name': 'Alice', 'age': 25, 'city': 'NYC'}

# 4. enumerate() + zip() together
for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{i}. {name} → {score}")

# 5. zip() to transpose a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = list(zip(*matrix))
print(transposed)  # [(1,4,7), (2,5,8), (3,6,9)]