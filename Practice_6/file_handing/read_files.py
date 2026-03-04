# Reading files in Python

# 1. Read entire file
with open("C:\\Users\\User\\kalmik\\PP2_Practices-2026\\Practice_6\\data.txt", "r") as f:
    content = f.read()
    print(content + '\n')  

# 2. Read line by line
with open("C:\\Users\\User\\kalmik\\PP2_Practices-2026\\Practice_6\\data.txt", "r") as f:
    for line in f:
        print(line.strip() + '\n')  

# 3. Read all lines into a list
with open("C:\\Users\\User\\kalmik\\PP2_Practices-2026\\Practice_6\\data.txt", "r") as f:
    lines = f.readlines()
    print(lines)  # ['line1\n', 'line2\n', ...]
    print()

# 4. Read first N lines
with open("C:\\Users\\User\\kalmik\\PP2_Practices-2026\\Practice_6\\data.txt", "r") as f:
    for i, line in enumerate(f):
        if i == 2: break
        print(line.strip() + '\n')

# 5. Read with encoding
with open("C:\\Users\\User\\kalmik\\PP2_Practices-2026\\Practice_6\\data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content + '\n')