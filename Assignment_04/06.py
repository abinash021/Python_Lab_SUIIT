'''
Write a Python program that takes a sentence as input from the user and performs the following 
transformations using string functions:
a) Remove any leading or trailing whitespace from the input.
b) Convert the sentence to lowercase.
c) Replace all spaces with underscores ('_').
d) Display the transformed sentence as the output.

'''

def transform_sentence(sentence):
    # Remove leading and trailing whitespace
    sentence = sentence.strip()
    
    # Convert to lowercase
    sentence = sentence.lower()
    
    # Replace spaces with underscores
    sentence = sentence.replace(' ', '_')
    
    return sentence

# Take input from the user
input_sentence = input("Enter a sentence: ")

# Transform the sentence
transformed_sentence = transform_sentence(input_sentence)

# Display the transformed sentence
print("Transformed sentence:", transformed_sentence)
