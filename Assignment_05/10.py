# Write a Python program that finds and displays the largest and smallest elements in a list without using built-in functions.

def find_max_min(lst):
    if not lst:
        return None, None
    
    max_num = lst[0]
    min_num = lst[0]
    
    for num in lst:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    
    return max_num, min_num

# Example usage:
numbers = [3, 7, 2, 8, 1, 6, 4, 9, 5]
largest, smallest = find_max_min(numbers)
print("Largest:", largest)
print("Smallest:", smallest)
