# Extend the previous program to append the text "Appending to the file" to the end of the "sample.txt" file without overwriting its existing content.

with open("sample.txt", "a") as file:
    file.write("\nAppending to the file")
