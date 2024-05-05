# Write a Python program that define two functions, square(x) and double(x), that perform mathematical operations on a number. Use function composition to create a new function called ‘square_and_double(x)’ that squares the number and then doubles the result.

def square(x):
    return x ** 2

def double(x):
    return 2 * x

def square_and_double(x):
    return double(square(x))

number = 5
print("Square of", number, ":", square(number))
print("Double of", number, ":", double(number))
print("Square and double of", number, ":", square_and_double(number))
