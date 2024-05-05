# Write a Python program to create a function that rotates the elements of an array (list) to the right by a given number of positions.

def rotate_right(arr, positions):
    n = len(arr)
    positions %= n
    return arr[-positions:] + arr[:-positions]

arr = [1, 2, 3, 4, 5]
rotated_arr = rotate_right(arr, 2)
print("Original array:", arr)
print("Rotated array:", rotated_arr)
