# Writing files in Python

# 1. Write (overwrites existing content)
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")

# 2. Append to existing file
with open("output.txt", "a") as f:
    f.write("New line added\n")

# 3. Write multiple lines at once
lines = ["apple\n", "banana\n", "cherry\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)

# 4. Write integers (must convert to str)
nums = [1, 2, 3, 4, 5]
with open("output.txt", "w") as f:
    for n in nums:
        f.write(str(n) + "\n")

# 5. Write and read back
with open("output.txt", "w") as f:
    f.write("Python is great!")

with open("output.txt", "r") as f:
    print(f.read())  # Python is great!