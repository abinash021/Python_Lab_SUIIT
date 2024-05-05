# Write a Python program that reads the contents of a text file, reverses the order of lines, and writes the reversed lines to a new file.

def reverse_lines(input_file, output_file):
    with open(input_file, "r") as infile:
        lines = infile.readlines()
        reversed_lines = reversed(lines)
        
        with open(output_file, "w") as outfile:
            for line in reversed_lines:
                outfile.write(line)

input_file = "input.txt"
output_file = "output.txt"
reverse_lines(input_file, output_file)
print("Lines reversed and written to", output_file)
