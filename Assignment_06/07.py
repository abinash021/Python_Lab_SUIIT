# Write a Python program that reads a text file and counts the frequency of each character (letters, digits, symbols) in the file. Display the results in a dictionary.

def count_characters(file_path):
    char_freq = {}
    with open(file_path, "r") as file:
        text = file.read()
        for char in text:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
    return char_freq

file_path = "text_file.txt"
character_frequency = count_characters(file_path)
print("Character frequency:", character_frequency)
