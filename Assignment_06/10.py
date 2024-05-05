# Write a program that searches for a specific word or phrase in all text files within a specified directory and its subdirectories. Display the list of matching files

import os

def search_files(directory, search_term):
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    content = f.read()
                    if search_term in content:
                        matching_files.append(file_path)
    return matching_files

directory = "path/to/directory"
search_term = "specific_word_or_phrase"

matching_files = search_files(directory, search_term)
if matching_files:
    print("Matching files:")
    for file_path in matching_files:
        print(file_path)
else:
    print("No matching files found.")
