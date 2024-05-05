# Write a Python function that takes a list and returns a new list with its elements reversed. Do not use the reverse() method.

def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print("Reversed list:", reversed_list)
