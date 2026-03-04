import os

# 1. Create a single directory
os.mkdir("new_folder")

# 2. Create nested directories
os.makedirs("parent/child/grandchild")

# 3. List all files in a directory
files = os.listdir(".")
print(files)

# 4. List only .py files
py_files = [f for f in os.listdir(".") if f.endswith(".py")]
print(py_files)

# 5. Check if directory exists before creating
if not os.path.exists("new_folder"):
    os.mkdir("new_folder")
else:
    print("Already exists")