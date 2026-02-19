import math
import random

# 1. Basic math functions
print(math.sqrt(25))        # 5.0
print(math.pi)              # 3.14159...

# 2. Floor and ceil
print(math.floor(4.9))      # 4
print(math.ceil(4.1))       # 5

# 3. Power and log
print(math.pow(2, 10))      # 1024.0
print(math.log(100, 10))    # 2.0

# 4. Random integer
num = random.randint(1, 100)
print(num)                  # random number 1-100

# 5. Random choice and shuffle
fruits = ["apple", "banana", "kiwi"]
print(random.choice(fruits))   # random fruit
random.shuffle(fruits)
print(fruits)                  # shuffled list