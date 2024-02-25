#Write a Python program that swaps the values of two variables with and without using a temporary variable.

x= int(input("Enter first number: "))
y= int(input("Enter second number: "))

print("Before swapping:")
print("x =", x)
print("y =", y)

x = x + y
y = x - y
x = x - y

print("\nAfter swapping:")
print("x =", x)
print("y =", y)

