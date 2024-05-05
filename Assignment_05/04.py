# Given a list of numbers, write a python program that extracts and displays a portion of the list (a slice) based on user-defined start and end indices.

def extract_slice(lst, start, end):
    return lst[start:end]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

start_index = int(input("Enter start index: "))
end_index = int(input("Enter end index: "))

result = extract_slice(numbers, start_index, end_index)
print("Extracted slice:", result)
