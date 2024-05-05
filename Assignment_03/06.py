# Write a Python program to implement a recursive function to calculate the factorial of a non-negative integer.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial of 5:", factorial(5))
print("Factorial of 7:", factorial(7))
print("Factorial of 0:", factorial(0))
