#  Write a Python program to define a function ‘divide_and_remainder’ that takes two numbers as input and returns both the quotient and remainder when the first number is divided by the second.

def divide_and_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

dividend1 = 10
divisor1 = 3
quotient1, remainder1 = divide_and_remainder(dividend1, divisor1)
print("Quotient:", quotient1)
print("Remainder:", remainder1)

dividend2 = 20
divisor2 = 4
quotient2, remainder2 = divide_and_remainder(dividend2, divisor2)
print("Quotient:", quotient2)
print("Remainder:", remainder2)

dividend3 = 15
divisor3 = 7
quotient3, remainder3 = divide_and_remainder(dividend3, divisor3)
print("Quotient:", quotient3)
print("Remainder:", remainder3)
