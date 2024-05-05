# Write a Python program to create a function that takes a list of numbers as input and calculates and returns the sum of all the numbers in the list.

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers_list = [1, 2, 3, 4, 5]
print("Sum of the numbers:", calculate_sum(numbers_list))
