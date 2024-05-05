# Write a Python program to create a function that takes a list of numbers with duplicates and returns a new list with duplicates removed while preserving the original order.

def remove_duplicates(lst):
    unique_elements = []
    seen = set()
    for num in lst:
        if num not in seen:
            unique_elements.append(num)
            seen.add(num)
    return unique_elements

numbers_with_duplicates = [1, 2, 3, 2, 4, 5, 6, 1, 3, 7, 8, 9, 9]
result = remove_duplicates(numbers_with_duplicates)
print("List with duplicates removed:", result)
