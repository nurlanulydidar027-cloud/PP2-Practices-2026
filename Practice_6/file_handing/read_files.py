# Reading files in Python

# 1. Read entire file
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

# 2. Read line by line
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())

# 3. Read all lines into a list
with open("data.txt", "r") as f:
    lines = f.readlines()
    print(lines)  # ['line1\n', 'line2\n', ...]

# 4. Read first N lines
with open("data.txt", "r") as f:
    for i, line in enumerate(f):
        if i == 3: break
        print(line.strip())

# 5. Read with encoding
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)