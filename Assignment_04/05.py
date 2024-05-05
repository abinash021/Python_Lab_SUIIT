# Write a Python program that asks the user to enter a sentence and then displays the sentence in all uppercase and all lowercase without using any bulit-in function.

def to_uppercase(sentence):
    uppercase_sentence = ""
    for char in sentence:
        if 'a' <= char <= 'z':
            uppercase_sentence += chr(ord(char) - 32)
        else:
            uppercase_sentence += char
    return uppercase_sentence

def to_lowercase(sentence):
    lowercase_sentence = ""
    for char in sentence:
        if 'A' <= char <= 'Z':
            lowercase_sentence += chr(ord(char) + 32)
        else:
            lowercase_sentence += char
    return lowercase_sentence

sentence = input("Enter a sentence: ")

uppercase_sentence = to_uppercase(sentence)
lowercase_sentence = to_lowercase(sentence)

print("Uppercase:", uppercase_sentence)
print("Lowercase:", lowercase_sentence)
