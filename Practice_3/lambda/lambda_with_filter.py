numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)             # [2, 4, 6, 8]


values = [-3, -1, 0, 2, 5, -7, 9]
positives = list(filter(lambda x: x > 0, values))
print(positives)         # [2, 5, 9]


words = ["cat", "elephant", "dog", "python", "ox"]
long_words = list(filter(lambda w: len(w) > 4, words))
print(long_words)        # ['elephant', 'python']


names = ["Alice", "bob", "Charlie", "dave", "Eve"]
capitalized = list(filter(lambda n: n[0].isupper(), names))
print(capitalized)       # ['Alice', 'Charlie', 'Eve']


lines = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda s: s != "", lines))
print(non_empty)         # ['hello', 'world', 'python']