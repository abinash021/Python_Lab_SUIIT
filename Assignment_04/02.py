# Write a Python program to create a function that calculates and returns the length of a given string without using the built-in len() function.

def calculate_length(string):
    count = 0
    for _ in string:
        count += 1
    return count


test_string = "Hello, World!"
length = calculate_length(test_string)
print("Length of the string:", length)
