# Write a Python program that checks if a given string is a palindrome (reads the same forwards and backwards) and returns a boolean result.

def is_palindrome(string):
    string = string.lower()
    string = ''.join(char for char in string if char.isalnum())
    return string == string[::-1]

test_string = "A man, a plan, a canal, Panama"
result = is_palindrome(test_string)
print("Is the string a palindrome?", result)
