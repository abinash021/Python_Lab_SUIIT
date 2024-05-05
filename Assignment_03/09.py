# Write a Python program to create a function called average that calculates the average of any number of arguments passed to it. Test the function with different numbers of arguments.

def average(*args):
    if len(args) == 0:
        return 0
    else:
        return sum(args) / len(args)

print("Average:", average(2, 4, 6, 8))
print("Average:", average(10, 20, 30))
print("Average:", average(1, 3, 5, 7, 9))
print("Average:", average())
