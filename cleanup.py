import os

directory_path = "./groupby_10000"

# Walk through all directories and subdirectories
for root, dirs, files in os.walk(directory_path):
    for file in files:
        # Delete all answer files
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)
            os.remove(file_path)
            print(f"Deleted: {file_path}")