# Practice6 — Python File Handling, Directory Management & Built-in Functions

A collection of Python examples covering file I/O, directory operations, and key built-in functions.

---

## 📁 Repository Structure

```
Practice6/
├── file_handling/
│   ├── read_files.py
│   ├── write_files.py
│   └── copy_delete_files.py
├── directory_management/
│   ├── create_list_dirs.py
│   └── move_files.py
├── builtin_functions/
│   ├── map_filter_reduce.py
│   └── enumerate_zip_examples.py
└── README.md
```

---

## 📄 file_handling/

### `read_files.py`
Demonstrates different ways to read files in Python.

| Method | Description |
|---|---|
| `f.read()` | Reads entire file as a string |
| `f.readline()` | Reads one line at a time |
| `f.readlines()` | Returns all lines as a list |
| `enumerate(f)` | Reads with line index |
| `encoding="utf-8"` | Handles special characters |

```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
```

---

### `write_files.py`
Covers writing and appending content to files.

| Mode | Description |
|---|---|
| `"w"` | Write — overwrites existing content |
| `"a"` | Append — adds to existing content |
| `f.write()` | Writes a single string |
| `f.writelines()` | Writes a list of strings |

```python
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
```

---

### `copy_delete_files.py`
Uses `shutil` and `os` modules to copy, delete, and manage files.

| Function | Description |
|---|---|
| `shutil.copy(src, dst)` | Copies a file |
| `os.remove(path)` | Deletes a file |
| `os.path.exists(path)` | Checks if file exists |
| `shutil.move(src, dst)` | Moves or renames a file |

```python
import shutil
shutil.copy("data.txt", "data_backup.txt")
```

---

## 📁 directory_management/

### `create_list_dirs.py`
Creating and listing directories using the `os` module.

| Function | Description |
|---|---|
| `os.mkdir(path)` | Creates a single directory |
| `os.makedirs(path)` | Creates nested directories |
| `os.listdir(path)` | Lists files in a directory |
| `os.path.exists(path)` | Checks if directory exists |

```python
import os
os.makedirs("parent/child/grandchild")
```

---

### `move_files.py`
Moving and renaming files and folders.

| Function | Description |
|---|---|
| `shutil.move(src, dst)` | Moves file or folder |
| `os.rename(old, new)` | Renames a file |

```python
import shutil
shutil.move("report.txt", "archive/report_2024.txt")
```

---

## 📁 builtin_functions/

### `map_filter_reduce.py`
Core functional programming tools in Python.

| Function | Description |
|---|---|
| `map(fn, iterable)` | Applies function to every element |
| `filter(fn, iterable)` | Keeps elements where function returns `True` |
| `reduce(fn, iterable)` | Accumulates elements into a single value |

```python
from functools import reduce

nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))   # [1, 4, 9, 16, 25]
evens   = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]
total   = reduce(lambda x, y: x + y, nums)    # 15
```

---

### `enumerate_zip_examples.py`
Useful built-ins for working with iterables.

| Function | Description |
|---|---|
| `enumerate(iterable, start)` | Adds index to each element |
| `zip(a, b)` | Pairs elements from multiple iterables |
| `dict(zip(keys, values))` | Builds a dictionary from two lists |

```python
# enumerate
for i, fruit in enumerate(["apple", "banana"], start=1):
    print(f"{i}. {fruit}")

# zip
for name, score in zip(["Alice", "Bob"], [95, 87]):
    print(f"{name}: {score}")
```

---

## 🚀 Getting Started

**Clone the repository:**
```bash
git clone https://github.com/your-username/Practice6.git
cd Practice6
```

**Run any example:**
```bash
python file_handling/read_files.py
python builtin_functions/map_filter_reduce.py
```

**Requirements:** Python 3.x — no external libraries needed.

---

## 📌 Key Concepts Summary

| Topic | Modules Used |
|---|---|
| File reading/writing | `open()`, built-in |
| Copy & delete files | `shutil`, `os` |
| Directory management | `os`, `shutil` |
| Functional tools | `map`, `filter`, `functools.reduce` |
| Iteration helpers | `enumerate`, `zip` |

---

## 👤 Author

> Replace with your name and GitHub profile link.
