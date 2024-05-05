# Write a Python program that reads a text file and replaces all occurrences of a specified word or phrase with another word or phrase. Save the modified text to a new file.

def replace_word(input_file, output_file, old_word, new_word):
    with open(input_file, "r") as infile:
        text = infile.read()
        modified_text = text.replace(old_word, new_word)
        
        with open(output_file, "w") as outfile:
            outfile.write(modified_text)

input_file = "input.txt"
output_file = "output.txt"
old_word = "old_word"
new_word = "new_word"
replace_word(input_file, output_file, old_word, new_word)
print("Modified text saved to", output_file)
