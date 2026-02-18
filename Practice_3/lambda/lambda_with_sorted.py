words = ["banana", "kiwi", "apple", "fig"]
by_length = sorted(words, key=lambda w: len(w))
print(by_length)         # ['fig', 'kiwi', 'apple', 'banana']


numbers = [3, 1, 4, 1, 5, 9, 2, 6]
descending = sorted(numbers, key=lambda x: x, reverse=True)
print(descending)        # [9, 6, 5, 4, 3, 2, 1, 1]


students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob",   "grade": 95},
    {"name": "Carol", "grade": 72},
]
by_grade = sorted(students, key=lambda s: s["grade"])
print(by_grade)
# [{'name': 'Carol', 'grade': 72}, {'name': 'Alice', ...}, {'name': 'Bob', ...}]


pairs = [(1, "banana"), (2, "apple"), (3, "cherry")]
by_fruit = sorted(pairs, key=lambda p: p[1])
print(by_fruit)          # [(2, 'apple'), (1, 'banana'), (3, 'cherry')]


names = ["charlie", "Alice", "bob", "Dave"]
case_insensitive = sorted(names, key=lambda n: n.lower())
print(case_insensitive)  # ['Alice', 'bob', 'charlie', 'Dave']