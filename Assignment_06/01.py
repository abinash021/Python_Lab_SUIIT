# Write a Python program that creates a new text file named "sample.txt" and writes the text "Hello, World!" to it. Ensure that the file is properly closed after writing.

with open("sample.txt", "w") as file:
    file.write("Hello, World!")
