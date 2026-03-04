import shutil
import os

# 1. Move file to another directory
shutil.move("data.txt", "archive/data.txt")

# 2. Rename a file
os.rename("old_name.txt", "new_name.txt")

# 3. Move entire folder
shutil.move("old_folder", "new_location/old_folder")

# 4. Move all .txt files to a folder
os.makedirs("texts", exist_ok=True)
for f in os.listdir("."):
    if f.endswith(".txt"):
        shutil.move(f, f"texts/{f}")

# 5. Move and rename at the same time
shutil.move("report.txt", "archive/report_2024.txt")