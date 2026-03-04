import shutil
import os

# 1. Copy a file
shutil.copy("data.txt", "data_backup.txt")

# 2. Copy file to another folder
shutil.copy("data.txt", "backup/data.txt")

# 3. Delete a file
os.remove("data_backup.txt")

# 4. Check if file exists before deleting
if os.path.exists("data_backup.txt"):
    os.remove("data_backup.txt")
else:
    print("File not found")

# 5. Move (rename) a file
shutil.move("data.txt", "archive/data_old.txt")