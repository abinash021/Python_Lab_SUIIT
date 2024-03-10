# Write a Python program that prompts the user to enter the coefficients of a quadratic equation (a, b, and c) and solves the equation, displaying the roots (real or complex) as output.

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

d = (b**2) - (4*a*c)

if d > 0:
    root1 = (-b + d **0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    print("Root 1 =", root1)
    print("Root 2 =", root2)
elif d == 0:
    root = -b / (2*a)
    print("Root =", root)
else:
    real_part = -b / (2*a)
    imaginary_part = (d**0.5) / (2*a)
    print("Root 1 =", real_part, "+", imaginary_part, "i")
    print("Root 2 =", real_part, "-", imaginary_part, "i")

# Note: 
# 2 ** 3 = 8, as 2 raised to the power of 3 is 8.
# 4 ** 0.5 = 2.0, as 4 raised to the power of 0.5 (square root) is 2.0.