# Write a Python program to create a function power that raises a number to a specified power. Make the power parameter optional with a default value of 2.

def power(number, exponent=2):
    return number ** exponent

print(power(3)) 
print(power(4, 3)) 
print(power(2, 5)) 
