# Write a Python program to create function called ‘capitalize_words’ that takes a string as input and returns the same string with the first letter of each word capitalized. Use string functions to achieve this.

def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

test_sentence = "this is a sample string"
capitalized_sentence = capitalize_words(test_sentence)
print("Capitalized sentence:", capitalized_sentence)
