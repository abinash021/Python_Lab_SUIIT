""""
Write a python program to check the validity of a password given by the user. The password should satisfy the following criteria: 
a)	Contain at least 1 letter between a and z 
b)	Contain at least 1 number between 0 and 9 
c)	Contain at least 1 letter between A and Z 
d)	Contain at least 1 character from $, #, @ 
e)	Minimum length of password: 6 
f)	Maximum length of password: 12
Based on above criteria checks password strength (weak, moderate, strong).

"""
password = input("Enter a password: ")

has_lower = any(char.islower() for char in password)
has_upper = any(char.isupper() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in ['$','#','@'] for char in password)

if 6 <= len(password) <= 12 and has_lower and has_upper and has_digit and has_special:
    print("Strong password")
elif len(password) < 6 or len(password) > 12:
    print("Weak password: Length should be between 6 and 12 characters")
else:
    print("Moderate password: It should contain at least one lowercase letter, one uppercase letter, one digit, and one of the characters $, #, or @")
