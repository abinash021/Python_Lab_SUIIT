# Write a Python program that sorts a list of strings in ascending order and displays the sorted list. Ensure the original list remains unchanged.

def sort_strings(lst):
    return sorted(lst)

original_list = ["banana", "apple", "grape", "orange"]
sorted_list = sort_strings(original_list)
print("Sorted list:", sorted_list)
