from functools import reduce

nums = [1, 2, 3, 4, 5]

# 1. map() — apply function to each element
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # [1, 4, 9, 16, 25]

# 2. filter() — keep elements that match condition
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)    # [2, 4]

# 3. reduce() — accumulate into single value
total = reduce(lambda x, y: x + y, nums)
print(total)    # 15

# 4. map() with multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
result = list(map(lambda x, y: x + y, a, b))
print(result)   # [11, 22, 33]

# 5. Chain map + filter
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums)))
print(result)   # [4, 16]  ← squares of even numbers