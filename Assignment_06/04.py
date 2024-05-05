# Write a Python program that copies the content of one text file (e.g., "source.txt") to another text file (e.g., "destination.txt"). Ensure that the program works for files of different sizes.

def copy_file(source_file, destination_file):
    with open(source_file, "r") as source:
        with open(destination_file, "w") as destination:
            for line in source:
                destination.write(line)

source_file = "source.txt"
destination_file = "destination.txt"

copy_file(source_file, destination_file)
print(f"Content from {source_file} copied to {destination_file}.")
