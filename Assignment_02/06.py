# Develop a Python program that calculates the factorial of a non-negative integer entered by the user using a while loop.

num = int(input("Enter a non-negative integer: "))

factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print("Factorial of", num, "is", factorial)


