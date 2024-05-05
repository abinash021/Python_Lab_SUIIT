# Write a Python program that reads and displays the contents of the "sample.txt" file created in the previous question.

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
