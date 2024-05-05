# Write a Python program that reads a text file and counts the number of words in it. Display the word count as the output.

def count_words(file_path):
    with open(file_path, "r") as file:
        text = file.read()
        word_count = len(text.split())
        return word_count

file_path = "text_file.txt"
word_count = count_words(file_path)
print("Number of words in the file:", word_count)
