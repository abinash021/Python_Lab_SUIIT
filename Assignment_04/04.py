# Given a string, write a Python program that extracts and displays the first three characters, the last three characters, and a substring from the middle of the string.

def extract_parts(string):
    length = len(string)
    first_three = string[:3]
    last_three = string[-3:]
    
    start_index = (length - 3) // 2
    
    middle_substring = string[start_index:start_index + 3]

    return first_three, last_three, middle_substring

input_string = input("Enter a string: ")

first_three, last_three, middle_substring = extract_parts(input_string)

print("First three characters:", first_three)
print("Last three characters:", last_three)
print("Middle substring:", middle_substring)
