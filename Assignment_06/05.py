# Develop a Python program that deletes the "sample.txt" file if it exists. Check if the file exists before attempting to delete it.

import os

file_path = "sample.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} has been deleted.")
else:
    print(f"{file_path} does not exist.")
