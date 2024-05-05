# Write a Python program that removes all vowels from a given string and displays the modified string.

def remove_vowels(string):
    vowels = "aeiouAEIOU"
    modified_string = ""
    for char in string:
        if char not in vowels:
            modified_string += char
    return modified_string

input_string = input("Enter a string: ")
modified_string = remove_vowels(input_string)
print("Modified string:", modified_string)
