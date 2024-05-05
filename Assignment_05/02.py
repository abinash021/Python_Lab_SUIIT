# Write a Python program that concatenates two lists and displays the resulting list. For example, if you have lists [1, 2, 3] and [4, 5, 6], the program should return [1, 2, 3, 4, 5, 6].

def concatenate_lists(list1, list2):
    return list1 + list2

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result_list = concatenate_lists(list1, list2)
print("Concatenated list:", result_list)
