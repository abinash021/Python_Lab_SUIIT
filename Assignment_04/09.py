# Write a Python program to create a function that takes a string as input and counts the frequency of each character (case-insensitive). Display the results in a dictionary.

def count_character_frequency(string):
    string = string.lower()
    frequency_dict = {}
    for char in string:
        if char.isalnum():
            frequency_dict[char] = frequency_dict.get(char, 0) + 1
    
    return frequency_dict

test_string = "Hello, World!"
frequency = count_character_frequency(test_string)
print("Character frequency:", frequency)
